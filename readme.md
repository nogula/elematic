<h1 align='center'> elematic </h1>

Materials information management utilities in Python using the MatML schema from NIST.

## Features

- Convert MatML XML files to Python data structures.
- Inspect and edit materials information.
- Use materials information in other Python projects.

## Documentation

[Documentation](https://github.com/nogula/elematic/wiki) is available, but still in work.
## Installation

Install elematic with pip.

```bash
pip install elematic@git+https://github.com/nogula/elematic@main
```
## Usage

This package comprises four utilities:

1. `elematic.api.MatML_api`: forms the basic classes and data structure for interacting with MatML data.
1. `elematic.api.io`: provides means to import and export MatML data from XML and other files.
1. `elematic.api.utilities`: provides helper functions to streamline the interaction of materials information.
1. `elematic.gui`: (not yet implemented) provides a means of visually inspecting and editing MatML data.

See the [Wiki tutorial](https://github.com/nogula/elematic/wiki/Tutorial) for more help.

## Credits & Acknowledgements
- This project is based entirely on the MatML schema, originally developed by NIST. Thank you, NIST.
- The initial API was created by conversion of the MatML 3.1 schema to a Python data structure via [generateDS](http://www.davekuhlman.org/generateDS.htm) by Dave Kuhlman. Thank you, Dave.

## See Also
- [MatEditor](https://docs.welsim.com/mateditor/mateditor_overview/): a free material editor software program for engineers.
- [BT-MatML-Editor](https://github.com/P-McG/BT-MatML-Editor): a text editor for the MatML 3.1 XML Schema.
- [matml](https://www.mathworks.com/matlabcentral/fileexchange/19686-matml): converts between MATLAB and MatML data.

## License
Copyright is released under the [MIT](https://raw.githubusercontent.com/nogula/elematic/main/LICENSE) license.