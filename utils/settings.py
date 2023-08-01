import yaml
import logging

def settings() -> dict:

  """
  Loads settings from ../settings.yaml and returns as a dictionary.
  """
  try:
    with open("settings.yaml", 'r') as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
        
  except FileNotFoundError as e:
     logging.ERROR(e)

  return settings