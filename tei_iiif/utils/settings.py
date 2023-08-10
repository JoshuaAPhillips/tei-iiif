import yaml
import logging


def settings() -> dict:

  """
  Loads settings from `../settings.yaml` and returns as a dictionary so that other functions can access.
  """
  try:
    with open("tei_iiif/settings.yaml", 'r') as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
        logging.info("Settings loaded.")
        return settings

  except FileNotFoundError as e:
     logging.error(e)