<h1><center>elematic</center></h1>

*Materials information management utilities in Python.*

## About elematic
elematic provides a data structure based on the MatML (Materials Markup Language) schema developed by NIST in the early 2000's. The following features are available:

- Convert MatML XML files to Python data structures (a JSON binding is also available via xsData).
- Inspect and edit materials information.
- Use materials information in other Python projects.

## Documentation
Documentation is available, but still a work in progress: [https://noahgula.com/elematic](https://noahgula.com/elematic).

## Installation
Use PyPI:
```sh
pip install elematic
```

## Usage
There are two main modules: `util` (import and export utilities) and `ds` (data structure). See [documentation](https://noahgula.com/elematic) for more information.

## Credits & Acknowledgements
- This project utilizes the MatML schema as the data structure architecture, originally developed by NIST.
- The initial API was created by conversion of the MatML 3.1 schema to a Python data structure via [xsData](https://xsdata.readthedocs.io/en/latest/).

## See Also
- [MatEditor](https://docs.welsim.com/mateditor/mateditor_overview/): a free material editor software program for engineers.
- [BT-MatML-Editor](https://github.com/P-McG/BT-MatML-Editor): a text editor for the MatML 3.1 XML Schema.
- [matml](https://www.mathworks.com/matlabcentral/fileexchange/19686-matml): converts between MATLAB and MatML data.
