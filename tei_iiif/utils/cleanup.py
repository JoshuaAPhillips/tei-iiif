from .settings import settings
import logging
import os
import shutil

settings = settings()
temp_dir = settings["temp_dir"]

def xmlCleaner(temp_dir) -> None:
  """
  Cleans up temporary XML files
  """
  try:
    for file in temp_dir:
        if file.endswith(".xml"):
          os.remove(file)
          logging.info(f"Removed file at {file}")
        else:
          pass
  except FileNotFoundError as e:
    logging.error(e)

def dirCleaner(temp_dir) -> None:
  """
  Removes up temp directory
  """
  try:
    shutil.rmtree(temp_dir)
    logging.info(f"Removed directory at {temp_dir}")
  except OSError as e:
    logging.error(f"Error: {e.filename} - {e.strerror}.")