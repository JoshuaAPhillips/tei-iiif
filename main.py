from utils.settings import settings
#from utils.cleanup import xmlCleaner, dirCleaner
from getfile import fileName, getFile
from xmlparser import getRoot, divList, metadata
from tempfilegen import tempFileGen

def main():
    """
    Does the thing
    """
    settings()
    filename = fileName()
    r = getFile(filename)
    root = getRoot(r)
    div_list = divList(root)
    metadata(root)
    tempFileGen(div_list)

if __name__ == '__main__':
    main()