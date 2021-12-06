import logging
import argparse
from os import path
from os import getenv
import re
from dotenv import load_dotenv
from ghripper.file_parsing import input_parse
from git.repo.base import Repo
from ghsearcher.searcher import search, get_client

load_dotenv()
GH_TOKEN = getenv('GH_TOKEN', None)

#### Logging config
console_out = logging.getLogger("ghripper")
consoleOutHandle = logging.StreamHandler()
consoleOutHandle.setLevel(logging.INFO)
consoleOutFormatter = logging.Formatter('%(asctime)s - %(message)s')
consoleOutHandle.setFormatter(consoleOutFormatter)
console_out.addHandler(consoleOutHandle)
console_out.setLevel(logging.INFO)

logger = logging.getLogger("debug")
consoleHandle = logging.StreamHandler()
consoleHandle.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
consoleHandle.setFormatter(formatter)
logger.addHandler(consoleHandle)
logger.setLevel(logging.ERROR)


def perform_changes(repos_to_change, reposdir):
  
  for ghcontext in repos_to_change: 
    for found_repo in ghcontext.matches: 
      repo = clone_repo(found_repo['repository']['full_name'], reposdir, ghcontext.ssh)
      
      if ghcontext.branch_name is not None:
        create_and_checkout_branch(repo, ghcontext.branch_name)
      
      # Repo[path] here looks like 'some/dir/and/file.txt'
      replace_file = path.join(repo.working_dir, *repo['path'].split('/'))
      find_and_replace(replace_file, ghcontext.find, ghcontext.replace_with)
      
      if ghcontext.commit_message is not None:
        commit(repo, replace_file, ghcontext.commit_message)
  
      if ghcontext.push:
        repo.git.push()


def commit(repo,file, message):
  """Function for committing a change"""
  repo.git.add(file)
  repo.git.commit('-m', message)


def find_and_replace(file_path, find, replace):
  """Find and replace an exact string in a file"""
  # Read in the file
  with open(file_path, 'r') as file :
    filedata = file.read()

  # Replace the target string
  filedata = filedata.replace(find, replace)

  # Write the file out again
  with open(file_path, 'w') as file:
    file.write(filedata)


def create_and_checkout_branch(repo: Repo, branch_name: str):
  """Create and check out the specified branch"""
  origin = repo.remote()
  repo.create_head(branch_name)
  origin.push(branch_name)
  repo.git.checkout(branch_name)


def clone_repo(repo: str, path: str, ssh: bool) -> Repo:
  url = f"git@github.com:{repo}.git" if ssh else f"https://github.com/{repo}.git"
  return Repo.clone_from(url, path)


def main(debug, config, reposdir):
  """Main logic of the program"""
  if debug:
    logger.setLevel(logging.DEBUG)

  repos_to_change = input_parse(config)
  
  client = get_client()

  for search_context in repos_to_change:
    logger.debug("Running query: %s", search_context.query)

    for result in search(search_context.query, endpoint='code', client=client):
      search_context.found_repos(result)
    
    search_context.completed = True

  perform_changes(repos_to_change, reposdir)


def cli_entry():
  """Parse arguments and kickoff the process"""
  parser = argparse.ArgumentParser(
    description='Search and replace text in GitHub repositories')

  parser.add_argument(
    '-v',
    '--version',
    action='version',
    version='%(prog)s 0.0.1')

  parser.add_argument(
    '-c',
    '--config',
    default='config.yaml',
    help='Config file for what to find and replace')

  parser.add_argument(
    '-r',
    '--reposdir',
    help='Where you would like the repos cloned to'
  )

  parser.add_argument(
    '--debug',
    action='store_true',
    help='Set this if you would like to see verbose logging.')

  args = parser.parse_args()
  main(**vars(args))


if __name__=='__main__':
  cli_entry()
