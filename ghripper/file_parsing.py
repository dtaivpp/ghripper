import logging
import json
import yaml
from ghripper.helpers import yaml_recursor

logger = logging.getLogger("debug")


def input_parse(file_path:str):
  """Parese the input yaml or txt file"""
  logger.debug("Parsing input file: %s", file_path)
  if file_path.endswith(".yaml"):
    ouput = input_yaml_file_parse(file_path)
  return ouput


def input_yaml_file_parse(file_path: str, options: str) -> list:
  """Parse input yaml files"""
  with open(file_path, "r", encoding="UTF-8") as stream:
    try:
      config = yaml.safe_load(stream)
      return config
    except yaml.YAMLError as exc:
      logger.exception(exc)


def statefile_parse(file_path: str, data: list):
  """Output the json or csv file"""
  if file_path.endswith('.json'):
    output_json_file(data, file_path)
  elif file_path.endswith('.csv'):
    output_csv_file(data, file_path)
  else:
    logger.error("Invalid ouput format")


def output_json_file(data, filename):
  """Output the data as a JSON File"""
  if len(data) == 0:
    return

  logger.debug("Writing JSON File: %s", filename)
  with open(filename, "+w", encoding="UTF-8") as outfile:
    json.dump(data, outfile, indent = 4)



def output_csv_file(data, filename):
  """Output the data as a CSV File"""
  if len(data) == 0:
    return

  logger.debug("Writing CSV File: %s", filename)
  with open(filename, "+w", encoding="UTF-8") as outfile:
    outfile.write("dork, repository, path, score\n")
    for entry in data:
      outfile.write(f"{entry['dork']}, {entry['repository']}, {entry['path']}, {entry['score']}\n")
