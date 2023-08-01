from utils.settings import settings
#from utils.cleanup import xmlCleaner, dirCleaner
from getfile import fileName, getFile
from xmlparser import getRoot, divList, metadata

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

if __name__ == '__main__':
    main()