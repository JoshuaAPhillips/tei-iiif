import sys
import logging
import requests
from utils.settings import settings

settings = settings()

def fileName() -> str:
    """
    Returns `filename` from command line argument and path specified in settings.yaml
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
   Returns `file` from local or remote store for parsing in `xmlparser.py`
   - Uses requests library to fetch remote files
      - Uses basic auth to fetch remote files: if auth required, set username and password in settings.yaml
      - If auth not required, leave username and password blank
      - If more advanced authentication systems such as OAuth are required, see https://requests.readthedocs.io/en/latest/user/authentication/ for implementation
   - Uses open() to fetch local files
   """
   
   if file.startswith("http"):
      try:
         r = requests.get(file, auth=(settings["request_params"]["username"], settings["request_params"]["password"]))
         if r.status_code == 200:
            return r
         else:
            logging.error("Error fetching file:" + r.status_code)
      except Exception as e:
         logging.error("Exception:" + e)

   else:
      try:
         r_wrapper = open(file, "r")
         r = r_wrapper.read()
         return r
      except FileNotFoundError as e:
         logging.error("File not found:" + e)