# GitHub Ripper
GH Ripper is a utility for doing mass updates to github repos. It will find and replace text in any number of repositories and can commit them up to a new branch automatically. 

## Usage

1. Install with pip `pip install ghripper`
2. (Optional) you can either export an environment variable named "GH_TOKEN" or include it in a local .env file to ensure you can make the most requests. See ["Creating a personal access token"](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) for more information on how to do so.

```
usage: ghripper [-h] [-v] [-c CONFIG] [-r REPOSDIR] [--debug]

Search and replace text in GitHub repositories

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c CONFIG, --config CONFIG
                        Config file for what to find and replace
  -r REPOSDIR, --reposdir REPOSDIR
                        Where you would like the repos cloned to
  --debug               Set this if you would like to see verbose logging.
```

Here is a simple example:
```
# Specifying config and where we would like the repos to clone to.
ghripper -c config.yaml -r /Users/dtippett/tmp
```

Here is an example of an entry in your config file: 
```yaml
dtaivpp/cloud_haiku:
  scope: repo, org, user
  find: "Testing code long time" 
  replace_with: "NO"
  branch_name: "GHRipper_Replacement"
  commit_message: "Testing code long time -> NO"
  push: False
```

## Contributing

For how to contribute please see [CONTRIBUTING.md]("CONTRIBUTING.md").
