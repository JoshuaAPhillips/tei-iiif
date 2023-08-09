import logging
from .utils.settings import settings
from .utils.cleanup import dirCleaner
from .getfile import fileName, getFile
from .xmlparser import getRoot, divList, metadata
from .tempfilegen import tempFileGen
from .divjson import divJson
from .manifestgen import manifestGen, jsonSave

settings = settings()
temp_dir = settings["temp_dir"]
logging_level = settings["logging"]["level"]
log_file = settings["logging"]["file"]

logging.basicConfig(
    level=logging_level, 
    format='%(asctime)s - %(levelname)s -%(name)s - %(message)s', 
    filename=log_file, 
    filemode="w", 
    force=True
    )

def main():
    """
    Does the thing
    """
    filename = fileName()
    r = getFile(filename)
    root = getRoot(r)
    div_list = divList(root)
    metadata_dict = metadata(root)
    tempFileGen(div_list)
    divJson(temp_dir)
    manifest_list = manifestGen(metadata_dict["idno"], settings["temp_dir"], settings["manifest_store"])
    jsonSave(manifest_list, metadata_dict["idno"])
    dirCleaner(temp_dir)
    logging.info("Done!")


if __name__ == '__main__':
    main()