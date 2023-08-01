import sys
import logging
import requests
from utils.settings import settings

settings = settings()

def fileName() -> str:
    base_url = settings["base_path"]
    filename = sys.argv[-1]

    if settings["base_path"] is not None:
      file = base_url + filename
      print(file)
      return file
    else:
       logging.error('Check "base_path" and "file_name" are set')

def getFile(file) -> object:
   if file.startswith("http"):
      try:
         r = requests.get(file)
         print(r)
      except FileNotFoundError as e:
         logging.error("File not found:" + e)


file = fileName()
getFile(file)