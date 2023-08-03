from utils.settings import settings
from getfile import fileName, getFile
from xmlparser import getRoot, divList, metadata
from tempfilegen import tempFileGen
from divjson import divJson

settings = settings()
temp_dir = settings["temp_dir"]

def main():
    """
    Does the thing
    """
    filename = fileName()
    r = getFile(filename)
    root = getRoot(r)
    div_list = divList(root)
    metadata(root)
    tempFileGen(div_list)
    divJson(temp_dir)
    #don't actually need to clean up xml, just implement a .endswith(".json") in the next step...

if __name__ == '__main__':
    main()