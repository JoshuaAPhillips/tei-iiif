import yaml
import os

def settings() -> dict:

  """
  Loads settings from ../settings.yaml and returns as a dictionary.
  """

  with open("settings.yaml", 'r') as f:
      settings = yaml.load(f, Loader=yaml.FullLoader)
      
  print(settings)

  return settings