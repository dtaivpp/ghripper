import logging
import argparse
from os import getenv
from dotenv import load_dotenv
from ghapi.all import GhApi
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


def perform_changes(repos_to_change, config_file): 
  # workflow : 
      # - Clone repo's into a specified folder
      # - Create Branch and set to current
      # - Find the text and replace
      # - Create commit with message
      # - If Push then push
  pass


def clone_repo(repo: str, path: str, ssh: bool) -> None:
  url = f"git@github.com:{repo}.git" if ssh else f"https://github.com/{repo}.git"
  Repo.clone_from(url, path)


def main(debug, config):
  """Main logic of the program"""
  if debug:
    logger.setLevel(logging.DEBUG)

  input = input_parse(config)
  
  client = get_client()
  results = []

  for search_context in input:
    logger.debug("Running query: %s", search_context.query)

    for result in search(search_context.query, endpoint='code', client=client):
      search_context.found_repos(result)
    
    search_context.u

  
  perform_changes(results, input)


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
    '--debug',
    action='store_true',
    help='Set this if you would like to see verbose logging.')

  args = parser.parse_args()
  main(**vars(args))


if __name__=='__main__':
  cli_entry()
