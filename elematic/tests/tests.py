from elematic.api import importers
from elematic.api import MatML_api as mapi

inputFile = r"elematic\res\test.xml"
doc = importers.import_xml(inputFile)

material = doc.get_Material(id="M1001")
print(material.BulkDetails.get_PropertyData(property="pr1")[0])