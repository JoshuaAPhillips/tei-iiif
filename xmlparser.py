from lxml import etree
import logging
from getfile import fileName, getFile
from utils.settings import settings

settings = settings()
filename = fileName()
r = getFile(filename)

def getRoot(r) -> object:
  """
  Returns root object of XML file
  """
  if filename.startswith("http"):
    try:
      root = etree.fromstring(r.content)
      logging.info("Parsing XML from remote source")
      return root
    
    except etree.XMLSyntaxError as e:
      logging.error(e)

  else:
    try:
      root = etree.parse(r)
      logging.info("Parsing XML from local source")
      return root
    
    except etree.XMLSyntaxError as e:
      logging.error(e)

def divList(root) -> list:

  """
  returns master list of <div>s for later use
  """

  div_list = []
  divs = root.findall('.//tei:div', namespaces=settings["namespace"])

  try:
    for div in divs:
      div_list.append(div)
  except AttributeError as e:
    logging.error(e)

  return div_list

def metadata(root) -> dict:
  """
  Returns dictionary of metadata for later use. This is a minimal dictionary that provides data necessary for the module's basic functionality, and can be expanded as needed.
  """
  metadata = {
    "title": root.find('.//tei:title', namespaces=settings["namespace"]).text,
    "idno": root.find('.//tei:idno', namespaces=settings["namespace"]).text,
    "author": root.find('.//tei:author', namespaces=settings["namespace"]).text
  }
  
  return metadata