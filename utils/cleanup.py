from utils.settings import settings
import logging
import os
import shutil

temp_dir = settings["temp_dir"]

def xmlCleaner() -> None:
  """
  Cleans up temporary XML files
  """
  try:
    for file in temp_dir:
        if file.endswith(".xml"):
            os.remove(file)
        else:
            pass
  except FileNotFoundError as e:
      logging.error(e)

def dirCleaner() -> None:
  """
  Removes up temp directory
  """
  try:
    shutil.rmtree(temp_dir)
  except OSError as e:
    logging.error(f"Error: {e.filename} - {e.strerror}.")

  logging.info('Cleaning up temporary files...')
