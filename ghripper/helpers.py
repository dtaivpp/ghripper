from fastcore.xtras import truncstr


class GithubSearchContext():
  def __init__(self, 
               context, 
               find,
               scope, 
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
    self.ssh = False if ssh is None else self.ssh=True
    

    self.matches = []


  def found_repos(self, repos):
    self.matches.extend(repos)
