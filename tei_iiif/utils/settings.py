import yaml
import logging
import importlib.resources


def settings() -> dict:

  """
  Loads settings from `../settings.yaml` and returns as a dictionary so that other functions can access.
  """
  try:
    settings_file = importlib.resources.read_text("tei_iiif", "settings.yaml")
    settings = yaml.safe_load(settings_file)
    logging.info("Settings loaded.")
    return settings

  except FileNotFoundError as e:
     logging.error(e)