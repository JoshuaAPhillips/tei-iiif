import sys
import logging
import requests
from utils.settings import settings

settings = settings()

def fileName() -> str:
    """
    Gets filename from command line argument and path specified in settings.yaml
    - (TODO: work on way to accept list of files and iterate through them)
    """
    base_url = settings["base_path"]
    filename = sys.argv[-1]

    if settings["base_path"] is not None:
      file = base_url + filename
      return file
    else:
       logging.error('Check "base_path" and "file_name" are set')

def getFile(file) -> object:
   """
   Returns file from local or remote store
   """
   if file.startswith("http"):
      try:
         r = requests.get(file)
         return r
      except FileNotFoundError as e:
         logging.error("File not found:" + e)

   else:
      try:
         r_wrapper = open(file, "r")
         r = r_wrapper.read()
         return r
      except FileNotFoundError as e:
         logging.error("File not found:" + e)