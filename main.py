from utils.settings import settings
from utils.cleanup import xmlCleaner, dirCleaner
from getfile import fileName, getFile

def main():
    """
    Does the thing
    """
    settings()
    filename = fileName()
    r = getFile(filename)

if __name__ == '__main__':
    main()