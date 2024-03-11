import sys

from . import MatML_api as mapi

def import_xml(inputFile):
    doc = mapi.parsexml_(inputFile)
    rootNode = doc.getroot()
    rootObject = mapi.MatML_Doc.factory()
    rootObject.build(rootNode)
    doc = None
    print(rootObject)
    return rootObject

def import_granta():
    pass

def main():
    args = sys.argv[1:]
    inputFile = args[0]
    if inputFile.endswith(".xml"):
        import_xml(inputFile)
    else:
        fileType = inputFile.split(".")[-1]
        print(f"Importer not implemented for files of type {fileType}")

if __name__ == '__main__':
    main()