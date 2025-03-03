"""This module provides utility functions for importing and exporting MatML documents
in XML and JSON formats.
"""

import os

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from elematic.ds import MatMLDoc


def import_xml(xml: str, **kwargs) -> MatMLDoc:
    """Imports a MatML document from an XML file or string.

    Args:
        xml: The XML file path or XML string.
        **kwargs: Additional keyword arguments for ParserConfig.
    """
    config = ParserConfig(**kwargs)
    context = XmlContext()
    parser = XmlParser(context=context, config=config)
    if os.path.isfile(xml):
        matml_doc = parser.parse(xml, MatMLDoc)
    else:
        matml_doc = parser.from_string(xml, MatMLDoc)
    return matml_doc


def export_xml(matml_doc: MatMLDoc, outfile: str | None = None, **kwargs) -> None | str:
    """Renders a MatML document object to an XML file or a string.

    Args:
        matml_doc: The MatML document object to render.
        outfile: The output file path. If None, the XML string is returned.
        **kwargs: Additional keyword arguments for SerializerConfig.
    """
    config = SerializerConfig(**kwargs)
    context = XmlContext()
    xml_serializer = XmlSerializer(config=config, context=context)
    if outfile is not None:
        with open(outfile, "w", encoding="utf-8") as f:
            xml_serializer.write(f, matml_doc)
    else:
        return xml_serializer.render(matml_doc)


def import_json(json: str, **kwargs) -> MatMLDoc:
    """Imports a MatML document from a JSON file or string.

    Args:
        json: The JSON file path or JSON string.
        **kwargs: Additional keyword arguments for ParserConfig.
    """
    config = ParserConfig(**kwargs)
    context = XmlContext()
    parser = JsonParser(context=context, config=config)
    if os.path.isfile(json):
        matml_doc = parser.parse(json, MatMLDoc)
    else:
        matml_doc = parser.from_string(json, MatMLDoc)
    return matml_doc


def export_json(
    matml_doc: MatMLDoc, outfile: str | None = None, **kwargs
) -> None | str:
    """Renders a MatML document object to a JSON file or a string.

    Args:
        matml_doc: The MatML document object to render.
        outfile: The output file path. If None, the JSON string is returned.
        **kwargs: Additional keyword arguments for SerializerConfig.
    """
    config = SerializerConfig(**kwargs)
    context = XmlContext()
    json_serializer = JsonSerializer(config=config, context=context)
    if outfile is not None:
        with open(outfile, "w", encoding="utf-8") as f:
            json_serializer.write(f, matml_doc)
    else:
        return json_serializer.render(matml_doc)
