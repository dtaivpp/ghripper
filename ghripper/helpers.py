"""Helper classes for managing state"""

class GithubSearchContext():
  """Search Context class for manageing search state.

  Parameters:
  -----------
    context = The name of the repo, org, or user you are searching
    scope = {user, org, repo}
    find = Text to find in the repo
    replace_with = Replacement string
    push = Whether or not you want to push your changes
    commit_message = Commit message to push
    branch_name = Branch name to use if pusing to a new branch
    ssh = Whether you are using git+ssh
  """
  def __init__(self,
               context,
               scope,
               find,
               replace_with,
               push=False,
               commit_message=None,
               branch_name=None,
               ssh=None):
    self.context = context
    self.find = find
    self.scope = scope
    self.replace_with = replace_with
    self.branch_name = branch_name
    self.commit_message = commit_message
    self.query = f"{find} {scope}:{context}"
    self.push = push
    self.completed = False
    self.ssh =  bool(ssh not in [None, False])
    self.matches = []


  def found_repos(self, repos):
    """Add repos as they are found"""
    self.matches.extend(repos)
