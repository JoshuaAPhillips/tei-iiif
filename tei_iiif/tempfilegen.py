from .utils.settings import settings
from .getfile import fileName, getFile
from .xmlparser import getRoot, divList, metadata
from lxml import etree
import os
import logging

settings = settings()

filename = fileName()
file = getFile(filename)
root = getRoot(file)
div_list = divList(root)
metadata_dict = metadata(root)

def tempDir() -> None:
  """
  Generates temporary directory for storing files
  """
  
  try:
    os.mkdir(settings["temp_dir"])
    logging.info("Created temporary directory at {}".format(settings["temp_dir"]))
  except FileExistsError:
    pass

def tempFileGen(div_list) -> None:
  """
  Generates temporary files for each `<div>` in the master list
  """
  tempDir()
  for idx, div in enumerate(div_list):
    filename = "./temp/{}-{}.xml".format(metadata_dict["idno"], idx + 1)
    with open(filename, "w") as f:
      f.write(etree.tostring(div, encoding="unicode"))
    logging.info("Created temporary file at {}".format(filename))

tempFileGen(div_list)
