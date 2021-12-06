class GithubSearchContext():
  def __init__(self, 
               context, 
               find,
               scope, 
               replace_with, 
               branch_name, 
               commit_message, 
               push):
    self.context = context
    self.find = find
    self.scope = scope
    self.replace_with = replace_with
    self.branch_name = branch_name
    self.commit_message = commit_message
    self.query = f"{find} {scope}:{context}"
    self.push = push
    self.completed = False
    self.matches = []


  def found_repos(self, repos):
    self.matches.extend(repos)
