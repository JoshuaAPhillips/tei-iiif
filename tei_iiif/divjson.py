import json
import os
import logging
from lxml import etree
from .utils.settings import settings

settings = settings()

def divJson(temp_file_dir=settings["temp_dir"]) -> None:
  """
  iterates over files in `temp`, creating a dictionary for each one (i.e. one `dict` per `<div>` in source file) with the following structure:
    `{`
        `"@facs": <p_children>`
     `}`
  and saves each dictionary out into `.json`
  """

  for filename in os.listdir(temp_file_dir):

    f = os.path.join(temp_file_dir, filename)
    if os.path.isfile(f) and f.endswith('.xml'):

      with open(f, "r") as file:
        div_dict = {}
        
        div = file.read()

        root = etree.fromstring(div)

        for p in root.findall('ns:p', namespaces=settings["namespace"]):
          facs = p.get('facs')
          children = p.xpath('./*')
          div_dict[facs] = [etree.tostring(i).decode('utf-8') for i in children]

        with open(f"{f}.json", "w") as dictfile:
          json.dump(div_dict, dictfile, indent=4)
          logging.debug(f"Created temporary JSON file at {f}.json")