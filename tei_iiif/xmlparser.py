from lxml import etree
import logging
from .getfile import fileName, getFile
from .utils.settings import settings

settings = settings()
filename = fileName()
r = getFile(filename)

def getRoot(r) -> object:
  """
  Uses lxml to return `root` object of XML file
  """
  if filename.startswith("http"):
    try:
      root = etree.fromstring(r.content)
      logging.debug("Parsing XML from remote source")
      return root
    
    except etree.XMLSyntaxError as e:
      logging.error(str(e) + f" : unable to parse XML", exc_info=True)

  else:
    try:
      root = etree.parse(r)
      logging.debug("Parsing XML from local source")
      return root
    
    except etree.XMLSyntaxError as e:
      logging.error(str(e) + f" : unable to parse XML", exc_info=True)

def divList(root) -> list:

  """
  Uses lxml to parse `root` and return master list of <div>s for later use
  """

  div_list = []
  divs = root.findall('.//ns:div', namespaces=settings["namespace"])

  try:
    for div in divs:
      div_list.append(div)
      
  except AttributeError as e:
    logging.error(e, exc_info=True)

  logging.debug('Created master list of <div>s for iteration in further functions')
  return div_list

def metadata(root) -> dict:
  """
  Returns dictionary of metadata for later use. This is a minimal dictionary that provides data necessary for the module's basic functionality, and can be expanded as needed.
  """
  metadata = {
    "title": root.find('.//ns:title', namespaces=settings["namespace"]).text,
    "idno": root.find('.//ns:idno', namespaces=settings["namespace"]).text,
    "author": root.find('.//ns:author', namespaces=settings["namespace"]).text
  }

  logging.debug('Created metadata dictionary for later use')
  
  return metadata