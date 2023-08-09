import json
import os
import re
import logging
import natsort
from .getfile import fileName, getFile
from .xmlparser import getRoot, divList, metadata
from .utils.settings import settings
from pprint import pp

settings = settings()
filename = fileName()
r = getFile(filename)
root = getRoot(r)
div_list = divList(root)
metadata = metadata(root)

idno = metadata["idno"]
temp_dir = settings["temp_dir"]
manifest_store = settings["manifest_store"]
trailing_pattern = settings["regex"]["trailing_pattern"]

def dirGen() -> None:
  """
  Generates directory for output files
  """

  try:
    os.mkdir(f'./{idno}-manifests')
    logging.debug(f'Created directory at ./{idno}-manifests')
  except FileExistsError as e:
    logging.debug(str(e) + ' directory already exists. Continuing...', exc_info=True)

def manifestGen(idno, temp_dir, manifest_store) -> list:
  """
  Generates IIIF annotationPage manifests and returns a list of manifests

  """
  dirGen()

  file_list = natsort.natsorted(os.listdir(temp_dir))
  manifest_list = []

  for counter, filename in enumerate(file_list):

    f = os.path.join(temp_dir, filename)
    if f.endswith(".json"):
      with open(f, 'r') as jsonfile:
        data = json.load(jsonfile)

        keys = data.keys()
        values = data.values()

        items_list = []
        annotation_page = {
          "@context": "http://iiif.io/api/presentation/3/context.json",
          "id": manifest_store + f"/annotations/{idno}-annotations/{idno}-{counter + 1}-annotations.json",
          "type": "AnnotationPage",
          "items": items_list
      }
        inner_counter = 1
        for key, value in zip(keys, values):

          keySanitiser = lambda key: re.sub(r'/(\d+),', r'#xywh=\1,', key).strip(trailing_pattern)

          annotation_individual = {
            "id": manifest_store + f"/{idno}-annotation#{inner_counter}.json",
            "type": "Annotation",
            "motivation": "commenting",
            "target": keySanitiser(key),
            "body": {
              "type": "TextualBody",
              "language": "en",
              "format": "text/html",
              "value": [value.strip() for value in value]
            }
          }
          inner_counter += 1
          items_list.append(annotation_individual)
        
        manifest_list.append(annotation_page)

    for file in temp_dir:
      if file.endswith('.json'):
        logging.info(f'Generating IIIF AnnotationPage manifests for {filename}...')

  return manifest_list

def jsonSave(manifest_list, idno) -> None:
    for file_counter, annotation_page in enumerate(manifest_list):
      with open(f"./{idno}-manifests/{idno}-{file_counter +1}-annotations.json", "w") as jsonfile:
      
        json.dump(annotation_page, jsonfile, indent=4)
    
    for file in temp_dir:
      if file.endswith('.json'):
        logging.info(f'Saving {idno} manifests to JSON...')