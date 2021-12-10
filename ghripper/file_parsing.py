import logging
from typing import List
import yaml
from ghripper.helpers import GithubSearchContext

logger = logging.getLogger("debug")

def input_parse(file_path:str) -> List[GithubSearchContext]:
  """Parese the input yaml or txt file"""
  logger.debug("Parsing input file: %s", file_path)
  if file_path.endswith(".yaml"):
    output = input_yaml_file_parse(file_path)
    return [GithubSearchContext(context=key, **value) for key, value in output.items()]
  return


def input_yaml_file_parse(file_path: str) -> list:
  """Parse input yaml files"""
  with open(file_path, "r", encoding="UTF-8") as stream:
    try:
      config = yaml.safe_load(stream)
      return config
    except yaml.YAMLError as exc:
      logger.exception(exc)
      return
