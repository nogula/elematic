# elematic
This software offers utilities to manage materials information using the [MatML v3.1 schema](https://www.oasis-open.org/committees/documents.php?wg_abbrev=materials). An API is provided to inspect and edit materials information within other Python scripts (e.g., to read property data for a material used in an analysis) as well as a graphical user interface to visually inspect and edit MatML files.

## Quickstart
This package comprises four utilities:

1. `.api.MatML_api`: forms the basic classes and data structure for interacting with MatML data.
1. `.api.importers`: provides means to import MatML data from XML and other files.
1. `api.exporters`: (not yet implemented) provides means to export MatML data to other handy formats for use in other programs.
1. `.gui`: (not yet implemented) provides a means of visually inspecting and editing MatML data.

### Installation

1. This software uses Python. It's built with 3.11, but you can probably use other 3.X versions at your own risk.
1. Install with pip: `pip install elematic@git+https://github.com/nogula/elematic`

### Example
This example will use the example MatML file located here: [INCONEL 718 - ASTM F3055 CLASS D](<elematic/res/example_matml/INCONEL 718 - ASTM F3055 CLASS D.xml>).

> [!IMPORTANT]
> This examples assumes you have working knowledge of the [MatML 3.1](<elematic\res\matml31.xsd>) schema, including the basic structure of how materials information is represented. A detailed explanation/tutorial of the schema is forthcoming, so hang tight.

#### Load MatML file
```python
from elematic.api import importers

library = importers.import_xml("INCONEL 718 - ASTM F3055 CLASS D.xml")
```

#### List available materials
```python
print(library.get_Material())
```
```
[<elematic.api.MatML_api.Material object at 0x000002771B178250>]
```
Based on this, we know the library only contains one material (since a list of length one is returned). We can 
```python
material = library.get_Material()[0]
print(material.BulkDetails.get_Name().valueOf_)
```
```
INCONEL 718 PER ASTM F3055 CLASS D
```
This seems to match what we would expect, given the name of the file.

#### View available property data
```python
print(len(material.BulkDetails.get_PropertyData()))
```
```
4
```
Apparently, there are four property data entries for this material card. To see what they are, we need to also access the PropertyDetails entries, as well.

```python
metadata = library.get_Metadata()
for property_data in material.BulkDetails.get_PropertyData():
    property = property_data.get_property()
    print(property)
    print(metadata.get_PropertyDetails(id=property).get_Name().valueOf_)
```
```
pr_1
TENSILE ULTIMATE STRENGTH
pr_2
TENSILE YIELD STRENGTH
pr_3
TENSILE YIELD STRENGTH
pr_4
MODULUS OF ELASTICITY
```
This loop prints the `property` attribute of each of the `PropertyData` elements, then searches the library's metadata for the corresponding `PropertyDetails` and prints its name.

#### Access property data values
```python
property = "pr_1"
property_data = material.BulkDetails.get_PropertyData(property=property)[0]
print(property_data.get_Data().valueOf_)
```
```
"192000,153000"
```
Basically, what's happening here is that we are getting the property `pr_` from the material card. This returns a list of properties since there could be multiple PropertyData with the same property. In this case there is only one, so we access it with the zero index. We then get the Data element and its `valueOf_` attribute. This returns a string of the value(s). (Note: there is an open Issue (#4) to create a utility to "process" this string into its appropriate format.)

Two questions emerge; what are the units of this property, and what parameter is it dependent on?
```python
print("Property units:",metadata.get_PropertyDetails(id=property).get_Units().get_description())
parameter = property_data.get_ParameterValue()[0].get_parameter()
print("Parameter id:",parameter)
print("Parameter name:",metadata.get_ParameterDetails(id=parameter).get_Name().valueOf_)
print("Parameter values:",property_data.get_ParameterValue()[0].get_Data().valueOf_)
print("Parameter units:",metadata.get_ParameterDetails(id=parameter).get_Units().get_description())
```
```
Property units: psi
Parameter id: pa_1
Parameter name: TEMPERATURE
Parameter values: 70,1200
Parameter units: DEGREES FAHRENHEIT
```
Mystery solved! Tensile ultimate strength is in psi, and has two data points, associated with room temperature and 1200 °F.

### Tips and Tricks
Until the gui becomes available, one should become familiar with the MatML 3.1 schema, and then consider the following:
- Every element in the schema is represented by a class. The relationships between each XML element are maintained.
  - E.g., every Material has exactly one BulkDetails child element. So it can be accessed by the `get_BulkDetails()` method.
    - Also, for those elements which contain precisely one child element of a given type, it can also be accessed like an attribute, e.g., `.BulkDetails`.
  - The parent element can be accessed via the attribute `.parent_object_`.
- If the element has a text node, it can be accessed via the `.valueOf_` attribute. E.g., `.get_Data().valueOf_`.
  - The (XML) attributes of an element can also be accessed by `get_...()` methods, or as (Python) attributes. E.g., the `id` of material is obtainable via both `.get_id()` or just `.id`.

## Credits

### Acknowledgement

The initial API was created by conversion of the MatML 3.1 schema to a Python data structure via [generateDS](http://www.davekuhlman.org/generateDS.htm) by Dave Kuhlman.

### Contributors
See: [Contributors](https://github.com/nogula/elematic/graphs/contributors)

## Contributing

## See also
- [MatEditor](https://docs.welsim.com/mateditor/mateditor_overview/): a free material editor software program for engineers.
- [BT-MatML-Editor](https://github.com/P-McG/BT-MatML-Editor): a text editor for the MatML 3.1 XML Schema.