import yaml
import logging


def settings() -> dict:

  """
  Loads settings from `../settings.yaml` and returns as a dictionary so that other functions can access.
  """
  try:
    with open("./settings.yaml", 'r') as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
        return settings

  except FileNotFoundError as e:
     logging.error(e)