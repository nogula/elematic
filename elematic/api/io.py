import sys
from . import MatML_api


def import_xml(inputFile):
    """Reads MatML information from an XML file. Currently does not validate the file.

    Args:
        inputFile (str): filename location of XML data.

    Returns:
        elematic.api.MatML_api.MatML_doc: the root element of the MatML data
    """
    doc = MatML_api.parsexml_(inputFile)
    rootNode = doc.getroot()
    rootObject = MatML_api.MatML_Doc.factory()
    rootObject.build(rootNode)
    doc = None
    return rootObject

def import_granta():
    raise NotImplementedError

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