#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Mar  7 19:29:19 2024 by generateDS.py version 2.43.3.
# Python 3.11.8 (tags/v3.11.8:db85d51, Feb  6 2024, 22:03:32) [MSC v.1937 64 bit (AMD64)]
#
# Command line options:
#   ('-o', 'MatML_api.py')
#   ('-s', 'MatML_api_subs.py')
#   ('-m', '')
#   ('--super', 'MatML_api')
#
# Command line arguments:
#   ../matml31.xsd
#
# Command line:
#   generateDS.py -o "MatML_api.py" -s "MatML_api_subs.py" -m --super="MatML_api" ../matml31.xsd
#
# Current working directory (os.getcwd()):
#   api_generator
#
from __future__ import annotations

from msilib.schema import Property
import sys

try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
from six.moves import zip_longest
import os
import re as re_
import base64
import datetime as datetime_
import decimal as decimal_
from lxml import etree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = ""
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc


def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element


#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ModulenotfoundExp_:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import (
        GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_,
    )
except ModulenotfoundExp_:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:

        class GeneratedsSuperSuper(object):
            pass

    class GeneratedsSuper(GeneratedsSuperSuper):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r"(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$")

        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name

            def utcoffset(self, dt):
                return self.__offset

            def tzname(self, dt):
                return self.__name

            def dst(self, dt):
                return None

        def __str__(self):
            settings = {
                "str_pretty_print": True,
                "str_indent_level": 0,
                "str_namespaceprefix": "",
                "str_name": self.__class__.__name__,
                "str_namespacedefs": "",
            }
            for n in settings:
                if hasattr(self, n):
                    settings[n] = getattr(self, n)
            if sys.version_info.major == 2:
                from StringIO import StringIO
            else:
                from io import StringIO
            output = StringIO()
            self.export(
                output,
                settings["str_indent_level"],
                pretty_print=settings["str_pretty_print"],
                namespaceprefix_=settings["str_namespaceprefix"],
                name_=settings["str_name"],
                namespacedef_=settings["str_namespacedefs"],
            )
            strval = output.getvalue()
            output.close()
            return strval

        def gds_format_string(self, input_data, input_name=""):
            return input_data

        def gds_parse_string(self, input_data, node=None, input_name=""):
            return input_data

        def gds_validate_string(self, input_data, node=None, input_name=""):
            if not input_data:
                return ""
            else:
                return input_data

        def gds_format_base64(self, input_data, input_name=""):
            return base64.b64encode(input_data).decode("ascii")

        def gds_validate_base64(self, input_data, node=None, input_name=""):
            return input_data

        def gds_format_integer(self, input_data, input_name=""):
            return "%d" % int(input_data)

        def gds_parse_integer(self, input_data, node=None, input_name=""):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, "Requires integer value: %s" % exp)
            return ival

        def gds_validate_integer(self, input_data, node=None, input_name=""):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires integer value")
            return value

        def gds_format_integer_list(self, input_data, input_name=""):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return "%s" % " ".join(input_data)

        def gds_validate_integer_list(self, input_data, node=None, input_name=""):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, "Requires sequence of integer values")
            return values

        def gds_format_float(self, input_data, input_name=""):
            value = ("%.15f" % float(input_data)).rstrip("0")
            if value.endswith("."):
                value += "0"
            return value

        def gds_parse_float(self, input_data, node=None, input_name=""):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, "Requires float or double value: %s" % exp)
            return fval_

        def gds_validate_float(self, input_data, node=None, input_name=""):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires float value")
            return value

        def gds_format_float_list(self, input_data, input_name=""):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return "%s" % " ".join(input_data)

        def gds_validate_float_list(self, input_data, node=None, input_name=""):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, "Requires sequence of float values")
            return values

        def gds_format_decimal(self, input_data, input_name=""):
            return_value = "%s" % input_data
            if "." in return_value:
                return_value = return_value.rstrip("0")
                if return_value.endswith("."):
                    return_value = return_value.rstrip(".")
            return return_value

        def gds_parse_decimal(self, input_data, node=None, input_name=""):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires decimal value")
            return decimal_value

        def gds_validate_decimal(self, input_data, node=None, input_name=""):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires decimal value")
            return value

        def gds_format_decimal_list(self, input_data, input_name=""):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return " ".join([self.gds_format_decimal(item) for item in input_data])

        def gds_validate_decimal_list(self, input_data, node=None, input_name=""):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, "Requires sequence of decimal values")
            return values

        def gds_format_double(self, input_data, input_name=""):
            return "%s" % input_data

        def gds_parse_double(self, input_data, node=None, input_name=""):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, "Requires double or float value: %s" % exp)
            return fval_

        def gds_validate_double(self, input_data, node=None, input_name=""):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, "Requires double or float value")
            return value

        def gds_format_double_list(self, input_data, input_name=""):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return "%s" % " ".join(input_data)

        def gds_validate_double_list(self, input_data, node=None, input_name=""):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, "Requires sequence of double or float values"
                    )
            return values

        def gds_format_boolean(self, input_data, input_name=""):
            return ("%s" % input_data).lower()

        def gds_parse_boolean(self, input_data, node=None, input_name=""):
            input_data = input_data.strip()
            if input_data in ("true", "1"):
                bval = True
            elif input_data in ("false", "0"):
                bval = False
            else:
                raise_parse_error(node, "Requires boolean value")
            return bval

        def gds_validate_boolean(self, input_data, node=None, input_name=""):
            if input_data not in (
                True,
                1,
                False,
                0,
            ):
                raise_parse_error(
                    node, "Requires boolean value " "(one of True, 1, False, 0)"
                )
            return input_data

        def gds_format_boolean_list(self, input_data, input_name=""):
            if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
                input_data = [str(s) for s in input_data]
            return "%s" % " ".join(input_data)

        def gds_validate_boolean_list(self, input_data, node=None, input_name=""):
            values = input_data.split()
            for value in values:
                value = self.gds_parse_boolean(value, node, input_name)
                if value not in (
                    True,
                    1,
                    False,
                    0,
                ):
                    raise_parse_error(
                        node,
                        "Requires sequence of boolean values "
                        "(one of True, 1, False, 0)",
                    )
            return values

        def gds_validate_datetime(self, input_data, node=None, input_name=""):
            return input_data

        def gds_format_datetime(self, input_data, input_name=""):
            if input_data.microsecond == 0:
                _svalue = "%04d-%02d-%02dT%02d:%02d:%02d" % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = "%04d-%02d-%02dT%02d:%02d:%02d.%s" % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ("%f" % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += "Z"
                    else:
                        if total_seconds < 0:
                            _svalue += "-"
                            total_seconds *= -1
                        else:
                            _svalue += "+"
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += "{0:02d}:{1:02d}".format(hours, minutes)
            return _svalue

        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == "Z":
                tz = GeneratedsSuper._FixedOffsetTZ(0, "UTC")
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(":")
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == "-":
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split(".")
            if len(time_parts) > 1:
                micro_seconds = int(float("0." + time_parts[1]) * 1000000)
                input_data = "%s.%s" % (
                    time_parts[0],
                    "{}".format(micro_seconds).rjust(6, "0"),
                )
                dt = datetime_.datetime.strptime(input_data, "%Y-%m-%dT%H:%M:%S.%f")
            else:
                dt = datetime_.datetime.strptime(input_data, "%Y-%m-%dT%H:%M:%S")
            dt = dt.replace(tzinfo=tz)
            return dt

        def gds_validate_date(self, input_data, node=None, input_name=""):
            return input_data

        def gds_format_date(self, input_data, input_name=""):
            _svalue = "%04d-%02d-%02d" % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += "Z"
                        else:
                            if total_seconds < 0:
                                _svalue += "-"
                                total_seconds *= -1
                            else:
                                _svalue += "+"
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += "{0:02d}:{1:02d}".format(hours, minutes)
            except AttributeError:
                pass
            return _svalue

        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == "Z":
                tz = GeneratedsSuper._FixedOffsetTZ(0, "UTC")
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(":")
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == "-":
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, "%Y-%m-%d")
            dt = dt.replace(tzinfo=tz)
            return dt.date()

        def gds_validate_time(self, input_data, node=None, input_name=""):
            return input_data

        def gds_format_time(self, input_data, input_name=""):
            if input_data.microsecond == 0:
                _svalue = "%02d:%02d:%02d" % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = "%02d:%02d:%02d.%s" % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ("%f" % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += "Z"
                    else:
                        if total_seconds < 0:
                            _svalue += "-"
                            total_seconds *= -1
                        else:
                            _svalue += "+"
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += "{0:02d}:{1:02d}".format(hours, minutes)
            return _svalue

        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            target = str(target)
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1

        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == "Z":
                tz = GeneratedsSuper._FixedOffsetTZ(0, "UTC")
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(":")
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == "-":
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split(".")) > 1:
                dt = datetime_.datetime.strptime(input_data, "%H:%M:%S.%f")
            else:
                dt = datetime_.datetime.strptime(input_data, "%H:%M:%S")
            dt = dt.replace(tzinfo=tz)
            return dt.time()

        def gds_check_cardinality_(
            self, value, input_name, min_occurs=0, max_occurs=1, required=None
        ):
            if value is None:
                length = 0
            elif isinstance(value, list):
                length = len(value)
            else:
                length = 1
            if required is not None:
                if required and length < 1:
                    self.gds_collector_.add_message(
                        "Required value {}{} is missing".format(
                            input_name, self.gds_get_node_lineno_()
                        )
                    )
            if length < min_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is below "
                    "the minimum allowed, "
                    "expected at least {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(), min_occurs, length
                    )
                )
            elif length > max_occurs:
                self.gds_collector_.add_message(
                    "Number of values for {}{} is above "
                    "the maximum allowed, "
                    "expected at most {}, found {}".format(
                        input_name, self.gds_get_node_lineno_(), max_occurs, length
                    )
                )

        def gds_validate_builtin_ST_(
            self,
            validator,
            value,
            input_name,
            min_occurs=None,
            max_occurs=None,
            required=None,
        ):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))

        def gds_validate_defined_ST_(
            self,
            validator,
            value,
            input_name,
            min_occurs=None,
            max_occurs=None,
            required=None,
        ):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))

        def gds_str_lower(self, instring):
            return instring.lower()

        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = "/".join(path_list)
            return path

        Tag_strip_pattern_ = re_.compile(r"\{.*\}")

        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub("", node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)

        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if "xsi" in node.nsmap:
                classname = node.get("{%s}type" % node.nsmap["xsi"])
                if classname is not None:
                    names = classname.split(":")
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1

        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content

        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in mapping.items()))

        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = "utf-8"
                return instring.encode(encoding)
            else:
                return instring

        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, unicode):
                result = quote_xml(instring).encode("utf8")
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result

        def __eq__(self, other):
            def excl_select_objs_(obj):
                return obj[0] != "parent_object_" and obj[0] != "gds_collector_"

            if type(self) != type(other):
                return False
            return all(
                x == y
                for x, y in zip_longest(
                    filter(excl_select_objs_, self.__dict__.items()),
                    filter(excl_select_objs_, other.__dict__.items()),
                )
            )

        def __ne__(self, other):
            return not self.__eq__(other)

        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass

        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass

        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None

        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass

        def gds_get_node_lineno_(self):
            if (
                hasattr(self, "gds_elementtree_node_")
                and self.gds_elementtree_node_ is not None
            ):
                return " near line {}".format(self.gds_elementtree_node_.sourceline)
            else:
                return ""

    def getSubclassFromModule_(module, class_):
        """Get the subclass of a class from a specific module."""
        name = class_.__name__ + "Sub"
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# Globals
#

ExternalEncoding = ""
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r"({.*})?(.*)")
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r"{(.*)}(.*)")
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write("    ")


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ""
    s1 = isinstance(inStr, BaseStrType_) and inStr or "%s" % inStr
    s2 = ""
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos : mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start() : mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace("&", "&amp;")
    s1 = s1.replace("<", "&lt;")
    s1 = s1.replace(">", "&gt;")
    return s1


def quote_attrib(inStr):
    s1 = isinstance(inStr, BaseStrType_) and inStr or "%s" % inStr
    s1 = s1.replace("&", "&amp;")
    s1 = s1.replace("<", "&lt;")
    s1 = s1.replace(">", "&gt;")
    s1 = s1.replace("\n", "&#10;")
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find("\n") == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find("\n") == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ""
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(":")
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == "xml":
            namespace = "http://www.w3.org/XML/1998/namespace"
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get(
                "{%s}%s"
                % (
                    namespace,
                    name,
                )
            )
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = "%s (element %s/line %d)" % (
            msg,
            node.tag,
            node.sourceline,
        )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8

    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value

    def getCategory(self):
        return self.category

    def getContenttype(self, content_type):
        return self.content_type

    def getValue(self):
        return self.value

    def getName(self):
        return self.name

    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:  # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name, pretty_print=pretty_print
            )

    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write("<%s>%s</%s>" % (self.name, self.value, self.name))
        elif (
            self.content_type == MixedContainer.TypeInteger
            or self.content_type == MixedContainer.TypeBoolean
        ):
            outfile.write("<%s>%d</%s>" % (self.name, self.value, self.name))
        elif (
            self.content_type == MixedContainer.TypeFloat
            or self.content_type == MixedContainer.TypeDecimal
        ):
            outfile.write("<%s>%f</%s>" % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write("<%s>%g</%s>" % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write(
                "<%s>%s</%s>" % (self.name, base64.b64encode(self.value), self.name)
            )

    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(element, "%s" % self.name)
            subelement.text = self.to_etree_simple()
        else:  # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)

    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (
            self.content_type == MixedContainer.TypeInteger
            or self.content_type == MixedContainer.TypeBoolean
        ):
            text = "%d" % self.value
        elif (
            self.content_type == MixedContainer.TypeFloat
            or self.content_type == MixedContainer.TypeDecimal
        ):
            text = "%f" % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = "%g" % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = "%s" % base64.b64encode(self.value)
        return text

    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value)
            )
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value)
            )
        else:  # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n'
                % (
                    self.category,
                    self.content_type,
                    self.name,
                )
            )
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(")\n")


class MemberSpec_(object):
    def __init__(
        self,
        name="",
        data_type="",
        container=0,
        optional=0,
        child_attrs=None,
        choice=None,
    ):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_data_type(self, data_type):
        self.data_type = data_type

    def get_data_type_chain(self):
        return self.data_type

    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return "xs:string"
        else:
            return self.data_type

    def set_container(self, container):
        self.container = container

    def get_container(self):
        return self.container

    def set_child_attrs(self, child_attrs):
        self.child_attrs = child_attrs

    def get_child_attrs(self):
        return self.child_attrs

    def set_choice(self, choice):
        self.choice = choice

    def get_choice(self):
        return self.choice

    def set_optional(self, optional):
        self.optional = optional

    def get_optional(self):
        return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


class ChemicalElementSymbol(str, Enum):
    """
    This datatype enumerates the valid strings representing chemical elements, which may be used in the `Symbol` element.
    """

    H = "H"  # Hydrogen
    HE = "He"  # Helium
    LI = "Li"  # Lithium
    BE = "Be"  # Beryllium
    B = "B"  # Boron
    C = "C"  # Carbon
    N = "N"  # Nitrogen
    O = "O"  # Oxygen
    F = "F"  # Fluorine
    NE = "Ne"  # Neon
    NA = "Na"  # Sodium
    MG = "Mg"  # Magnesium
    AL = "Al"  # Aluminium
    SI = "Si"  # Silicon
    P = "P"  # Phosphorus
    S = "S"  # Sulfur
    CL = "Cl"  # Chlorine
    AR = "Ar"  # Argon
    K = "K"  # Potassium
    CA = "Ca"  # Calcium
    SC = "Sc"  # Scandium
    TI = "Ti"  # Titanium
    V = "V"  # Vanadium
    CR = "Cr"  # Chromium
    MN = "Mn"  # Manganese
    FE = "Fe"  # Iron
    CO = "Co"  # Cobalt
    NI = "Ni"  # Nickel
    CU = "Cu"  # Copper
    ZN = "Zn"  # Zinc
    GA = "Ga"  # Gallium
    GE = "Ge"  # Germanium
    AS = "As"  # Arsenic
    SE = "Se"  # Selenium
    BR = "Br"  # Bromine
    KR = "Kr"  # Krypton
    RB = "Rb"  # Rubidium
    SR = "Sr"  # Strontium
    Y = "Y"  # Yttrium
    ZR = "Zr"  # Zirconium
    NB = "Nb"  # Niobium
    MO = "Mo"  # Molybdenum
    TC = "Tc"  # Technetium
    RU = "Ru"  # Ruthenium
    RH = "Rh"  # Rhodium
    PD = "Pd"  # Palladium
    AG = "Ag"  # Silver
    CD = "Cd"  # Cadmium
    IN = "In"  # Indium
    SN = "Sn"  # Tin
    SB = "Sb"  # Antimony
    TE = "Te"  # Tellurium
    I = "I"  # Iodine
    XE = "Xe"  # Xenon
    CS = "Cs"  # Caesium
    BA = "Ba"  # Barium
    LA = "La"  # Lanthanum
    CE = "Ce"  # Cerium
    PR = "Pr"  # Praseodymium
    ND = "Nd"  # Neodymium
    PM = "Pm"  # Promethium
    SM = "Sm"  # Samarium
    EU = "Eu"  # Europium
    GD = "Gd"  # Gadolinium
    TB = "Tb"  # Terbium
    DY = "Dy"  # Dysprosium
    HO = "Ho"  # Holmium
    ER = "Er"  # Erbium
    TM = "Tm"  # Thulium
    YB = "Yb"  # Ytterbium
    LU = "Lu"  # Lutetium
    HF = "Hf"  # Hafnium
    TA = "Ta"  # Tantalum
    W = "W"  # Tungsten
    RE = "Re"  # Rhenium
    OS = "Os"  # Osmium
    IR = "Ir"  # Iridium
    PT = "Pt"  # Platinum
    AU = "Au"  # Gold
    HG = "Hg"  # Mercury
    TL = "Tl"  # Thallium
    PB = "Pb"  # Lead
    BI = "Bi"  # Bismuth
    PO = "Po"  # Polonium
    AT = "At"  # Astatine
    RN = "Rn"  # Radon
    FR = "Fr"  # Francium
    RA = "Ra"  # Radium
    AC = "Ac"  # Actinium
    TH = "Th"  # Thorium
    PA = "Pa"  # Protactinium
    U = "U"  # Uranium
    NP = "Np"  # Neptunium
    PU = "Pu"  # Plutonium
    AM = "Am"  # Americium
    CM = "Cm"  # Curium
    BK = "Bk"  # Berkelium
    CF = "Cf"  # Californium
    ES = "Es"  # Einsteinium
    FM = "Fm"  # Fermium
    MD = "Md"  # Mendelevium
    NO = "No"  # Nobelium
    LR = "Lr"  # Lawrencium
    RF = "Rf"  # Rutherfordium
    DB = "Db"  # Dubnium
    SG = "Sg"  # Seaborgium
    BH = "Bh"  # Bohrium
    HS = "Hs"  # Hassium
    MT = "Mt"  # Meitnerium
    UUN = "Uun"  # Ununnilium
    UUU = "Uuu"  # Unununium
    UUB = "Uub"  # Ununbium
    UUQ = "Uuq"  # Ununquadium
    UUH = "Uuh"  # Ununhexium
    UUO = "Uuo"  # Ununoctium


class CurrencyCode(str, Enum):
    """ISO4217_CurrencyCode

    Based on ISO-4217, and taken from paper N699 on http://www.jtc1sc32.org/ As of 2003-12-11 permission to use this element has been sought from, but not yet been granted by, the authors of the paper. This element declares the content model for `CurrencyCode`, which contains a string representing a currency. For the most current updates, refer to http://www.din.de/gremien/nas/nabd/iso4217ma/codlistp1/en_listp1.html.
    """

    AFA = "AFA"  # Afghani
    ALL = "ALL"  # Lek
    AMD = "AMD"  # Armenian Dram
    ANG = "ANG"  # Netherlands Antillian Guilder
    AOA = "AOA"  # Kwanza
    ARS = "ARS"  # Argentine Peso
    ATS = "ATS"  # Schilling
    AUD = "AUD"  # Australian Dollar
    AWG = "AWG"  # Aruban Guilder
    AZM = "AZM"  # Azerbaijanian Manat
    BAM = "BAM"  # Convertible Marks
    BBD = "BBD"  # Barbados Dollar
    BDT = "BDT"  # Taka
    BEF = "BEF"  # Belgian Franc
    BGL = "BGL"  # Lev
    BGN = "BGN"  # Bulgarian Lev
    BHD = "BHD"  # Bahraini Dinar
    BIF = "BIF"  # Burundi Franc
    BMD = "BMD"  # Bermudian Dollar
    BND = "BND"  # Brunei Dollar
    BOB = "BOB"  # Boliviano
    BOV = "BOV"  # Mvdol
    BRL = "BRL"  # Brazilian Real
    BSD = "BSD"  # Bahamian Dollar
    BTN = "BTN"  # Ngultrum
    BWP = "BWP"  # Pula
    BYB = "BYB"  # Belarussian Ruble
    BYR = "BYR"  # Belarussian Ruble
    BZD = "BZD"  # Belize Dollar
    CAD = "CAD"  # Canadian Dollar
    CDF = "CDF"  # Franc Congolais
    CHF = "CHF"  # Swiss Franc
    CLF = "CLF"  # Unidades de fomento
    CLP = "CLP"  # Chilean Peso
    CNY = "CNY"  # Yuan Renminbi
    COP = "COP"  # Colombian Peso
    CRC = "CRC"  # Costa Rican Colon
    CUP = "CUP"  # Cuban Peso
    CVE = "CVE"  # Cape Verde Escudo
    CYP = "CYP"  # Cyprus Pound
    CZK = "CZK"  # Czech Koruna
    DEM = "DEM"  # Deutsche Mark
    DJF = "DJF"  # Djibouti Franc
    DKK = "DKK"  # Danish Krone
    DOP = "DOP"  # Dominican Peso
    DZD = "DZD"  # Algerian Dinar
    EEK = "EEK"  # Kroon
    EGP = "EGP"  # Egyptian Pound
    ERN = "ERN"  # Nakfa
    ESP = "ESP"  # Spanish Peseta
    ETB = "ETB"  # Ethiopian Birr
    EUR = "EUR"  # Euro
    FIM = "FIM"  # Markka
    FJD = "FJD"  # Fiji Dollar
    FKP = "FKP"  # Falkland Islands Pound
    FRF = "FRF"  # French Franc
    GBP = "GBP"  # Pound Sterling
    GEL = "GEL"  # Lari
    GHC = "GHC"  # Cedi
    GIP = "GIP"  # Gibraltar Pound
    GMD = "GMD"  # Dalasi
    GNF = "GNF"  # Guinea Franc
    GRD = "GRD"  # Drachma
    GTQ = "GTQ"  # Quetzal
    GWP = "GWP"  # Guinea-Bissau Peso
    GYD = "GYD"  # Guyana Dollar
    HKD = "HKD"  # Hong Kong Dollar
    HNL = "HNL"  # Lempira
    HRK = "HRK"  # Croatian kuna
    HTG = "HTG"  # Gourde
    HUF = "HUF"  # Forint
    IDR = "IDR"  # Rupiah
    IEP = "IEP"  # Irish Pound
    ILS = "ILS"  # New Israeli Sheqel
    INR = "INR"  # Indian Rupee
    IQD = "IQD"  # Iraqi Dinar
    IRR = "IRR"  # Iranian Rial
    ISK = "ISK"  # Iceland Krona
    ITL = "ITL"  # Italian Lira
    JMD = "JMD"  # Jamaican Dollar
    JOD = "JOD"  # Jordanian Dinar
    JPY = "JPY"  # Yen
    KES = "KES"  # Kenyan Shilling
    KGS = "KGS"  # Som
    KHR = "KHR"  # Riel
    KMF = "KMF"  # Comoro Franc
    KPW = "KPW"  # North Korean Won
    KRW = "KRW"  # Won
    KWD = "KWD"  # Kuwaiti Dinar
    KYD = "KYD"  # Cayman Islands Dollar
    KZT = "KZT"  # Tenge
    LAK = "LAK"  # Kip
    LBP = "LBP"  # Lebanese Pound
    LKR = "LKR"  # Sri Lanka Rupee
    LRD = "LRD"  # Liberian Dollar
    LSL = "LSL"  # Loti
    LTL = "LTL"  # Lithuanian Litus
    LUF = "LUF"  # Luxembourg Franc
    LVL = "LVL"  # Latvian Lats
    LYD = "LYD"  # Libyan Dinar
    MAD = "MAD"  # Moroccan Dirham
    MDL = "MDL"  # Moldovan Leu
    MGF = "MGF"  # Malagasy Franc
    MKD = "MKD"  # Denar
    MMK = "MMK"  # Kyat
    MNT = "MNT"  # Tugrik
    MOP = "MOP"  # Pataca
    MRO = "MRO"  # Ouguiya
    MTL = "MTL"  # Maltese Lira
    MUR = "MUR"  # Mauritius Rupee
    MVR = "MVR"  # Rufiyaa
    MWK = "MWK"  # Kwacha
    MXN = "MXN"  # Mexican Peso
    MXV = "MXV"  # Mexican Unidad de Inversion (UDI)
    MYR = "MYR"  # Malaysian Ringgit
    MZM = "MZM"  # Metical
    NAD = "NAD"  # Namibia Dollar
    NGN = "NGN"  # Naira
    NIO = "NIO"  # Cordoba Oro
    NLG = "NLG"  # Netherlands Guilder
    NOK = "NOK"  # Norwegian Krone
    NPR = "NPR"  # Nepalese Rupee
    NZD = "NZD"  # New Zealand Dollar
    OMR = "OMR"  # Rial Omani
    PAB = "PAB"  # Balboa
    PEN = "PEN"  # Nuevo Sol
    PGK = "PGK"  # Kina
    PHP = "PHP"  # Philippine Peso
    PKR = "PKR"  # Pakistan Rupee
    PLN = "PLN"  # Zloty
    PTE = "PTE"  # Portuguese Escudo
    PYG = "PYG"  # Guarani
    QAR = "QAR"  # Qatari Rial
    ROL = "ROL"  # Leu
    RUB = "RUB"  # Russian Ruble
    RUR = "RUR"  # Russian Ruble
    RWF = "RWF"  # Rwanda Franc
    SAR = "SAR"  # Saudi Riyal
    SBD = "SBD"  # Solomon Islands Dollar
    SCR = "SCR"  # Seychelles Rupee
    SDD = "SDD"  # Sudanese Dinar
    SEK = "SEK"  # Swedish Krona
    SGD = "SGD"  # Singapore Dollar
    SHP = "SHP"  # Saint Helena Pound
    SIT = "SIT"  # Tolar
    SKK = "SKK"  # Slovak Koruna
    SLL = "SLL"  # Leone
    SOS = "SOS"  # Somali Shilling
    SRG = "SRG"  # Suriname Guilder
    STD = "STD"  # Dobra
    SVC = "SVC"  # El Salvador Colon
    SYP = "SYP"  # Syrian Pound
    SZL = "SZL"  # Lilangeni
    THB = "THB"  # Baht
    TJR = "TJR"  # Tajik Ruble
    TMM = "TMM"  # Manat
    TND = "TND"  # Tunisian Dinar
    TOP = "TOP"  # Pa’anga
    TPE = "TPE"  # Timor Escudo
    TRL = "TRL"  # Turkish Lira
    TTD = "TTD"  # Trinidad and Tobago Dollar
    TWD = "TWD"  # New Taiwan Dollar
    TZS = "TZS"  # Tanzanian Shilling
    UAH = "UAH"  # Hryvnia
    UGX = "UGX"  # Uganda Shilling
    USD = "USD"  # US Dollar
    UYU = "UYU"  # Peso Uruguayo
    UZS = "UZS"  # Uzbekistan Sum
    VEB = "VEB"  # Bolivar
    VND = "VND"  # Dong
    VUV = "VUV"  # Vatu
    WST = "WST"  # Tala
    XAF = "XAF"  # CFA Franc BEAC
    XCD = "XCD"  # East Caribbean Dollar
    XDR = "XDR"  # SDR
    XOF = "XOF"  # CFA Franc BCEAO
    XPF = "XPF"  # CFP Franc
    YER = "YER"  # Yemeni Rial
    YUM = "YUM"  # Yugoslavian Dinar
    ZAR = "ZAR"  # Rand
    ZMK = "ZMK"  # Kwacha
    ZWD = "ZWD"  # Zimbabwe Dollar


class DataFormat(str, Enum):
    """This element declares the content model for `DataFormat` and is composed of the following elements. `DataFormat` is used to indicate the format of a value with which it is associated ("float," "integer," "string,", "exponential" or "mixed") "mixed" is only used for a group of data where each individual member of the group can be given a unique format."""

    FLOAT = "float"
    INTEGER = "integer"
    STRING = "string"
    EXPONENTIAL = "exponential"
    MIXED = "mixed"


class ScaleType(str, Enum):
    LINEAR = "Linear"
    LOGARITHMIC = "Logarithmic"


class MatML_Doc(GeneratedsSuper):
    """This element declares the content model for `MatML_Doc`, topmost in the hierarchy of elements that comprise a document marked up using MatML. Content models describe the relationships of the element and its child elements.

    - `MatML_Doc` must contain one or more `Material` elements.

    - `Metadata` contains descriptions of the data sources, properties, measurement techniques, specimens, and parameters which are referenced when materials property data are encoded using other elements. `Metadata` may occur once or not at all within the Material element. For more information, see the documentation for the `Metadata` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Material: Material = None,
        Metadata: Metadata = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        if Material is None:
            self.Material = []
        else:
            self.Material = Material
        self.Material_nsprefix_ = None
        self.Metadata = Metadata
        self.Metadata_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, MatML_Doc)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MatML_Doc.subclass:
            return MatML_Doc.subclass(*args_, **kwargs_)
        else:
            return MatML_Doc(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Material(self, id=None):
        if id is not None:
            for material in self.get_Material():
                if material.get_id() == id:
                    return material
            return None
        return self.Material

    def set_Material(self, Material):
        self.Material = Material

    def add_Material(self, value):
        self.Material.append(value)

    def insert_Material_at(self, index, value):
        self.Material.insert(index, value)

    def replace_Material_at(self, index, value):
        self.Material[index] = value

    MaterialProp = property(get_Material, set_Material)

    def get_Metadata(self):
        return self.Metadata

    def set_Metadata(self, Metadata):
        self.Metadata = Metadata

    MetadataProp = property(get_Metadata, set_Metadata)

    def has__content(self):
        if self.Material or self.Metadata is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="MatML_Doc",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("MatML_Doc")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "MatML_Doc":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="MatML_Doc"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="MatML_Doc",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="MatML_Doc"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="MatML_Doc",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for Material_ in self.Material:
            namespaceprefix_ = (
                self.Material_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Material_nsprefix_)
                else ""
            )
            Material_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Material",
                pretty_print=pretty_print,
            )
        if self.Metadata is not None:
            namespaceprefix_ = (
                self.Metadata_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Metadata_nsprefix_)
                else ""
            )
            self.Metadata.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Metadata",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Material":
            obj_ = Material.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Material.append(obj_)
            obj_.original_tagname_ = "Material"
        elif nodeName_ == "Metadata":
            obj_ = Metadata.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Metadata = obj_
            obj_.original_tagname_ = "Metadata"


class AssociationDetails(GeneratedsSuper):
    """This element declares the content model for `AssociationDetails`, which contains a description of a relationship of the component to another component in a complex material system such as a composite, weld, or multilayer material. `AssociationDetails` is composed of the following elements.

    - `Associate` contains the name of a component's associate. For example, a TiC coating has been placed on AISI 1018 steel coupons. The `Associate` of the steel, then, is the "titanium carbide coating." `Associate` must occur once and only once within the `AssociationDetails` element.
    - `Relationship` contains a description of the relationship between a component and the associate. For example, the associate of the "steel" component is the "titanium carbide coating." The relationship of the "steel" to the "titanium carbide coating" is that the steel is the "substrate" for the coating. `Relationship` must occur once and only once within the `AssociationDetails` element.
    - `Notes` contains any additional information concerning the association and may occur once or not at all within the `AssociationDetails` element.

    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Associate: str = None,
        Relationship: str = None,
        Notes=None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Associate = Associate
        self.validate_Associate(self.Associate)
        self.Associate_nsprefix_ = None
        self.Relationship = Relationship
        self.validate_Relationship(self.Relationship)
        self.Relationship_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AssociationDetails
            )
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AssociationDetails.subclass:
            return AssociationDetails.subclass(*args_, **kwargs_)
        else:
            return AssociationDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Associate(self):
        return self.Associate

    def set_Associate(self, Associate):
        self.Associate = Associate

    AssociateProp = property(get_Associate, set_Associate)

    def get_Relationship(self):
        return self.Relationship

    def set_Relationship(self, Relationship):
        self.Relationship = Relationship

    RelationshipProp = property(get_Relationship, set_Relationship)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Associate(self, value):
        result = True
        # Validate type Associate, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_Relationship(self, value):
        result = True
        # Validate type Relationship, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Associate is not None
            or self.Relationship is not None
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="AssociationDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("AssociationDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "AssociationDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="AssociationDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="AssociationDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="AssociationDetails",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="AssociationDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Associate is not None:
            namespaceprefix_ = (
                self.Associate_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Associate_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sAssociate>%s</%sAssociate>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Associate), input_name="Associate"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Relationship is not None:
            namespaceprefix_ = (
                self.Relationship_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Relationship_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sRelationship>%s</%sRelationship>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Relationship), input_name="Relationship"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Associate":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Associate")
            value_ = self.gds_validate_string(value_, node, "Associate")
            self.Associate = value_
            self.Associate_nsprefix_ = child_.prefix
            # validate type Associate
            self.validate_Associate(self.Associate)
        elif nodeName_ == "Relationship":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Relationship")
            value_ = self.gds_validate_string(value_, node, "Relationship")
            self.Relationship = value_
            self.Relationship_nsprefix_ = child_.prefix
            # validate type Relationship
            self.validate_Relationship(self.Relationship)
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class BulkDetails(GeneratedsSuper):
    """This element declares the content model for `BulkDetails`, which contains a description of the bulk material and is composed of the following elements.

    - `Name` contains the material's name and has one optional attribute, `authority`, for identifying an authoritative source of material names. `Name` must occur once and only once within the `BulkDetails` element.
    - `Class` contains the material's class and may occur zero or more times within the `BulkDetails` element.
    - `Subclass` contains the material's subclass(es) and may occur zero or more times within the `BulkDetails` element.
    - `Specification` contains the material's specification(s) and has one optional attribute, `authority`, for identifying an authoritative source of material specifications. `Specification` may occur zero or more times within the `BulkDetails` element.
    - `Source` contains the name of the source of the material and may occur once or not at all within the `BulkDetails` element.
    - `Form` contains the form of the material and may occur once or not at all within the `BulkDetails` element. It has an optional element `Geometry`, for describing the dimensions of the Component.  For additional information, see the documentation for the `Form` type.
    - `ProcessingDetails` contains a description of a processing step for the material and may occur zero or more times within the `BulkDetails` element. For additional information, see the documentation for the `ProcessingDetails` element.
    - `Characterization` contains the characterization of the material, including the formula, chemical composition, phase composition, and dimensional details. `Characterization` may occur once or not at all within the `BulkDetails` element. For additional information, see the documentation for the `Characterization` element.
    - `PropertyData` contains the property data for the material and may occur zero or more times within the `BulkDetails` element. For additional information, see the documentation for the `PropertyData` element.
    - `Notes` contains any additional information concerning the bulk material and may occur once or not at all within the `BulkDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Name: Name = None,
        Class: Class = None,
        Subclass: Class = None,
        Specification: Specification = None,
        Source: Source = None,
        Form: Form = None,
        ProcessingDetails: ProcessingDetails = None,
        Characterization: Characterization = None,
        PropertyData: PropertyData = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        if Class is None:
            self.Class = []
        else:
            self.Class = Class
        self.Class_nsprefix_ = None
        if Subclass is None:
            self.Subclass = []
        else:
            self.Subclass = Subclass
        self.Subclass_nsprefix_ = None
        if Specification is None:
            self.Specification = []
        else:
            self.Specification = Specification
        self.Specification_nsprefix_ = None
        self.Source = Source
        self.Source_nsprefix_ = None
        self.Form = Form
        self.Form_nsprefix_ = None
        if ProcessingDetails is None:
            self.ProcessingDetails = []
        else:
            self.ProcessingDetails = ProcessingDetails
        self.ProcessingDetails_nsprefix_ = None
        self.Characterization = Characterization
        self.Characterization_nsprefix_ = None
        if PropertyData is None:
            self.PropertyData = []
        else:
            self.PropertyData = PropertyData
        self.PropertyData_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, BulkDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if BulkDetails.subclass:
            return BulkDetails.subclass(*args_, **kwargs_)
        else:
            return BulkDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Class(self):
        return self.Class

    def set_Class(self, Class):
        self.Class = Class

    def add_Class(self, value):
        self.Class.append(value)

    def insert_Class_at(self, index, value):
        self.Class.insert(index, value)

    def replace_Class_at(self, index, value):
        self.Class[index] = value

    ClassProp = property(get_Class, set_Class)

    def get_Subclass(self):
        return self.Subclass

    def set_Subclass(self, Subclass):
        self.Subclass = Subclass

    def add_Subclass(self, value):
        self.Subclass.append(value)

    def insert_Subclass_at(self, index, value):
        self.Subclass.insert(index, value)

    def replace_Subclass_at(self, index, value):
        self.Subclass[index] = value

    SubclassProp = property(get_Subclass, set_Subclass)

    def get_Specification(self):
        return self.Specification

    def set_Specification(self, Specification):
        self.Specification = Specification

    def add_Specification(self, value):
        self.Specification.append(value)

    def insert_Specification_at(self, index, value):
        self.Specification.insert(index, value)

    def replace_Specification_at(self, index, value):
        self.Specification[index] = value

    SpecificationProp = property(get_Specification, set_Specification)

    def get_Source(self):
        return self.Source

    def set_Source(self, Source):
        self.Source = Source

    SourceProp = property(get_Source, set_Source)

    def get_Form(self):
        return self.Form

    def set_Form(self, Form):
        self.Form = Form

    FormProp = property(get_Form, set_Form)

    def get_ProcessingDetails(self):
        return self.ProcessingDetails

    def set_ProcessingDetails(self, ProcessingDetails):
        self.ProcessingDetails = ProcessingDetails

    def add_ProcessingDetails(self, value):
        self.ProcessingDetails.append(value)

    def insert_ProcessingDetails_at(self, index, value):
        self.ProcessingDetails.insert(index, value)

    def replace_ProcessingDetails_at(self, index, value):
        self.ProcessingDetails[index] = value

    ProcessingDetailsProp = property(get_ProcessingDetails, set_ProcessingDetails)

    def get_Characterization(self):
        return self.Characterization

    def set_Characterization(self, Characterization):
        self.Characterization = Characterization

    CharacterizationProp = property(get_Characterization, set_Characterization)

    def get_PropertyData(self, property=None):
        if property is not None:
            properties = []
            for property_data in self.get_PropertyData():
                if property_data.get_property() == property:
                    properties.append(property_data)
            return properties
        return self.PropertyData

    def set_PropertyData(self, PropertyData):
        self.PropertyData = PropertyData

    def add_PropertyData(self, value):
        self.PropertyData.append(value)

    def insert_PropertyData_at(self, index, value):
        self.PropertyData.insert(index, value)

    def replace_PropertyData_at(self, index, value):
        self.PropertyData[index] = value

    PropertyDataProp = property(get_PropertyData, set_PropertyData)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Name is not None
            or self.Class
            or self.Subclass
            or self.Specification
            or self.Source is not None
            or self.Form is not None
            or self.ProcessingDetails
            or self.Characterization is not None
            or self.PropertyData
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="BulkDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("BulkDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "BulkDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="BulkDetails"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="BulkDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="BulkDetails",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="BulkDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        for Class_ in self.Class:
            namespaceprefix_ = (
                self.Class_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Class_nsprefix_)
                else ""
            )
            Class_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Class",
                pretty_print=pretty_print,
            )
        for Subclass_ in self.Subclass:
            namespaceprefix_ = (
                self.Subclass_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Subclass_nsprefix_)
                else ""
            )
            Subclass_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Subclass",
                pretty_print=pretty_print,
            )
        for Specification_ in self.Specification:
            namespaceprefix_ = (
                self.Specification_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Specification_nsprefix_)
                else ""
            )
            Specification_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Specification",
                pretty_print=pretty_print,
            )
        if self.Source is not None:
            namespaceprefix_ = (
                self.Source_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Source_nsprefix_)
                else ""
            )
            self.Source.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Source",
                pretty_print=pretty_print,
            )
        if self.Form is not None:
            namespaceprefix_ = (
                self.Form_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Form_nsprefix_)
                else ""
            )
            self.Form.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Form",
                pretty_print=pretty_print,
            )
        for ProcessingDetails_ in self.ProcessingDetails:
            namespaceprefix_ = (
                self.ProcessingDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ProcessingDetails_nsprefix_)
                else ""
            )
            ProcessingDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ProcessingDetails",
                pretty_print=pretty_print,
            )
        if self.Characterization is not None:
            namespaceprefix_ = (
                self.Characterization_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Characterization_nsprefix_)
                else ""
            )
            self.Characterization.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Characterization",
                pretty_print=pretty_print,
            )
        for PropertyData_ in self.PropertyData:
            namespaceprefix_ = (
                self.PropertyData_nsprefix_ + ":"
                if (UseCapturedNS_ and self.PropertyData_nsprefix_)
                else ""
            )
            PropertyData_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="PropertyData",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Class":
            obj_ = Class.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Class.append(obj_)
            obj_.original_tagname_ = "Class"
        elif nodeName_ == "Subclass":
            obj_ = Class.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Subclass.append(obj_)
            obj_.original_tagname_ = "Subclass"
        elif nodeName_ == "Specification":
            obj_ = Specification.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Specification.append(obj_)
            obj_.original_tagname_ = "Specification"
        elif nodeName_ == "Source":
            obj_ = Source.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Source = obj_
            obj_.original_tagname_ = "Source"
        elif nodeName_ == "Form":
            obj_ = Form.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Form = obj_
            obj_.original_tagname_ = "Form"
        elif nodeName_ == "ProcessingDetails":
            obj_ = ProcessingDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ProcessingDetails.append(obj_)
            obj_.original_tagname_ = "ProcessingDetails"
        elif nodeName_ == "Characterization":
            obj_ = Characterization.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Characterization = obj_
            obj_.original_tagname_ = "Characterization"
        elif nodeName_ == "PropertyData":
            obj_ = PropertyData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PropertyData.append(obj_)
            obj_.original_tagname_ = "PropertyData"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class Characterization(GeneratedsSuper):
    """This element declares the content model for `Characterization`, which contains a description of the chemical composition of the bulk material or component and is composed of the following elements.

    - `Formula` contains a string representation of the chemical formula for the bulk material or component and must occur once and only once within the `Characterization` element.  For further details see documentation of the `Formula` element.
    - `ChemicalComposition` contains a description of the compounds and elements that comprise the bulk material or component and may occur once or not at all within the `Characterization` element. For additional information, see the documentation for the `ChemicalComposition` element.
    - `PhaseComposition` contains a description of the phases that comprise the bulk material or component and may occur zero or more times within the `Characterization` element. For additional information, see the documentation for the `PhaseComposition` element.
    - `DimensionalDetails` contains information relating to component or bulk material dimensional characteristics such as grain size, porosity, precipitate size and distribution, etc., and may occur zero or more times within the `Characterization` element. For additional information, see the documentation for the `DimensionalDetails` element.
    - `Notes` contains any additional information concerning the `Characterization` and may occur once or not at all within the `Characterization` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Formula: str = None,
        ChemicalComposition: ChemicalComposition = None,
        PhaseComposition: Name = None,
        DimensionalDetails: DimensionalDetails = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Formula = Formula
        self.validate_Formula(self.Formula)
        self.Formula_nsprefix_ = None
        self.ChemicalComposition = ChemicalComposition
        self.ChemicalComposition_nsprefix_ = None
        if PhaseComposition is None:
            self.PhaseComposition = []
        else:
            self.PhaseComposition = PhaseComposition
        self.PhaseComposition_nsprefix_ = None
        if DimensionalDetails is None:
            self.DimensionalDetails = []
        else:
            self.DimensionalDetails = DimensionalDetails
        self.DimensionalDetails_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Characterization)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Characterization.subclass:
            return Characterization.subclass(*args_, **kwargs_)
        else:
            return Characterization(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Formula(self):
        return self.Formula

    def set_Formula(self, Formula):
        self.Formula = Formula

    FormulaProp = property(get_Formula, set_Formula)

    def get_ChemicalComposition(self):
        return self.ChemicalComposition

    def set_ChemicalComposition(self, ChemicalComposition):
        self.ChemicalComposition = ChemicalComposition

    ChemicalCompositionProp = property(get_ChemicalComposition, set_ChemicalComposition)

    def get_PhaseComposition(self):
        return self.PhaseComposition

    def set_PhaseComposition(self, PhaseComposition):
        self.PhaseComposition = PhaseComposition

    def add_PhaseComposition(self, value):
        self.PhaseComposition.append(value)

    def insert_PhaseComposition_at(self, index, value):
        self.PhaseComposition.insert(index, value)

    def replace_PhaseComposition_at(self, index, value):
        self.PhaseComposition[index] = value

    PhaseCompositionProp = property(get_PhaseComposition, set_PhaseComposition)

    def get_DimensionalDetails(self):
        return self.DimensionalDetails

    def set_DimensionalDetails(self, DimensionalDetails):
        self.DimensionalDetails = DimensionalDetails

    def add_DimensionalDetails(self, value):
        self.DimensionalDetails.append(value)

    def insert_DimensionalDetails_at(self, index, value):
        self.DimensionalDetails.insert(index, value)

    def replace_DimensionalDetails_at(self, index, value):
        self.DimensionalDetails[index] = value

    DimensionalDetailsProp = property(get_DimensionalDetails, set_DimensionalDetails)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Formula(self, value):
        result = True
        # Validate type Formula, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Formula is not None
            or self.ChemicalComposition is not None
            or self.PhaseComposition
            or self.DimensionalDetails
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Characterization",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Characterization")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Characterization":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="Characterization",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Characterization",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="Characterization",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Characterization",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Formula is not None:
            namespaceprefix_ = (
                self.Formula_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Formula_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sFormula>%s</%sFormula>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Formula), input_name="Formula"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.ChemicalComposition is not None:
            namespaceprefix_ = (
                self.ChemicalComposition_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ChemicalComposition_nsprefix_)
                else ""
            )
            self.ChemicalComposition.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ChemicalComposition",
                pretty_print=pretty_print,
            )
        for PhaseComposition_ in self.PhaseComposition:
            namespaceprefix_ = (
                self.PhaseComposition_nsprefix_ + ":"
                if (UseCapturedNS_ and self.PhaseComposition_nsprefix_)
                else ""
            )
            PhaseComposition_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="PhaseComposition",
                pretty_print=pretty_print,
            )
        for DimensionalDetails_ in self.DimensionalDetails:
            namespaceprefix_ = (
                self.DimensionalDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.DimensionalDetails_nsprefix_)
                else ""
            )
            DimensionalDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="DimensionalDetails",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Formula":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Formula")
            value_ = self.gds_validate_string(value_, node, "Formula")
            self.Formula = value_
            self.Formula_nsprefix_ = child_.prefix
            # validate type Formula
            self.validate_Formula(self.Formula)
        elif nodeName_ == "ChemicalComposition":
            obj_ = ChemicalComposition.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ChemicalComposition = obj_
            obj_.original_tagname_ = "ChemicalComposition"
        elif nodeName_ == "PhaseComposition":
            obj_ = PhaseComposition.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PhaseComposition.append(obj_)
            obj_.original_tagname_ = "PhaseComposition"
        elif nodeName_ == "DimensionalDetails":
            obj_ = DimensionalDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DimensionalDetails.append(obj_)
            obj_.original_tagname_ = "DimensionalDetails"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class ChemicalComposition(GeneratedsSuper):
    """This element declares the content model for `ChemicalComposition`, which contains a detailed description of the compounds and elements that comprise the bulk material or component. `ChemicalComposition` must contain at least one `Compound` element or `Element` element but may contain as many of each element as needed.

    - `Compound` contains a description of a compound. For additional information, see the documentation for the `Compound` element.
    - `Element` contains a description of an element. For additional information, see the documentation for the `Element` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Compound: Compound = None,
        Element: Element = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        if Compound is None:
            self.Compound = []
        else:
            self.Compound = Compound
        self.Compound_nsprefix_ = None
        if Element is None:
            self.Element = []
        else:
            self.Element = Element
        self.Element_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ChemicalComposition
            )
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ChemicalComposition.subclass:
            return ChemicalComposition.subclass(*args_, **kwargs_)
        else:
            return ChemicalComposition(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Compound(self):
        return self.Compound

    def set_Compound(self, Compound):
        self.Compound = Compound

    def add_Compound(self, value):
        self.Compound.append(value)

    def insert_Compound_at(self, index, value):
        self.Compound.insert(index, value)

    def replace_Compound_at(self, index, value):
        self.Compound[index] = value

    CompoundProp = property(get_Compound, set_Compound)

    def get_Element(self):
        return self.Element

    def set_Element(self, Element):
        self.Element = Element

    def add_Element(self, value):
        self.Element.append(value)

    def insert_Element_at(self, index, value):
        self.Element.insert(index, value)

    def replace_Element_at(self, index, value):
        self.Element[index] = value

    ElementProp = property(get_Element, set_Element)

    def has__content(self):
        if self.Compound or self.Element:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ChemicalComposition",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("ChemicalComposition")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "ChemicalComposition":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="ChemicalComposition",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="ChemicalComposition",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="ChemicalComposition",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ChemicalComposition",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for Compound_ in self.Compound:
            namespaceprefix_ = (
                self.Compound_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Compound_nsprefix_)
                else ""
            )
            Compound_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Compound",
                pretty_print=pretty_print,
            )
        for Element_ in self.Element:
            namespaceprefix_ = (
                self.Element_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Element_nsprefix_)
                else ""
            )
            Element_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Element",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Compound":
            obj_ = Compound.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Compound.append(obj_)
            obj_.original_tagname_ = "Compound"
        elif nodeName_ == "Element":
            obj_ = Element.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Element.append(obj_)
            obj_.original_tagname_ = "Element"


class Class(GeneratedsSuper):
    """This element declares the content model for `Class`, which is the material class to which the `Material` belongs.

    The `Class` can either have a `Name` or `ParentMaterial` element:

    - `Name` contains a string representing the name of the material's class and may occur only once within the `Class` element.
    - `ParentMaterial` is a reference by `id` to another `Material` in the `MatML_Doc` and can occur only once in the `Class` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Name: Name = None,
        ParentMaterial: ParentMaterialType = None,
        ParentSubClass: Class = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        if ParentMaterial is None:
            self.ParentMaterial = []
        else:
            self.ParentMaterial = ParentMaterial
        self.ParentMaterial_nsprefix_ = None
        if ParentSubClass is None:
            self.ParentSubClass = []
        else:
            self.ParentSubClass = ParentSubClass
        self.ParentSubClass_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Class)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Class.subclass:
            return Class.subclass(*args_, **kwargs_)
        else:
            return Class(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_ParentMaterial(self):
        return self.ParentMaterial

    def set_ParentMaterial(self, ParentMaterial):
        self.ParentMaterial = ParentMaterial

    def add_ParentMaterial(self, value):
        self.ParentMaterial.append(value)

    def insert_ParentMaterial_at(self, index, value):
        self.ParentMaterial.insert(index, value)

    def replace_ParentMaterial_at(self, index, value):
        self.ParentMaterial[index] = value

    ParentMaterialProp = property(get_ParentMaterial, set_ParentMaterial)

    def get_ParentSubClass(self):
        return self.ParentSubClass

    def set_ParentSubClass(self, ParentSubClass):
        self.ParentSubClass = ParentSubClass

    def add_ParentSubClass(self, value):
        self.ParentSubClass.append(value)

    def insert_ParentSubClass_at(self, index, value):
        self.ParentSubClass.insert(index, value)

    def replace_ParentSubClass_at(self, index, value):
        self.ParentSubClass[index] = value

    ParentSubClassProp = property(get_ParentSubClass, set_ParentSubClass)

    def has__content(self):
        if self.Name is not None or self.ParentMaterial or self.ParentSubClass:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Class",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Class")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Class":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Class"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Class",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Class"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Class",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        for ParentMaterial_ in self.ParentMaterial:
            namespaceprefix_ = (
                self.ParentMaterial_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ParentMaterial_nsprefix_)
                else ""
            )
            ParentMaterial_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ParentMaterial",
                pretty_print=pretty_print,
            )
        for ParentSubClass_ in self.ParentSubClass:
            namespaceprefix_ = (
                self.ParentSubClass_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ParentSubClass_nsprefix_)
                else ""
            )
            ParentSubClass_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ParentSubClass",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "ParentMaterial":
            obj_ = ParentMaterialType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParentMaterial.append(obj_)
            obj_.original_tagname_ = "ParentMaterial"
        elif nodeName_ == "ParentSubClass":
            obj_ = Class.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParentSubClass.append(obj_)
            obj_.original_tagname_ = "ParentSubClass"


class ComponentDetails(GeneratedsSuper):
    """This element declares the content model for `ComponentDetails`, which contains a description of a component within the bulk material and has one optional attribute, `id`, which may be used as an identification specifier for the component and is especially useful for complex systems such as composite laminates.

    `ComponentDetails` is composed of the following elements.

    - `Name` contains the component's name and has one optional attribute, `authority`, for identifying an authoritative source of component names. `Name` must occur once and only once within the `ComponentDetails` type.
    - `Class` contains the component's class and may occur zero or more times within the `ComponentDetails` element.  For additional information, see the documentation for the `Class` type.
    - `Subclass` contains the component's subclass(es) and may occur zero or more times within the `ComponentDetails` element. For additional information, see the documentation for the `SubClass` type.
    - `Specification` contains the component's specification(s) and has one optional attribute, `authority`, for identifying an authoritative source of component specifications. `Specification` may occur zero or more times within the `ComponentDetails` type.
    - `Source` contains the name of the source of the component and may occur once or not at all within the `ComponentDetails` type.  For additional information, see the documentation for the `SourceDetails` element.
    - `Form` contains the form of the component and may occur once or not at all within the `ComponentDetails` type.  It has an optional element `Geometry`, for describing the dimensions of the Component.  For additional information, see the documentation for the `Form` type.
    - `ProcessingDetails` contains a description of a processing step for the component and may occur zero or more times within the `ComponentDetails` type. For additional information, see the documentation for the `ProcessingDetails` element.
    - `Characterization` contains the characterization of the component, including the formula, chemical composition, phase composition, and dimensional details. `Characterization` may occur once or not at all within the `ComponentDetails` type. For additional information, see the documentation for the `Characterization` element.
    - `PropertyData` contains the property data for the component and may occur zero or more times within the `ComponentDetails` type. For additional information, see the documentation for the `PropertyData` element.
    - `AssociationDetails` contains a description of a relationship of the component to another component and may occur zero or more times within the `ComponentDetails` type. For additional information, see the documentation for the `AssociationDetails` element. Notes contains any additional information concerning the component and may occur once or not at all within the `ComponentDetails` type.
    - `ComponentDetails` contains a description of a component within the component and is used to support encoding of information for complex materials systems such as composites. `ComponentDetails` may occur zero or more times within a `ComponentDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        Name: Name = None,
        Class: Class = None,
        Subclass: Class = None,
        Specification: Specification = None,
        Source: Source = None,
        Form: Form = None,
        ProcessingDetails: ProcessingDetails = None,
        Characterization: Characterization = None,
        PropertyData: PropertyData = None,
        AssociationDetails: AssociationDetails = None,
        ComponentDetails_member: ComponentDetails = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        if Class is None:
            self.Class = []
        else:
            self.Class = Class
        self.Class_nsprefix_ = None
        if Subclass is None:
            self.Subclass = []
        else:
            self.Subclass = Subclass
        self.Subclass_nsprefix_ = None
        if Specification is None:
            self.Specification = []
        else:
            self.Specification = Specification
        self.Specification_nsprefix_ = None
        self.Source = Source
        self.Source_nsprefix_ = None
        self.Form = Form
        self.Form_nsprefix_ = None
        if ProcessingDetails is None:
            self.ProcessingDetails = []
        else:
            self.ProcessingDetails = ProcessingDetails
        self.ProcessingDetails_nsprefix_ = None
        self.Characterization = Characterization
        self.Characterization_nsprefix_ = None
        if PropertyData is None:
            self.PropertyData = []
        else:
            self.PropertyData = PropertyData
        self.PropertyData_nsprefix_ = None
        if AssociationDetails is None:
            self.AssociationDetails = []
        else:
            self.AssociationDetails = AssociationDetails
        self.AssociationDetails_nsprefix_ = None
        if ComponentDetails_member is None:
            self.ComponentDetails = []
        else:
            self.ComponentDetails = ComponentDetails_member
        self.ComponentDetails_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, ComponentDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ComponentDetails.subclass:
            return ComponentDetails.subclass(*args_, **kwargs_)
        else:
            return ComponentDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Class(self):
        return self.Class

    def set_Class(self, Class):
        self.Class = Class

    def add_Class(self, value):
        self.Class.append(value)

    def insert_Class_at(self, index, value):
        self.Class.insert(index, value)

    def replace_Class_at(self, index, value):
        self.Class[index] = value

    ClassProp = property(get_Class, set_Class)

    def get_Subclass(self):
        return self.Subclass

    def set_Subclass(self, Subclass):
        self.Subclass = Subclass

    def add_Subclass(self, value):
        self.Subclass.append(value)

    def insert_Subclass_at(self, index, value):
        self.Subclass.insert(index, value)

    def replace_Subclass_at(self, index, value):
        self.Subclass[index] = value

    SubclassProp = property(get_Subclass, set_Subclass)

    def get_Specification(self):
        return self.Specification

    def set_Specification(self, Specification):
        self.Specification = Specification

    def add_Specification(self, value):
        self.Specification.append(value)

    def insert_Specification_at(self, index, value):
        self.Specification.insert(index, value)

    def replace_Specification_at(self, index, value):
        self.Specification[index] = value

    SpecificationProp = property(get_Specification, set_Specification)

    def get_Source(self):
        return self.Source

    def set_Source(self, Source):
        self.Source = Source

    SourceProp = property(get_Source, set_Source)

    def get_Form(self):
        return self.Form

    def set_Form(self, Form):
        self.Form = Form

    FormProp = property(get_Form, set_Form)

    def get_ProcessingDetails(self):
        return self.ProcessingDetails

    def set_ProcessingDetails(self, ProcessingDetails):
        self.ProcessingDetails = ProcessingDetails

    def add_ProcessingDetails(self, value):
        self.ProcessingDetails.append(value)

    def insert_ProcessingDetails_at(self, index, value):
        self.ProcessingDetails.insert(index, value)

    def replace_ProcessingDetails_at(self, index, value):
        self.ProcessingDetails[index] = value

    ProcessingDetailsProp = property(get_ProcessingDetails, set_ProcessingDetails)

    def get_Characterization(self):
        return self.Characterization

    def set_Characterization(self, Characterization):
        self.Characterization = Characterization

    CharacterizationProp = property(get_Characterization, set_Characterization)

    def get_PropertyData(self, property=None):
        if property is not None:
            properties = []
            for property_data in self.get_PropertyData():
                if property_data.get_property() == property:
                    properties.append(property_data)
            return properties
        return self.PropertyData

    def set_PropertyData(self, PropertyData):
        self.PropertyData = PropertyData

    def add_PropertyData(self, value):
        self.PropertyData.append(value)

    def insert_PropertyData_at(self, index, value):
        self.PropertyData.insert(index, value)

    def replace_PropertyData_at(self, index, value):
        self.PropertyData[index] = value

    PropertyDataProp = property(get_PropertyData, set_PropertyData)

    def get_AssociationDetails(self):
        return self.AssociationDetails

    def set_AssociationDetails(self, AssociationDetails):
        self.AssociationDetails = AssociationDetails

    def add_AssociationDetails(self, value):
        self.AssociationDetails.append(value)

    def insert_AssociationDetails_at(self, index, value):
        self.AssociationDetails.insert(index, value)

    def replace_AssociationDetails_at(self, index, value):
        self.AssociationDetails[index] = value

    AssociationDetailsProp = property(get_AssociationDetails, set_AssociationDetails)

    def get_ComponentDetails(self, id=None):
        if id is not None:
            for component_details in self.get_ComponentDetails():
                if component_details.get_id() == id:
                    return component_details
            return None
        return self.ComponentDetails

    def set_ComponentDetails(self, ComponentDetails):
        self.ComponentDetails = ComponentDetails

    def add_ComponentDetails(self, value):
        self.ComponentDetails.append(value)

    def insert_ComponentDetails_at(self, index, value):
        self.ComponentDetails.insert(index, value)

    def replace_ComponentDetails_at(self, index, value):
        self.ComponentDetails[index] = value

    ComponentDetailsProp = property(get_ComponentDetails, set_ComponentDetails)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def has__content(self):
        if (
            self.Name is not None
            or self.Class
            or self.Subclass
            or self.Specification
            or self.Source is not None
            or self.Form is not None
            or self.ProcessingDetails
            or self.Characterization is not None
            or self.PropertyData
            or self.AssociationDetails
            or self.ComponentDetails
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ComponentDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("ComponentDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "ComponentDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="ComponentDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="ComponentDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="ComponentDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ComponentDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        for Class_ in self.Class:
            namespaceprefix_ = (
                self.Class_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Class_nsprefix_)
                else ""
            )
            Class_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Class",
                pretty_print=pretty_print,
            )
        for Subclass_ in self.Subclass:
            namespaceprefix_ = (
                self.Subclass_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Subclass_nsprefix_)
                else ""
            )
            Subclass_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Subclass",
                pretty_print=pretty_print,
            )
        for Specification_ in self.Specification:
            namespaceprefix_ = (
                self.Specification_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Specification_nsprefix_)
                else ""
            )
            Specification_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Specification",
                pretty_print=pretty_print,
            )
        if self.Source is not None:
            namespaceprefix_ = (
                self.Source_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Source_nsprefix_)
                else ""
            )
            self.Source.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Source",
                pretty_print=pretty_print,
            )
        if self.Form is not None:
            namespaceprefix_ = (
                self.Form_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Form_nsprefix_)
                else ""
            )
            self.Form.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Form",
                pretty_print=pretty_print,
            )
        for ProcessingDetails_ in self.ProcessingDetails:
            namespaceprefix_ = (
                self.ProcessingDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ProcessingDetails_nsprefix_)
                else ""
            )
            ProcessingDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ProcessingDetails",
                pretty_print=pretty_print,
            )
        if self.Characterization is not None:
            namespaceprefix_ = (
                self.Characterization_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Characterization_nsprefix_)
                else ""
            )
            self.Characterization.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Characterization",
                pretty_print=pretty_print,
            )
        for PropertyData_ in self.PropertyData:
            namespaceprefix_ = (
                self.PropertyData_nsprefix_ + ":"
                if (UseCapturedNS_ and self.PropertyData_nsprefix_)
                else ""
            )
            PropertyData_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="PropertyData",
                pretty_print=pretty_print,
            )
        for AssociationDetails_ in self.AssociationDetails:
            namespaceprefix_ = (
                self.AssociationDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.AssociationDetails_nsprefix_)
                else ""
            )
            AssociationDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="AssociationDetails",
                pretty_print=pretty_print,
            )
        for ComponentDetails_ in self.ComponentDetails:
            namespaceprefix_ = (
                self.ComponentDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ComponentDetails_nsprefix_)
                else ""
            )
            ComponentDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ComponentDetails",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Class":
            obj_ = Class.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Class.append(obj_)
            obj_.original_tagname_ = "Class"
        elif nodeName_ == "Subclass":
            obj_ = Class.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Subclass.append(obj_)
            obj_.original_tagname_ = "Subclass"
        elif nodeName_ == "Specification":
            obj_ = Specification.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Specification.append(obj_)
            obj_.original_tagname_ = "Specification"
        elif nodeName_ == "Source":
            obj_ = Source.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Source = obj_
            obj_.original_tagname_ = "Source"
        elif nodeName_ == "Form":
            obj_ = Form.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Form = obj_
            obj_.original_tagname_ = "Form"
        elif nodeName_ == "ProcessingDetails":
            obj_ = ProcessingDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ProcessingDetails.append(obj_)
            obj_.original_tagname_ = "ProcessingDetails"
        elif nodeName_ == "Characterization":
            obj_ = Characterization.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Characterization = obj_
            obj_.original_tagname_ = "Characterization"
        elif nodeName_ == "PropertyData":
            obj_ = PropertyData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PropertyData.append(obj_)
            obj_.original_tagname_ = "PropertyData"
        elif nodeName_ == "AssociationDetails":
            obj_ = AssociationDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AssociationDetails.append(obj_)
            obj_.original_tagname_ = "AssociationDetails"
        elif nodeName_ == "ComponentDetails":
            obj_ = ComponentDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ComponentDetails.append(obj_)
            obj_.original_tagname_ = "ComponentDetails"


class Compound(GeneratedsSuper):
    """This element declares the content model for `Compound`, which contains the elemental description of a chemical compound and is composed the following elements.

    - `Element` contains the description of a chemical element and must occur one or more times within the `Compound` element. For additional information, see the documentation for the `Element` element.
    - Concentration contains the concentration of the compound and may occur once or not at all within the `Compound` element. For additional information, see the documentation for the `Concentration` element.
    - `Notes` contains any additional information concerning the compound and may occur once or not at all within the `Compound` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Element: Element = None,
        Concentration: Concentration = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        if Element is None:
            self.Element = []
        else:
            self.Element = Element
        self.Element_nsprefix_ = None
        self.Concentration = Concentration
        self.Concentration_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Compound)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Compound.subclass:
            return Compound.subclass(*args_, **kwargs_)
        else:
            return Compound(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Element(self):
        return self.Element

    def set_Element(self, Element):
        self.Element = Element

    def add_Element(self, value):
        self.Element.append(value)

    def insert_Element_at(self, index, value):
        self.Element.insert(index, value)

    def replace_Element_at(self, index, value):
        self.Element[index] = value

    ElementProp = property(get_Element, set_Element)

    def get_Concentration(self):
        return self.Concentration

    def set_Concentration(self, Concentration):
        self.Concentration = Concentration

    ConcentrationProp = property(get_Concentration, set_Concentration)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if self.Element or self.Concentration is not None or self.Notes is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Compound",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Compound")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Compound":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Compound"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Compound",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Compound"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Compound",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for Element_ in self.Element:
            namespaceprefix_ = (
                self.Element_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Element_nsprefix_)
                else ""
            )
            Element_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Element",
                pretty_print=pretty_print,
            )
        if self.Concentration is not None:
            namespaceprefix_ = (
                self.Concentration_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Concentration_nsprefix_)
                else ""
            )
            self.Concentration.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Concentration",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Element":
            obj_ = Element.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Element.append(obj_)
            obj_.original_tagname_ = "Element"
        elif nodeName_ == "Concentration":
            obj_ = Concentration.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Concentration = obj_
            obj_.original_tagname_ = "Concentration"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class Concentration(GeneratedsSuper):
    """This element declares the content model for `Concentration` and is composed of the following elements.

    - `Value` contains the value of the concentration and has one required attribute, `format`, for indicating the format of the value.  `Value` must occur once and only once within the `Concentration` element.
    - `Units` contains the units for the value of the concentration and must occur once and only once within the `Concentration` element. For additional information, see the documentation for the `Units` element.
    - `Qualifier` contains any qualifier pertinent to the value of the concentration (e.g. "min," "max," etc.) and may occur once or not at all within the `Concentration` element.
    - `Uncertainty` contains the measurement uncertainty(ies) of the data in Data and may occur zero or more times within the `Concentration` element. For additional information, see the documentation for the `Uncertainty` type.
    - `Notes` contains any additional information concerning the concentration and may occur once or not at all within the `Concentration` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Value: Value = None,
        Units: Units = None,
        Qualifier: str = None,
        Uncertainty: Uncertainty = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
        self.Units = Units
        self.Units_nsprefix_ = None
        if Qualifier is None:
            self.Qualifier = []
        else:
            self.Qualifier = Qualifier
        self.Qualifier_nsprefix_ = None
        if Uncertainty is None:
            self.Uncertainty = []
        else:
            self.Uncertainty = Uncertainty
        self.Uncertainty_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Concentration)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Concentration.subclass:
            return Concentration.subclass(*args_, **kwargs_)
        else:
            return Concentration(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Value(self):
        return self.Value

    def set_Value(self, Value):
        self.Value = Value

    ValueProp = property(get_Value, set_Value)

    def get_Units(self):
        return self.Units

    def set_Units(self, Units):
        self.Units = Units

    UnitsProp = property(get_Units, set_Units)

    def get_Qualifier(self):
        return self.Qualifier

    def set_Qualifier(self, Qualifier):
        self.Qualifier = Qualifier

    def add_Qualifier(self, value):
        self.Qualifier.append(value)

    def insert_Qualifier_at(self, index, value):
        self.Qualifier.insert(index, value)

    def replace_Qualifier_at(self, index, value):
        self.Qualifier[index] = value

    QualifierProp = property(get_Qualifier, set_Qualifier)

    def get_Uncertainty(self):
        return self.Uncertainty

    def set_Uncertainty(self, Uncertainty):
        self.Uncertainty = Uncertainty

    def add_Uncertainty(self, value):
        self.Uncertainty.append(value)

    def insert_Uncertainty_at(self, index, value):
        self.Uncertainty.insert(index, value)

    def replace_Uncertainty_at(self, index, value):
        self.Uncertainty[index] = value

    UncertaintyProp = property(get_Uncertainty, set_Uncertainty)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Qualifier(self, value):
        result = True
        # Validate type Qualifier, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Value is not None
            or self.Units is not None
            or self.Qualifier
            or self.Uncertainty
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Concentration",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Concentration")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Concentration":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Concentration"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Concentration",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="Concentration",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Concentration",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Value is not None:
            namespaceprefix_ = (
                self.Value_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Value_nsprefix_)
                else ""
            )
            self.Value.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Value",
                pretty_print=pretty_print,
            )
        if self.Units is not None:
            namespaceprefix_ = (
                self.Units_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Units_nsprefix_)
                else ""
            )
            self.Units.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Units",
                pretty_print=pretty_print,
            )
        for Qualifier_ in self.Qualifier:
            namespaceprefix_ = (
                self.Qualifier_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Qualifier_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sQualifier>%s</%sQualifier>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(Qualifier_), input_name="Qualifier"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        for Uncertainty_ in self.Uncertainty:
            namespaceprefix_ = (
                self.Uncertainty_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Uncertainty_nsprefix_)
                else ""
            )
            Uncertainty_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Uncertainty",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Value":
            obj_ = Value.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Value = obj_
            obj_.original_tagname_ = "Value"
        elif nodeName_ == "Units":
            obj_ = Units.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Units = obj_
            obj_.original_tagname_ = "Units"
        elif nodeName_ == "Qualifier":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Qualifier")
            value_ = self.gds_validate_string(value_, node, "Qualifier")
            self.Qualifier.append(value_)
            self.Qualifier_nsprefix_ = child_.prefix
            # validate type Qualifier
            self.validate_Qualifier(self.Qualifier[-1])
        elif nodeName_ == "Uncertainty":
            obj_ = Uncertainty.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Uncertainty.append(obj_)
            obj_.original_tagname_ = "Uncertainty"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class DimensionalDetails(GeneratedsSuper):
    """This element declares the content model for `DimensionalDetails`, which contains a description of a dimensional characteristic (e.g. grain size, porosity, precipitate size and distribution, etc.) of the bulk material or component and is composed of the following elements.

    - `Name` contains the name of the characteristic and has one optional attribute, `authority`, for identifying an authoritative source of dimensional characteristic names. `Name` must occur once and only once within the `DimensionalDetails` element.
    - `Value` contains the value of the dimensional characteristic and has one required attribute, format, for indicating the format of the value.  `Value` must occur once and only once within the `DimensionalDetails` element.
    - `Units` contains the units for the value of the dimensional characteristic and must occur once and only once within the `DimensionalDetails` element. For additional information, see the documentation for the `Units` type.
    - `Qualifier` contains any qualifier pertinent to the value of the dimensional characteristic (e.g. "min," "max," etc.) and may occur once or not at all within the `DimensionalDetails` element.
    - `Uncertainty` contains the measurement uncertainty(ies) of the data in Data and may occur zero or more times within the `DimensionalDetails` element. For additional information, see the documentation for the `Uncertainty` type.
    - `Notes` contains any additional information concerning the dimensional characteristic and may occur once or not at all within the `DimensionalDetails` element.

    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Name: Name = None,
        Value: Value = None,
        Units: Units = None,
        Qualifier: str = None,
        Uncertainty: Uncertainty = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
        self.Units = Units
        self.Units_nsprefix_ = None
        self.Qualifier = Qualifier
        self.validate_Qualifier(self.Qualifier)
        self.Qualifier_nsprefix_ = None
        if Uncertainty is None:
            self.Uncertainty = []
        else:
            self.Uncertainty = Uncertainty
        self.Uncertainty_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DimensionalDetails
            )
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DimensionalDetails.subclass:
            return DimensionalDetails.subclass(*args_, **kwargs_)
        else:
            return DimensionalDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Value(self):
        return self.Value

    def set_Value(self, Value):
        self.Value = Value

    ValueProp = property(get_Value, set_Value)

    def get_Units(self):
        return self.Units

    def set_Units(self, Units):
        self.Units = Units

    UnitsProp = property(get_Units, set_Units)

    def get_Qualifier(self):
        return self.Qualifier

    def set_Qualifier(self, Qualifier):
        self.Qualifier = Qualifier

    QualifierProp = property(get_Qualifier, set_Qualifier)

    def get_Uncertainty(self):
        return self.Uncertainty

    def set_Uncertainty(self, Uncertainty):
        self.Uncertainty = Uncertainty

    def add_Uncertainty(self, value):
        self.Uncertainty.append(value)

    def insert_Uncertainty_at(self, index, value):
        self.Uncertainty.insert(index, value)

    def replace_Uncertainty_at(self, index, value):
        self.Uncertainty[index] = value

    UncertaintyProp = property(get_Uncertainty, set_Uncertainty)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Qualifier(self, value):
        result = True
        # Validate type Qualifier, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Name is not None
            or self.Value is not None
            or self.Units is not None
            or self.Qualifier is not None
            or self.Uncertainty
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="DimensionalDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("DimensionalDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "DimensionalDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="DimensionalDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="DimensionalDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="DimensionalDetails",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="DimensionalDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Value is not None:
            namespaceprefix_ = (
                self.Value_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Value_nsprefix_)
                else ""
            )
            self.Value.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Value",
                pretty_print=pretty_print,
            )
        if self.Units is not None:
            namespaceprefix_ = (
                self.Units_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Units_nsprefix_)
                else ""
            )
            self.Units.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Units",
                pretty_print=pretty_print,
            )
        if self.Qualifier is not None:
            namespaceprefix_ = (
                self.Qualifier_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Qualifier_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sQualifier>%s</%sQualifier>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Qualifier), input_name="Qualifier"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        for Uncertainty_ in self.Uncertainty:
            namespaceprefix_ = (
                self.Uncertainty_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Uncertainty_nsprefix_)
                else ""
            )
            Uncertainty_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Uncertainty",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Value":
            obj_ = Value.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Value = obj_
            obj_.original_tagname_ = "Value"
        elif nodeName_ == "Units":
            obj_ = Units.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Units = obj_
            obj_.original_tagname_ = "Units"
        elif nodeName_ == "Qualifier":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Qualifier")
            value_ = self.gds_validate_string(value_, node, "Qualifier")
            self.Qualifier = value_
            self.Qualifier_nsprefix_ = child_.prefix
            # validate type Qualifier
            self.validate_Qualifier(self.Qualifier)
        elif nodeName_ == "Uncertainty":
            obj_ = Uncertainty.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Uncertainty.append(obj_)
            obj_.original_tagname_ = "Uncertainty"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class Element(GeneratedsSuper):
    """This element declares the content model for `Element` and is composed of the following elements.

    - `Symbol` contains the symbol for the chemical element, which is one among those enumerated by the `ChemicalElementSymbol` datatype. `Symbol` has one optional attribute, `subscript`, for indicating the subscript (formula units) of the chemical element. `Symbol` must occur once and only once within the `Element` element. For additional information, see the documentation for the `ChemicalElementSymbol` datatype.
    - `Concentration` contains the concentration of the element and may occur once or not at all within the `Element` element. For additional information, see the documentation for the `Concentration` element.
    - `Notes` contains any additional information concerning the element and may occur once or not at all within the `Element` element.

    `Symbol`:
    - This element declares the content model for `Symbol`, which contains the symbol for the chemical element.
    - The entry for `Symbol` is selected from among the strings enumerated by the `ChemicalElementSymbol` datatype.
    - `Symbol` has one optional attribute, `subscript`, for indicating the subscript (formula units) of the chemical element.

    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Symbol: SymbolType = None,
        Concentration: Concentration = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Symbol = Symbol
        self.Symbol_nsprefix_ = None
        self.Concentration = Concentration
        self.Concentration_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Element)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Element.subclass:
            return Element.subclass(*args_, **kwargs_)
        else:
            return Element(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Symbol(self):
        return self.Symbol

    def set_Symbol(self, Symbol):
        self.Symbol = Symbol

    SymbolProp = property(get_Symbol, set_Symbol)

    def get_Concentration(self):
        return self.Concentration

    def set_Concentration(self, Concentration):
        self.Concentration = Concentration

    ConcentrationProp = property(get_Concentration, set_Concentration)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Symbol is not None
            or self.Concentration is not None
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Element",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Element")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Element":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Element"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Element",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Element"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Element",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Symbol is not None:
            namespaceprefix_ = (
                self.Symbol_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Symbol_nsprefix_)
                else ""
            )
            self.Symbol.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Symbol",
                pretty_print=pretty_print,
            )
        if self.Concentration is not None:
            namespaceprefix_ = (
                self.Concentration_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Concentration_nsprefix_)
                else ""
            )
            self.Concentration.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Concentration",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Symbol":
            obj_ = SymbolType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Symbol = obj_
            obj_.original_tagname_ = "Symbol"
        elif nodeName_ == "Concentration":
            obj_ = Concentration.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Concentration = obj_
            obj_.original_tagname_ = "Concentration"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class Form(GeneratedsSuper):
    """This element declares the content model for `Form`, which contains a description of the form of the bulk material or component.

    It also contains an element to describe the geometry of the the form and an element for any notes.  For additional information, see the documentation for the `Geometry` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Description: Name = None,
        Geometry: Geometry = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Description = Description
        self.Description_nsprefix_ = None
        self.Geometry = Geometry
        self.Geometry_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Form)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Form.subclass:
            return Form.subclass(*args_, **kwargs_)
        else:
            return Form(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Description(self):
        return self.Description

    def set_Description(self, Description):
        self.Description = Description

    DescriptionProp = property(get_Description, set_Description)

    def get_Geometry(self):
        return self.Geometry

    def set_Geometry(self, Geometry):
        self.Geometry = Geometry

    GeometryProp = property(get_Geometry, set_Geometry)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Description is not None
            or self.Geometry is not None
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Form",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Form")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Form":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Form"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Form",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Form"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Form",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Description is not None:
            namespaceprefix_ = (
                self.Description_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Description_nsprefix_)
                else ""
            )
            self.Description.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Description",
                pretty_print=pretty_print,
            )
        if self.Geometry is not None:
            namespaceprefix_ = (
                self.Geometry_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Geometry_nsprefix_)
                else ""
            )
            self.Geometry.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Geometry",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Description":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Description = obj_
            obj_.original_tagname_ = "Description"
        elif nodeName_ == "Geometry":
            obj_ = Geometry.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Geometry = obj_
            obj_.original_tagname_ = "Geometry"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class Geometry(GeneratedsSuper):
    """This element declares the content model for `Geometry`, which contains a description of the geometry of the bulk material, component or specimen and is composed of the following elements.

    - `Shape` is a string describing the shape of the bulk material or component and must occur once and only once within the `Geometry` element.
    - `Dimensions` is a string describing the dimensions of the bulk material or component and may occur once or not at all within the `Geometry` element.
    - `Orientation`  is a string describing the orientation of the bulk material or component and may occur once or not at all within the `Geometry` element.
    - `Notes` contains any additional information concerning the geometry and may occur once or not at all within the `Geometry` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Shape: str = None,
        Dimensions: str = None,
        Orientation: str = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Shape = Shape
        self.Shape_nsprefix_ = None
        self.Dimensions = Dimensions
        self.Dimensions_nsprefix_ = None
        self.Orientation = Orientation
        self.Orientation_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Geometry)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Geometry.subclass:
            return Geometry.subclass(*args_, **kwargs_)
        else:
            return Geometry(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Shape(self):
        return self.Shape

    def set_Shape(self, Shape):
        self.Shape = Shape

    ShapeProp = property(get_Shape, set_Shape)

    def get_Dimensions(self):
        return self.Dimensions

    def set_Dimensions(self, Dimensions):
        self.Dimensions = Dimensions

    DimensionsProp = property(get_Dimensions, set_Dimensions)

    def get_Orientation(self):
        return self.Orientation

    def set_Orientation(self, Orientation):
        self.Orientation = Orientation

    OrientationProp = property(get_Orientation, set_Orientation)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Shape is not None
            or self.Dimensions is not None
            or self.Orientation is not None
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Geometry",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Geometry")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Geometry":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Geometry"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Geometry",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Geometry"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Geometry",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Shape is not None:
            namespaceprefix_ = (
                self.Shape_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Shape_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sShape>%s</%sShape>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Shape), input_name="Shape"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Dimensions is not None:
            namespaceprefix_ = (
                self.Dimensions_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Dimensions_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sDimensions>%s</%sDimensions>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Dimensions), input_name="Dimensions"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Orientation is not None:
            namespaceprefix_ = (
                self.Orientation_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Orientation_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sOrientation>%s</%sOrientation>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Orientation), input_name="Orientation"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Shape":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Shape")
            value_ = self.gds_validate_string(value_, node, "Shape")
            self.Shape = value_
            self.Shape_nsprefix_ = child_.prefix
        elif nodeName_ == "Dimensions":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Dimensions")
            value_ = self.gds_validate_string(value_, node, "Dimensions")
            self.Dimensions = value_
            self.Dimensions_nsprefix_ = child_.prefix
        elif nodeName_ == "Orientation":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Orientation")
            value_ = self.gds_validate_string(value_, node, "Orientation")
            self.Orientation = value_
            self.Orientation_nsprefix_ = child_.prefix
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class Glossary(GeneratedsSuper):
    """This element declares the content model for `Glossary`, which contains descriptions of material and property terms used in the document. `Glossary` must contain one or more `GlossaryTerm` elements."""

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, Term: GlossaryTerm = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        if Term is None:
            self.Term = []
        else:
            self.Term = Term
        self.Term_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Glossary)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Glossary.subclass:
            return Glossary.subclass(*args_, **kwargs_)
        else:
            return Glossary(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Term(self):
        return self.Term

    def set_Term(self, Term):
        self.Term = Term

    def add_Term(self, value):
        self.Term.append(value)

    def insert_Term_at(self, index, value):
        self.Term.insert(index, value)

    def replace_Term_at(self, index, value):
        self.Term[index] = value

    TermProp = property(get_Term, set_Term)

    def has__content(self):
        if self.Term:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Glossary",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Glossary")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Glossary":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Glossary"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Glossary",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Glossary"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Glossary",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for Term_ in self.Term:
            namespaceprefix_ = (
                self.Term_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Term_nsprefix_)
                else ""
            )
            Term_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Term",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Term":
            obj_ = GlossaryTerm.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Term.append(obj_)
            obj_.original_tagname_ = "Term"


class GlossaryTerm(GeneratedsSuper):
    """This element declares the content model for `GlossaryTerm` which is composed of the following elements.

    - `Name` contains the term's name and has one optional attribute, authority, for identifying an authoritative source of terms. Name must occur once and only once within the `GlossaryTerm` element.
    - `Definition` contains the term's definition and must occur once and only once within the `GlossaryTerm` element.
    - `Abbreviation` contains the term's abbreviations and may occur zero or more times within the `GlossaryTerm` element.
    - `Synonym` contains the term's synonyms and may occur zero or more times within the `GlossaryTerm` element.
    - `Notes` contains any additional information concerning the term and may occur once or not at all within the `GlossaryTerm` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Name: Name = None,
        Definition: str = None,
        Abbreviation: str = None,
        Synonym: str = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Definition = Definition
        self.Definition_nsprefix_ = None
        if Abbreviation is None:
            self.Abbreviation = []
        else:
            self.Abbreviation = Abbreviation
        self.Abbreviation_nsprefix_ = None
        if Synonym is None:
            self.Synonym = []
        else:
            self.Synonym = Synonym
        self.Synonym_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, GlossaryTerm)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GlossaryTerm.subclass:
            return GlossaryTerm.subclass(*args_, **kwargs_)
        else:
            return GlossaryTerm(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Definition(self):
        return self.Definition

    def set_Definition(self, Definition):
        self.Definition = Definition

    DefinitionProp = property(get_Definition, set_Definition)

    def get_Abbreviation(self):
        return self.Abbreviation

    def set_Abbreviation(self, Abbreviation):
        self.Abbreviation = Abbreviation

    def add_Abbreviation(self, value):
        self.Abbreviation.append(value)

    def insert_Abbreviation_at(self, index, value):
        self.Abbreviation.insert(index, value)

    def replace_Abbreviation_at(self, index, value):
        self.Abbreviation[index] = value

    AbbreviationProp = property(get_Abbreviation, set_Abbreviation)

    def get_Synonym(self):
        return self.Synonym

    def set_Synonym(self, Synonym):
        self.Synonym = Synonym

    def add_Synonym(self, value):
        self.Synonym.append(value)

    def insert_Synonym_at(self, index, value):
        self.Synonym.insert(index, value)

    def replace_Synonym_at(self, index, value):
        self.Synonym[index] = value

    SynonymProp = property(get_Synonym, set_Synonym)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Name is not None
            or self.Definition is not None
            or self.Abbreviation
            or self.Synonym
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="GlossaryTerm",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("GlossaryTerm")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "GlossaryTerm":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="GlossaryTerm"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="GlossaryTerm",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="GlossaryTerm",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="GlossaryTerm",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Definition is not None:
            namespaceprefix_ = (
                self.Definition_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Definition_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sDefinition>%s</%sDefinition>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Definition), input_name="Definition"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        for Abbreviation_ in self.Abbreviation:
            namespaceprefix_ = (
                self.Abbreviation_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Abbreviation_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sAbbreviation>%s</%sAbbreviation>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(Abbreviation_), input_name="Abbreviation"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        for Synonym_ in self.Synonym:
            namespaceprefix_ = (
                self.Synonym_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Synonym_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sSynonym>%s</%sSynonym>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(Synonym_), input_name="Synonym"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Definition":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Definition")
            value_ = self.gds_validate_string(value_, node, "Definition")
            self.Definition = value_
            self.Definition_nsprefix_ = child_.prefix
        elif nodeName_ == "Abbreviation":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Abbreviation")
            value_ = self.gds_validate_string(value_, node, "Abbreviation")
            self.Abbreviation.append(value_)
            self.Abbreviation_nsprefix_ = child_.prefix
        elif nodeName_ == "Synonym":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Synonym")
            value_ = self.gds_validate_string(value_, node, "Synonym")
            self.Synonym.append(value_)
            self.Synonym_nsprefix_ = child_.prefix
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class Graphs(GeneratedsSuper):
    """This element declares the content model for `Graphs`, which must contain one or more `Graph` elements.

    `Graph` uses the W3C's Scalable Vector Graphics markup language (SVG) for describing two dimensional graphics and allows for three types of graphical objects: vector graphics shapes, images, and text.

    `Graph` must occur one or more times within the `Graphs` element. For more information concerning SVG, see the documentation at http://www.w3.org/TR/SVG/.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, Graph: GraphType = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        if Graph is None:
            self.Graph = []
        else:
            self.Graph = Graph
        self.Graph_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Graphs)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Graphs.subclass:
            return Graphs.subclass(*args_, **kwargs_)
        else:
            return Graphs(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Graph(self):
        return self.Graph

    def set_Graph(self, Graph):
        self.Graph = Graph

    def add_Graph(self, value):
        self.Graph.append(value)

    def insert_Graph_at(self, index, value):
        self.Graph.insert(index, value)

    def replace_Graph_at(self, index, value):
        self.Graph[index] = value

    GraphProp = property(get_Graph, set_Graph)

    def has__content(self):
        if self.Graph:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Graphs",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Graphs")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Graphs":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Graphs"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Graphs",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Graphs"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Graphs",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for Graph_ in self.Graph:
            namespaceprefix_ = (
                self.Graph_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Graph_nsprefix_)
                else ""
            )
            Graph_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Graph",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Graph":
            obj_ = GraphType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Graph.append(obj_)
            obj_.original_tagname_ = "Graph"


class Material(GeneratedsSuper):
    """This element declares the content model for `Material`, which contains materials data. `Material` has three optional attributes.

    1. The first attribute, `id`, may be used as an identification specifier for the material, which is especially useful for complex systems such as composite laminates.
    2. The second attribute, `layers`, may be used to indicate the number of layers in complex systems such as composite laminates.
    3. The third attribute, `local_frame_of_reference`, may be used as an identification specifier for the local material orientation relative to the global frame of reference, which is especially useful for complex systems such as anisotropic materials.

    Material is composed of the following elements.

    - BulkDetails contains a description of the bulk material and must occur once and only once within the Material element. For additional information, see the documentation for the BulkDetails element.
    - ComponentDetails contains a description of a component within the bulk material and may occur zero or more times within the Material element. ComponentDetails may be used to describe complex materials systems such as welds (e.g. the base metal, the heat affected zone, and the weld metal) or composites (e.g. the whiskers, fibers, and matrix of a fiber-reinforced composite material). For additional information, see the documentation for the ComponentDetails element.
    - Graphs contains descriptions of two dimensional graphics and may occur once or not at all within the Material element. For additional information, see the documentation for the Graphs element.
    - Glossary contains descriptions of the material and property terms used in the document and may occur once or not at all within the Material element. For additional information, see the documentation for the Glossary element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        layers: int = None,
        local_frame_of_reference: str = None,
        BulkDetails: BulkDetails = None,
        ComponentDetails: BulkDetails = None,
        Graphs: Graphs = None,
        Glossary: Glossary = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.layers = _cast(int, layers)
        self.layers_nsprefix_ = None
        self.local_frame_of_reference = _cast(None, local_frame_of_reference)
        self.local_frame_of_reference_nsprefix_ = None
        self.BulkDetails = BulkDetails
        self.BulkDetails_nsprefix_ = None
        if ComponentDetails is None:
            self.ComponentDetails = []
        else:
            self.ComponentDetails = ComponentDetails
        self.ComponentDetails_nsprefix_ = None
        self.Graphs = Graphs
        self.Graphs_nsprefix_ = None
        self.Glossary = Glossary
        self.Glossary_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Material)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Material.subclass:
            return Material.subclass(*args_, **kwargs_)
        else:
            return Material(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_BulkDetails(self):
        return self.BulkDetails

    def set_BulkDetails(self, BulkDetails):
        self.BulkDetails = BulkDetails

    BulkDetailsProp = property(get_BulkDetails, set_BulkDetails)

    def get_ComponentDetails(self, id=None):
        if id is not None:
            for component_details in self.get_ComponentDetails():
                if component_details.get_id() == id:
                    return component_details
            return None
        return self.ComponentDetails

    def set_ComponentDetails(self, ComponentDetails):
        self.ComponentDetails = ComponentDetails

    def add_ComponentDetails(self, value):
        self.ComponentDetails.append(value)

    def insert_ComponentDetails_at(self, index, value):
        self.ComponentDetails.insert(index, value)

    def replace_ComponentDetails_at(self, index, value):
        self.ComponentDetails[index] = value

    ComponentDetailsProp = property(get_ComponentDetails, set_ComponentDetails)

    def get_Graphs(self):
        return self.Graphs

    def set_Graphs(self, Graphs):
        self.Graphs = Graphs

    GraphsProp = property(get_Graphs, set_Graphs)

    def get_Glossary(self):
        return self.Glossary

    def set_Glossary(self, Glossary):
        self.Glossary = Glossary

    GlossaryProp = property(get_Glossary, set_Glossary)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def get_layers(self):
        return self.layers

    def set_layers(self, layers):
        self.layers = layers

    layersProp = property(get_layers, set_layers)

    def get_local_frame_of_reference(self):
        return self.local_frame_of_reference

    def set_local_frame_of_reference(self, local_frame_of_reference):
        self.local_frame_of_reference = local_frame_of_reference

    local_frame_of_referenceProp = property(
        get_local_frame_of_reference, set_local_frame_of_reference
    )

    def has__content(self):
        if (
            self.BulkDetails is not None
            or self.ComponentDetails
            or self.Graphs is not None
            or self.Glossary is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Material",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Material")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Material":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Material"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Material",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Material"
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )
        if self.layers is not None and "layers" not in already_processed:
            already_processed.add("layers")
            outfile.write(
                ' layers="%s"'
                % self.gds_format_integer(self.layers, input_name="layers")
            )
        if (
            self.local_frame_of_reference is not None
            and "local_frame_of_reference" not in already_processed
        ):
            already_processed.add("local_frame_of_reference")
            outfile.write(
                " local_frame_of_reference=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.local_frame_of_reference),
                            input_name="local_frame_of_reference",
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Material",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.BulkDetails is not None:
            namespaceprefix_ = (
                self.BulkDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.BulkDetails_nsprefix_)
                else ""
            )
            self.BulkDetails.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="BulkDetails",
                pretty_print=pretty_print,
            )
        for ComponentDetails_ in self.ComponentDetails:
            namespaceprefix_ = (
                self.ComponentDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ComponentDetails_nsprefix_)
                else ""
            )
            ComponentDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ComponentDetails",
                pretty_print=pretty_print,
            )
        if self.Graphs is not None:
            namespaceprefix_ = (
                self.Graphs_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Graphs_nsprefix_)
                else ""
            )
            self.Graphs.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Graphs",
                pretty_print=pretty_print,
            )
        if self.Glossary is not None:
            namespaceprefix_ = (
                self.Glossary_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Glossary_nsprefix_)
                else ""
            )
            self.Glossary.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Glossary",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value
        value = find_attr_value_("layers", node)
        if value is not None and "layers" not in already_processed:
            already_processed.add("layers")
            self.layers = self.gds_parse_integer(value, node, "layers")
        value = find_attr_value_("local_frame_of_reference", node)
        if value is not None and "local_frame_of_reference" not in already_processed:
            already_processed.add("local_frame_of_reference")
            self.local_frame_of_reference = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "BulkDetails":
            obj_ = BulkDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.BulkDetails = obj_
            obj_.original_tagname_ = "BulkDetails"
        elif nodeName_ == "ComponentDetails":
            obj_ = ComponentDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ComponentDetails.append(obj_)
            obj_.original_tagname_ = "ComponentDetails"
        elif nodeName_ == "Graphs":
            obj_ = Graphs.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Graphs = obj_
            obj_.original_tagname_ = "Graphs"
        elif nodeName_ == "Glossary":
            obj_ = Glossary.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Glossary = obj_
            obj_.original_tagname_ = "Glossary"


class Metadata(GeneratedsSuper):
    """This element declares the content model for `Metadata`, which contains descriptions of authorities, data sources, measurement techniques, parameters, properties, material and component sources, specimens, and test conditions. `Metadata` is composed of the following elements.

    - `AuthorityDetails` contains a description of authorities referenced from the `Specification` and `Name` elements and may occur zero or more times within the `Metadata` element. For additional information, see the documentation for the `AuthorityDetails` element.
    - `DataSourceDetails` contains a description of a data source referenced using the `PropertyData` element and may occur zero or more times within the `Metadata` element. For additional information, see the documentation for the `DataSourceDetails` element.
    - `MeasurementTechniqueDetails` contains a description of a measurement technique referenced using the `PropertyData` element and may occur zero or more times within the `Metadata` element. For additional information, see the documentation for the `MeasurementTechniqueDetails` element.
    - `ParameterDetails` contains a description of a parameter referenced using the `PropertyData` element and may occur zero or more times within the `Metadata` element. For additional information, see the documentation for the `ParameterDetails` element.
    - `PropertyDetails` contains a description of a property for which materials data are encoded using the `PropertyData` element and may occur zero or more times within the `Metadata` element. For additional information, see the documentation for the Prope`r`tyDetails element.
    - `SourceDetails` contains a description of the source of a material or component referenced using the Source element and may occur zero or more times within the `Metadata` element. For additional information, see the documentation for the `SourceDetails` element.
    - `SpecimenDetails` contains a description of a specimen referenced using the `PropertyData` element and may occur zero or more times within the `Metadata` element. For additional information, see the documentation for the `SpecimenDetails` element.
    - `TestCondtionDetails` contains a description of the test condtion(s) referenced using the `PropertyData` element and may occur zero or more times within the `Metadata` element. For additional information, see the documentation for the `TestCondtionDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        AuthorityDetails: AuthorityDetails = None,
        DataSourceDetails: DataSourceDetails = None,
        MeasurementTechniqueDetails: MeasurementTechniqueDetails = None,
        ParameterDetails: ParameterDetails = None,
        PropertyDetails: PropertyDetails = None,
        SourceDetails: SourceDetails = None,
        SpecimenDetails: SpecimenDetails = None,
        TestConditionDetails: TestConditionDetails = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        if AuthorityDetails is None:
            self.AuthorityDetails = []
        else:
            self.AuthorityDetails = AuthorityDetails
        self.AuthorityDetails_nsprefix_ = None
        if DataSourceDetails is None:
            self.DataSourceDetails = []
        else:
            self.DataSourceDetails = DataSourceDetails
        self.DataSourceDetails_nsprefix_ = None
        if MeasurementTechniqueDetails is None:
            self.MeasurementTechniqueDetails = []
        else:
            self.MeasurementTechniqueDetails = MeasurementTechniqueDetails
        self.MeasurementTechniqueDetails_nsprefix_ = None
        if ParameterDetails is None:
            self.ParameterDetails = []
        else:
            self.ParameterDetails = ParameterDetails
        self.ParameterDetails_nsprefix_ = None
        if PropertyDetails is None:
            self.PropertyDetails = []
        else:
            self.PropertyDetails = PropertyDetails
        self.PropertyDetails_nsprefix_ = None
        if SourceDetails is None:
            self.SourceDetails = []
        else:
            self.SourceDetails = SourceDetails
        self.SourceDetails_nsprefix_ = None
        if SpecimenDetails is None:
            self.SpecimenDetails = []
        else:
            self.SpecimenDetails = SpecimenDetails
        self.SpecimenDetails_nsprefix_ = None
        if TestConditionDetails is None:
            self.TestConditionDetails = []
        else:
            self.TestConditionDetails = TestConditionDetails
        self.TestConditionDetails_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Metadata)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Metadata.subclass:
            return Metadata.subclass(*args_, **kwargs_)
        else:
            return Metadata(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_AuthorityDetails(self, id=None):
        if id is not None:
            for authority_details in self.get_AuthorityDetails():
                if authority_details.get_id() == id:
                    return authority_details
            return None
        return self.AuthorityDetails

    def set_AuthorityDetails(self, AuthorityDetails):
        self.AuthorityDetails = AuthorityDetails

    def add_AuthorityDetails(self, value):
        self.AuthorityDetails.append(value)

    def insert_AuthorityDetails_at(self, index, value):
        self.AuthorityDetails.insert(index, value)

    def replace_AuthorityDetails_at(self, index, value):
        self.AuthorityDetails[index] = value

    AuthorityDetailsProp = property(get_AuthorityDetails, set_AuthorityDetails)

    def get_DataSourceDetails(self, id=None):
        if id is not None:
            for data_source_details in self.get_DataSourceDetails():
                if data_source_details.get_id() == id:
                    return data_source_details
            return None
        return self.DataSourceDetails

    def set_DataSourceDetails(self, DataSourceDetails):
        self.DataSourceDetails = DataSourceDetails

    def add_DataSourceDetails(self, value):
        self.DataSourceDetails.append(value)

    def insert_DataSourceDetails_at(self, index, value):
        self.DataSourceDetails.insert(index, value)

    def replace_DataSourceDetails_at(self, index, value):
        self.DataSourceDetails[index] = value

    DataSourceDetailsProp = property(get_DataSourceDetails, set_DataSourceDetails)

    def get_MeasurementTechniqueDetails(self, id=None):
        if id is not None:
            for measurement_technique_details in self.get_MeasurementTechniqueDetails():
                if measurement_technique_details.get_id() == id:
                    return measurement_technique_details
            return None
        return self.MeasurementTechniqueDetails

    def set_MeasurementTechniqueDetails(self, MeasurementTechniqueDetails):
        self.MeasurementTechniqueDetails = MeasurementTechniqueDetails

    def add_MeasurementTechniqueDetails(self, value):
        self.MeasurementTechniqueDetails.append(value)

    def insert_MeasurementTechniqueDetails_at(self, index, value):
        self.MeasurementTechniqueDetails.insert(index, value)

    def replace_MeasurementTechniqueDetails_at(self, index, value):
        self.MeasurementTechniqueDetails[index] = value

    MeasurementTechniqueDetailsProp = property(
        get_MeasurementTechniqueDetails, set_MeasurementTechniqueDetails
    )

    def get_ParameterDetails(self, id=None):
        if id is not None:
            for parameter_details in self.get_ParameterDetails():
                if parameter_details.get_id() == id:
                    return parameter_details
            return None
        return self.ParameterDetails

    def set_ParameterDetails(self, ParameterDetails):
        self.ParameterDetails = ParameterDetails

    def add_ParameterDetails(self, value):
        self.ParameterDetails.append(value)

    def insert_ParameterDetails_at(self, index, value):
        self.ParameterDetails.insert(index, value)

    def replace_ParameterDetails_at(self, index, value):
        self.ParameterDetails[index] = value

    ParameterDetailsProp = property(get_ParameterDetails, set_ParameterDetails)

    def get_PropertyDetails(self, id=None):
        if id is not None:
            for property_details in self.get_PropertyDetails():
                if property_details.get_id() == id:
                    return property_details
            return None
        return self.PropertyDetails

    def set_PropertyDetails(self, PropertyDetails):
        self.PropertyDetails = PropertyDetails

    def add_PropertyDetails(self, value):
        self.PropertyDetails.append(value)

    def insert_PropertyDetails_at(self, index, value):
        self.PropertyDetails.insert(index, value)

    def replace_PropertyDetails_at(self, index, value):
        self.PropertyDetails[index] = value

    PropertyDetailsProp = property(get_PropertyDetails, set_PropertyDetails)

    def get_SourceDetails(self, id=None):
        if id is not None:
            for source_details in self.get_SourceDetails():
                if source_details.get_id() == id:
                    return source_details
            return None
        return self.SourceDetails

    def set_SourceDetails(self, SourceDetails):
        self.SourceDetails = SourceDetails

    def add_SourceDetails(self, value):
        self.SourceDetails.append(value)

    def insert_SourceDetails_at(self, index, value):
        self.SourceDetails.insert(index, value)

    def replace_SourceDetails_at(self, index, value):
        self.SourceDetails[index] = value

    SourceDetailsProp = property(get_SourceDetails, set_SourceDetails)

    def get_SpecimenDetails(self, id=None):
        if id is not None:
            for specimen_details in self.get_SpecimenDetails():
                if specimen_details.get_id() == id:
                    return specimen_details
            return None
        return self.SpecimenDetails

    def set_SpecimenDetails(self, SpecimenDetails):
        self.SpecimenDetails = SpecimenDetails

    def add_SpecimenDetails(self, value):
        self.SpecimenDetails.append(value)

    def insert_SpecimenDetails_at(self, index, value):
        self.SpecimenDetails.insert(index, value)

    def replace_SpecimenDetails_at(self, index, value):
        self.SpecimenDetails[index] = value

    SpecimenDetailsProp = property(get_SpecimenDetails, set_SpecimenDetails)

    def get_TestConditionDetails(self, id=None):
        if id is not None:
            for test_condition_details in self.get_TestConditionDetails():
                if test_condition_details.get_id() == id:
                    return test_condition_details
            return None
        return self.TestConditionDetails

    def set_TestConditionDetails(self, TestConditionDetails):
        self.TestConditionDetails = TestConditionDetails

    def add_TestConditionDetails(self, value):
        self.TestConditionDetails.append(value)

    def insert_TestConditionDetails_at(self, index, value):
        self.TestConditionDetails.insert(index, value)

    def replace_TestConditionDetails_at(self, index, value):
        self.TestConditionDetails[index] = value

    TestConditionDetailsProp = property(
        get_TestConditionDetails, set_TestConditionDetails
    )

    def has__content(self):
        if (
            self.AuthorityDetails
            or self.DataSourceDetails
            or self.MeasurementTechniqueDetails
            or self.ParameterDetails
            or self.PropertyDetails
            or self.SourceDetails
            or self.SpecimenDetails
            or self.TestConditionDetails
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Metadata",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Metadata")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Metadata":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Metadata"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Metadata",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Metadata"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Metadata",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for AuthorityDetails_ in self.AuthorityDetails:
            namespaceprefix_ = (
                self.AuthorityDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.AuthorityDetails_nsprefix_)
                else ""
            )
            AuthorityDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="AuthorityDetails",
                pretty_print=pretty_print,
            )
        for DataSourceDetails_ in self.DataSourceDetails:
            namespaceprefix_ = (
                self.DataSourceDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.DataSourceDetails_nsprefix_)
                else ""
            )
            DataSourceDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="DataSourceDetails",
                pretty_print=pretty_print,
            )
        for MeasurementTechniqueDetails_ in self.MeasurementTechniqueDetails:
            namespaceprefix_ = (
                self.MeasurementTechniqueDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.MeasurementTechniqueDetails_nsprefix_)
                else ""
            )
            MeasurementTechniqueDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="MeasurementTechniqueDetails",
                pretty_print=pretty_print,
            )
        for ParameterDetails_ in self.ParameterDetails:
            namespaceprefix_ = (
                self.ParameterDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ParameterDetails_nsprefix_)
                else ""
            )
            ParameterDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ParameterDetails",
                pretty_print=pretty_print,
            )
        for PropertyDetails_ in self.PropertyDetails:
            namespaceprefix_ = (
                self.PropertyDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.PropertyDetails_nsprefix_)
                else ""
            )
            PropertyDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="PropertyDetails",
                pretty_print=pretty_print,
            )
        for SourceDetails_ in self.SourceDetails:
            namespaceprefix_ = (
                self.SourceDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.SourceDetails_nsprefix_)
                else ""
            )
            SourceDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="SourceDetails",
                pretty_print=pretty_print,
            )
        for SpecimenDetails_ in self.SpecimenDetails:
            namespaceprefix_ = (
                self.SpecimenDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.SpecimenDetails_nsprefix_)
                else ""
            )
            SpecimenDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="SpecimenDetails",
                pretty_print=pretty_print,
            )
        for TestConditionDetails_ in self.TestConditionDetails:
            namespaceprefix_ = (
                self.TestConditionDetails_nsprefix_ + ":"
                if (UseCapturedNS_ and self.TestConditionDetails_nsprefix_)
                else ""
            )
            TestConditionDetails_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="TestConditionDetails",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "AuthorityDetails":
            obj_ = AuthorityDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AuthorityDetails.append(obj_)
            obj_.original_tagname_ = "AuthorityDetails"
        elif nodeName_ == "DataSourceDetails":
            obj_ = DataSourceDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DataSourceDetails.append(obj_)
            obj_.original_tagname_ = "DataSourceDetails"
        elif nodeName_ == "MeasurementTechniqueDetails":
            obj_ = MeasurementTechniqueDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.MeasurementTechniqueDetails.append(obj_)
            obj_.original_tagname_ = "MeasurementTechniqueDetails"
        elif nodeName_ == "ParameterDetails":
            obj_ = ParameterDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterDetails.append(obj_)
            obj_.original_tagname_ = "ParameterDetails"
        elif nodeName_ == "PropertyDetails":
            obj_ = PropertyDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PropertyDetails.append(obj_)
            obj_.original_tagname_ = "PropertyDetails"
        elif nodeName_ == "SourceDetails":
            obj_ = SourceDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SourceDetails.append(obj_)
            obj_.original_tagname_ = "SourceDetails"
        elif nodeName_ == "SpecimenDetails":
            obj_ = SpecimenDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.SpecimenDetails.append(obj_)
            obj_.original_tagname_ = "SpecimenDetails"
        elif nodeName_ == "TestConditionDetails":
            obj_ = TestConditionDetails.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TestConditionDetails.append(obj_)
            obj_.original_tagname_ = "TestConditionDetails"


class Name(GeneratedsSuper):
    """This element declares the content model for `Name`, which contains a string representing a name and has one optional attribute, `authority`, for identifying an authoritative source of names in the context in which the `Name` element is used."""

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self, authority: str = None, valueOf_=None, gds_collector_=None, **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.authority = _cast(None, authority)
        self.authority_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Name)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Name.subclass:
            return Name.subclass(*args_, **kwargs_)
        else:
            return Name(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_authority(self):
        return self.authority

    def set_authority(self, authority):
        self.authority = authority

    authorityProp = property(get_authority, set_authority)

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        self.valueOf_ = valueOf_

    def has__content(self):
        if 1 if type(self.valueOf_) in [int, float] else self.valueOf_:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Name",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Name")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Name":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Name"
        )
        outfile.write(">")
        self._exportChildren(
            outfile,
            level + 1,
            namespaceprefix_,
            namespacedef_,
            name_,
            pretty_print=pretty_print,
        )
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Name"
    ):
        if self.authority is not None and "authority" not in already_processed:
            already_processed.add("authority")
            outfile.write(
                " authority=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.authority), input_name="authority"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Name",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("authority", node)
        if value is not None and "authority" not in already_processed:
            already_processed.add("authority")
            self.authority = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


class ParameterValue(GeneratedsSuper):
    """This element declares the content model for `ParameterValue`, which contains the value of a parameter. `ParameterValue` has two required attributes.

    1. The first attribute, `parameter`, references an id attribute specified in a `ParameterDetails` element so that the descriptive details of the parameter are tied to the value.
    2. The second attribute, `format`, indicates the format of the value.  If used, "mixed" indicates that the not all of the parameter values are of the same type (e.g. a "No Break" value for an otherwise numeric set of Charpy Izod test results).  If used, then the "format" attribute on each "Data" item should be individually set.

    `ParameterValue` is composed of the following elements.

    - `Data` contains the property data and has one required attribute, format, for indicating the format of the data. `Data` must occur once and only once within the `ParameterValue` element.
    - `Qualifier` contains any qualifier(s) pertinent to the data in `ParameterValue` (e.g. "min," "max," etc.) and may occur zero or more times within the `PropertyData` element.
    - `Uncertainty` contains the measurement uncertainty(ies) of the data in `ParameterValue` and may occur once or not at all within the `ParameterValue` element. For additional information, see the documentation for the `Uncertainty` element.
    - `Notes` contains any additional information concerning the property data and may occur once or not at all within the `PropertyData` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        parameter: str = None,
        format: DataFormat = None,
        Data: DataType = None,
        Uncertainty: Uncertainty = None,
        Qualifier: str = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.parameter = _cast(None, parameter)
        self.parameter_nsprefix_ = None
        self.format = _cast(None, format)
        self.format_nsprefix_ = None
        self.Data = Data
        self.Data_nsprefix_ = None
        if Uncertainty is None:
            self.Uncertainty = []
        else:
            self.Uncertainty = Uncertainty
        self.Uncertainty_nsprefix_ = None
        if Qualifier is None:
            self.Qualifier = []
        else:
            self.Qualifier = Qualifier
        self.Qualifier_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, ParameterValue)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterValue.subclass:
            return ParameterValue.subclass(*args_, **kwargs_)
        else:
            return ParameterValue(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Data(self):
        return self.Data

    def set_Data(self, Data):
        self.Data = Data

    DataProp = property(get_Data, set_Data)

    def get_Uncertainty(self):
        return self.Uncertainty

    def set_Uncertainty(self, Uncertainty):
        self.Uncertainty = Uncertainty

    def add_Uncertainty(self, value):
        self.Uncertainty.append(value)

    def insert_Uncertainty_at(self, index, value):
        self.Uncertainty.insert(index, value)

    def replace_Uncertainty_at(self, index, value):
        self.Uncertainty[index] = value

    UncertaintyProp = property(get_Uncertainty, set_Uncertainty)

    def get_Qualifier(self):
        return self.Qualifier

    def set_Qualifier(self, Qualifier):
        self.Qualifier = Qualifier

    def add_Qualifier(self, value):
        self.Qualifier.append(value)

    def insert_Qualifier_at(self, index, value):
        self.Qualifier.insert(index, value)

    def replace_Qualifier_at(self, index, value):
        self.Qualifier[index] = value

    QualifierProp = property(get_Qualifier, set_Qualifier)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_parameter(self):
        return self.parameter

    def set_parameter(self, parameter):
        self.parameter = parameter

    parameterProp = property(get_parameter, set_parameter)

    def get_format(self):
        return self.format

    def set_format(self, format):
        self.format = format

    formatProp = property(get_format, set_format)

    def validate_Qualifier(self, value):
        result = True
        # Validate type Qualifier, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_DataFormat(self, value):
        # Validate type DataFormat, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            value = value
            enumerations = ["float", "integer", "string", "exponential", "mixed"]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DataFormat'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def has__content(self):
        if (
            self.Data is not None
            or self.Uncertainty
            or self.Qualifier
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ParameterValue",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("ParameterValue")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "ParameterValue":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="ParameterValue"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="ParameterValue",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="ParameterValue",
    ):
        if self.parameter is not None and "parameter" not in already_processed:
            already_processed.add("parameter")
            outfile.write(
                " parameter=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.parameter), input_name="parameter"
                        )
                    ),
                )
            )
        if self.format is not None and "format" not in already_processed:
            already_processed.add("format")
            outfile.write(
                " format=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.format), input_name="format"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ParameterValue",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Data is not None:
            namespaceprefix_ = (
                self.Data_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Data_nsprefix_)
                else ""
            )
            self.Data.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Data",
                pretty_print=pretty_print,
            )
        for Uncertainty_ in self.Uncertainty:
            namespaceprefix_ = (
                self.Uncertainty_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Uncertainty_nsprefix_)
                else ""
            )
            Uncertainty_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Uncertainty",
                pretty_print=pretty_print,
            )
        for Qualifier_ in self.Qualifier:
            namespaceprefix_ = (
                self.Qualifier_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Qualifier_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sQualifier>%s</%sQualifier>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(Qualifier_), input_name="Qualifier"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("parameter", node)
        if value is not None and "parameter" not in already_processed:
            already_processed.add("parameter")
            self.parameter = value
        value = find_attr_value_("format", node)
        if value is not None and "format" not in already_processed:
            already_processed.add("format")
            self.format = value
            self.validate_DataFormat(self.format)  # validate type DataFormat

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Data":
            obj_ = DataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Data = obj_
            obj_.original_tagname_ = "Data"
        elif nodeName_ == "Uncertainty":
            obj_ = Uncertainty.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Uncertainty.append(obj_)
            obj_.original_tagname_ = "Uncertainty"
        elif nodeName_ == "Qualifier":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Qualifier")
            value_ = self.gds_validate_string(value_, node, "Qualifier")
            self.Qualifier.append(value_)
            self.Qualifier_nsprefix_ = child_.prefix
            # validate type Qualifier
            self.validate_Qualifier(self.Qualifier[-1])
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class PhaseComposition(GeneratedsSuper):
    """This element declares the content model for `PhaseComposition`, which contains a description of a phase that comprises the bulk material or component and is composed of the following elements.

    - `Name` contains the name of the phase and has one optional attribute, authority, for identifying an authoritative source of phase names. `Name` must occur once and only once within the `PhaseComposition` element.
    - `Concentration` contains the concentration of the phase and may occur once or not at all within the `PhaseComposition` element. For additional information, see the documentation for the `Concentration` element.
    - `PropertyData` contains property data for the phase and may occur zero or more times within the `PhaseComposition` element. For additional information, see the documentation for the `PropertyData` element.
    - `Notes` contains any additional information concerning the phase and may occur once or not at all within the `PhaseComposition` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Name: Name = None,
        Concentration: Concentration = None,
        PropertyData: PropertyData = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Concentration = Concentration
        self.Concentration_nsprefix_ = None
        if PropertyData is None:
            self.PropertyData = []
        else:
            self.PropertyData = PropertyData
        self.PropertyData_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, PhaseComposition)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PhaseComposition.subclass:
            return PhaseComposition.subclass(*args_, **kwargs_)
        else:
            return PhaseComposition(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Concentration(self):
        return self.Concentration

    def set_Concentration(self, Concentration):
        self.Concentration = Concentration

    ConcentrationProp = property(get_Concentration, set_Concentration)

    def get_PropertyData(self, property=None):
        if property is not None:
            properties = []
            for property_data in self.get_PropertyData():
                if property_data.get_property() == property:
                    properties.append(property_data)
            return properties
        return self.PropertyData

    def set_PropertyData(self, PropertyData):
        self.PropertyData = PropertyData

    def add_PropertyData(self, value):
        self.PropertyData.append(value)

    def insert_PropertyData_at(self, index, value):
        self.PropertyData.insert(index, value)

    def replace_PropertyData_at(self, index, value):
        self.PropertyData[index] = value

    PropertyDataProp = property(get_PropertyData, set_PropertyData)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Name is not None
            or self.Concentration is not None
            or self.PropertyData
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="PhaseComposition",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("PhaseComposition")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "PhaseComposition":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="PhaseComposition",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="PhaseComposition",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="PhaseComposition",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="PhaseComposition",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Concentration is not None:
            namespaceprefix_ = (
                self.Concentration_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Concentration_nsprefix_)
                else ""
            )
            self.Concentration.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Concentration",
                pretty_print=pretty_print,
            )
        for PropertyData_ in self.PropertyData:
            namespaceprefix_ = (
                self.PropertyData_nsprefix_ + ":"
                if (UseCapturedNS_ and self.PropertyData_nsprefix_)
                else ""
            )
            PropertyData_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="PropertyData",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Concentration":
            obj_ = Concentration.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Concentration = obj_
            obj_.original_tagname_ = "Concentration"
        elif nodeName_ == "PropertyData":
            obj_ = PropertyData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PropertyData.append(obj_)
            obj_.original_tagname_ = "PropertyData"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class ProcessingDetails(GeneratedsSuper):
    """This element declares the content model for `ProcessingDetails`, which contains a description of a processing step for the bulk material or component. `ProcessingDetails` is composed of the following elements.

    - `Name` contains the name of the processing step and has one optional attribute, `authority`, for identifying an authoritative source of processing step names. Name must occur once and only once within the `ProcessingDetails` element.
    - `ParameterValue` contains the value of a parameter under which the processing step occurred and may occur zero or more times within the `ProcessingDetails` element. For additional information, see the documentation for the `ParameterValue` element.
    - `Result` is a string that contains a description of the outcome or result of the processing step and may occur once or not at all within the `ProcessingDetails` element.
    - `Notes` contains any additional information concerning the processing step and may occur once or not at all within the `ProcessingDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        Name: Name = None,
        ParameterValue: ParameterValue = None,
        Result: str = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        if ParameterValue is None:
            self.ParameterValue = []
        else:
            self.ParameterValue = ParameterValue
        self.ParameterValue_nsprefix_ = None
        self.Result = Result
        self.Result_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, ProcessingDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ProcessingDetails.subclass:
            return ProcessingDetails.subclass(*args_, **kwargs_)
        else:
            return ProcessingDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_ParameterValue(self, parameter=None):
        if parameter is not None:
            parameters = []
            for parameter_value in self.get_ParameterValue():
                if parameter_value.get_property() == property:
                    parameters.append(parameter_value)
            return parameters
        return self.ParameterValue

    def set_ParameterValue(self, ParameterValue):
        self.ParameterValue = ParameterValue

    def add_ParameterValue(self, value):
        self.ParameterValue.append(value)

    def insert_ParameterValue_at(self, index, value):
        self.ParameterValue.insert(index, value)

    def replace_ParameterValue_at(self, index, value):
        self.ParameterValue[index] = value

    ParameterValueProp = property(get_ParameterValue, set_ParameterValue)

    def get_Result(self):
        return self.Result

    def set_Result(self, Result):
        self.Result = Result

    ResultProp = property(get_Result, set_Result)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Name is not None
            or self.ParameterValue
            or self.Result is not None
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ProcessingDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("ProcessingDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "ProcessingDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="ProcessingDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="ProcessingDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="ProcessingDetails",
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ProcessingDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        for ParameterValue_ in self.ParameterValue:
            namespaceprefix_ = (
                self.ParameterValue_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ParameterValue_nsprefix_)
                else ""
            )
            ParameterValue_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ParameterValue",
                pretty_print=pretty_print,
            )
        if self.Result is not None:
            namespaceprefix_ = (
                self.Result_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Result_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sResult>%s</%sResult>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Result), input_name="Result"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "ParameterValue":
            obj_ = ParameterValue.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterValue.append(obj_)
            obj_.original_tagname_ = "ParameterValue"
        elif nodeName_ == "Result":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Result")
            value_ = self.gds_validate_string(value_, node, "Result")
            self.Result = value_
            self.Result_nsprefix_ = child_.prefix
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class PropertyData(GeneratedsSuper):
    """This element declares the content model for `PropertyData`, which contains property data. `PropertyData` has seven attributes.

    1. The first attribute, `property`, is required and references an id attribute specified in a `PropertyDetails` element so that the descriptive details for the property are tied to the data found in the `Data` element.
    2. The second attribute, `technique`, is optional and references an id attribute Specified in a `MeasurementTechniqueDetails` element so that the Descriptive details for the measurement technique are tied to the data found In the `Data` element.
    3. The third attribute, `source`, is optional and references an id attribute specified in a `DataSourceDetails` element so that the descriptive details for the data source are tied to the data found in the `Data` element.
    4. The fourth attribute, `specimen`, is optional and references an id attribute specified in a `SpecimenDetails` element so that the descriptive details for the specimen are tied to the data found in the `Data` element.
    5. The fifth attribute, `test`, is optional and references an id attribute specified in a `TestCondtionDetails` element so that the descriptive details for the test condition(s) are tied to the data found in the `Data` element.
    6. The sixth attribute, `delimiter`, specifies the delimiter that separates multiple values in the `Data`, `Qualifier`, `Uncertainty`, and `ParameterValue` elements.  The default value is a comma (',').
    7. The seventh attribute, `quote`, specifies the string that is used to quote values in the `Data`, `Qualifier`, `Uncertainty` and `ParameterValue` elements.  The default value is a null string, which is equivalent to saying that the values are not quoted.

    `PropertyData` is composed of the following elements.

    - `Data` contains the property data and has one required attribute, `format`, for indicating the format of the data. `Data` must occur once and only once within the `PropertyData` element.
    - `Qualifier` contains any qualifier(s) pertinent to the data in Data (e.g. "min," "max," etc.) and may occur once or not at all within the `PropertyData` element.
    - `Uncertainty` contains the measurement uncertainty(ies) of the data in `Data` and may occur once or not at all within the `PropertyData` element. For additional information, see the documentation for the Uncertainty element.
    - `ParameterValue` contains the value(s) of a parameter under which the data were determined and may occur zero or more times within the `PropertyData` element. For additional information, see the documentation for the `ParameterValue` element.
    - `Notes` contains any additional information concerning the property data and may occur once or not at all within the `PropertyData` element.

    Note -	Multiple entries in the `Data`, `Qualifier`, `UncertaintyValue`, and `ParameterValue` elements must be comma delimited and synchronized across elements, i.e., the number of entries in each of these four elements must be equal.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        property: str = None,
        technique: str = None,
        source: str = None,
        specimen: str = None,
        test: str = None,
        delimiter: str = ",",
        quote: str = None,
        Data: DataType = None,
        Uncertainty: Uncertainty = None,
        Qualifier: str = None,
        ParameterValue: ParameterValue = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.property = _cast(None, property)
        self.property_nsprefix_ = None
        self.technique = _cast(None, technique)
        self.technique_nsprefix_ = None
        self.source = _cast(None, source)
        self.source_nsprefix_ = None
        self.specimen = _cast(None, specimen)
        self.specimen_nsprefix_ = None
        self.test = _cast(None, test)
        self.test_nsprefix_ = None
        self.delimiter = _cast(None, delimiter)
        self.delimiter_nsprefix_ = None
        self.quote = _cast(None, quote)
        self.quote_nsprefix_ = None
        self.Data = Data
        self.Data_nsprefix_ = None
        if Uncertainty is None:
            self.Uncertainty = []
        else:
            self.Uncertainty = Uncertainty
        self.Uncertainty_nsprefix_ = None
        if Qualifier is None:
            self.Qualifier = []
        else:
            self.Qualifier = Qualifier
        self.Qualifier_nsprefix_ = None
        if ParameterValue is None:
            self.ParameterValue = []
        else:
            self.ParameterValue = ParameterValue
        self.ParameterValue_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, PropertyData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PropertyData.subclass:
            return PropertyData.subclass(*args_, **kwargs_)
        else:
            return PropertyData(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Data(self):
        return self.Data

    def set_Data(self, Data):
        self.Data = Data

    DataProp = property(get_Data, set_Data)

    def get_Uncertainty(self):
        return self.Uncertainty

    def set_Uncertainty(self, Uncertainty):
        self.Uncertainty = Uncertainty

    def add_Uncertainty(self, value):
        self.Uncertainty.append(value)

    def insert_Uncertainty_at(self, index, value):
        self.Uncertainty.insert(index, value)

    def replace_Uncertainty_at(self, index, value):
        self.Uncertainty[index] = value

    UncertaintyProp = property(get_Uncertainty, set_Uncertainty)

    def get_Qualifier(self):
        return self.Qualifier

    def set_Qualifier(self, Qualifier):
        self.Qualifier = Qualifier

    def add_Qualifier(self, value):
        self.Qualifier.append(value)

    def insert_Qualifier_at(self, index, value):
        self.Qualifier.insert(index, value)

    def replace_Qualifier_at(self, index, value):
        self.Qualifier[index] = value

    QualifierProp = property(get_Qualifier, set_Qualifier)

    def get_ParameterValue(self, parameter=None):
        if parameter is not None:
            parameters = []
            for parameter_value in self.get_ParameterValue():
                if parameter_value.get_property() == property:
                    parameters.append(parameter_value)
            return parameters
        return self.ParameterValue

    def set_ParameterValue(self, ParameterValue):
        self.ParameterValue = ParameterValue

    def add_ParameterValue(self, value):
        self.ParameterValue.append(value)

    def insert_ParameterValue_at(self, index, value):
        self.ParameterValue.insert(index, value)

    def replace_ParameterValue_at(self, index, value):
        self.ParameterValue[index] = value

    ParameterValueProp = property(get_ParameterValue, set_ParameterValue)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_property(self):
        return self.property

    def set_property(self, property):
        self.property = property

    propertyProp = property(get_property, set_property)

    def get_technique(self):
        return self.technique

    def set_technique(self, technique):
        self.technique = technique

    techniqueProp = property(get_technique, set_technique)

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source

    sourceProp = property(get_source, set_source)

    def get_specimen(self):
        return self.specimen

    def set_specimen(self, specimen):
        self.specimen = specimen

    specimenProp = property(get_specimen, set_specimen)

    def get_test(self):
        return self.test

    def set_test(self, test):
        self.test = test

    testProp = property(get_test, set_test)

    def get_delimiter(self):
        return self.delimiter

    def set_delimiter(self, delimiter):
        self.delimiter = delimiter

    delimiterProp = property(get_delimiter, set_delimiter)

    def get_quote(self):
        return self.quote

    def set_quote(self, quote):
        self.quote = quote

    quoteProp = property(get_quote, set_quote)

    def validate_Qualifier(self, value):
        result = True
        # Validate type Qualifier, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_delimiterType(self, value):
        # Validate type delimiterType, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd minLength restriction on delimiterType'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def has__content(self):
        if (
            self.Data is not None
            or self.Uncertainty
            or self.Qualifier
            or self.ParameterValue
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="PropertyData",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("PropertyData")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "PropertyData":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="PropertyData"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="PropertyData",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="PropertyData",
    ):
        if self.property is not None and "property" not in already_processed:
            already_processed.add("property")
            outfile.write(
                " property=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.property), input_name="property"
                        )
                    ),
                )
            )
        if self.technique is not None and "technique" not in already_processed:
            already_processed.add("technique")
            outfile.write(
                " technique=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.technique), input_name="technique"
                        )
                    ),
                )
            )
        if self.source is not None and "source" not in already_processed:
            already_processed.add("source")
            outfile.write(
                " source=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.source), input_name="source"
                        )
                    ),
                )
            )
        if self.specimen is not None and "specimen" not in already_processed:
            already_processed.add("specimen")
            outfile.write(
                " specimen=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.specimen), input_name="specimen"
                        )
                    ),
                )
            )
        if self.test is not None and "test" not in already_processed:
            already_processed.add("test")
            outfile.write(
                " test=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.test), input_name="test"
                        )
                    ),
                )
            )
        if self.delimiter != "," and "delimiter" not in already_processed:
            already_processed.add("delimiter")
            outfile.write(
                " delimiter=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.delimiter), input_name="delimiter"
                        )
                    ),
                )
            )
        if self.quote is not None and "quote" not in already_processed:
            already_processed.add("quote")
            outfile.write(
                " quote=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.quote), input_name="quote"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="PropertyData",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Data is not None:
            namespaceprefix_ = (
                self.Data_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Data_nsprefix_)
                else ""
            )
            self.Data.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Data",
                pretty_print=pretty_print,
            )
        for Uncertainty_ in self.Uncertainty:
            namespaceprefix_ = (
                self.Uncertainty_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Uncertainty_nsprefix_)
                else ""
            )
            Uncertainty_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Uncertainty",
                pretty_print=pretty_print,
            )
        for Qualifier_ in self.Qualifier:
            namespaceprefix_ = (
                self.Qualifier_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Qualifier_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sQualifier>%s</%sQualifier>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(Qualifier_), input_name="Qualifier"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        for ParameterValue_ in self.ParameterValue:
            namespaceprefix_ = (
                self.ParameterValue_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ParameterValue_nsprefix_)
                else ""
            )
            ParameterValue_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ParameterValue",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("property", node)
        if value is not None and "property" not in already_processed:
            already_processed.add("property")
            self.property = value
        value = find_attr_value_("technique", node)
        if value is not None and "technique" not in already_processed:
            already_processed.add("technique")
            self.technique = value
        value = find_attr_value_("source", node)
        if value is not None and "source" not in already_processed:
            already_processed.add("source")
            self.source = value
        value = find_attr_value_("specimen", node)
        if value is not None and "specimen" not in already_processed:
            already_processed.add("specimen")
            self.specimen = value
        value = find_attr_value_("test", node)
        if value is not None and "test" not in already_processed:
            already_processed.add("test")
            self.test = value
        value = find_attr_value_("delimiter", node)
        if value is not None and "delimiter" not in already_processed:
            already_processed.add("delimiter")
            self.delimiter = value
            self.validate_delimiterType(self.delimiter)  # validate type delimiterType
        value = find_attr_value_("quote", node)
        if value is not None and "quote" not in already_processed:
            already_processed.add("quote")
            self.quote = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Data":
            obj_ = DataType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Data = obj_
            obj_.original_tagname_ = "Data"
        elif nodeName_ == "Uncertainty":
            obj_ = Uncertainty.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Uncertainty.append(obj_)
            obj_.original_tagname_ = "Uncertainty"
        elif nodeName_ == "Qualifier":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Qualifier")
            value_ = self.gds_validate_string(value_, node, "Qualifier")
            self.Qualifier.append(value_)
            self.Qualifier_nsprefix_ = child_.prefix
            # validate type Qualifier
            self.validate_Qualifier(self.Qualifier[-1])
        elif nodeName_ == "ParameterValue":
            obj_ = ParameterValue.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterValue.append(obj_)
            obj_.original_tagname_ = "ParameterValue"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class Source(GeneratedsSuper):
    """This element declares the content model for `Source`, which contains an `id` attribute specified in a `SourceDetails` element representing the source of the bulk material or component."""

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, source: str = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.source = _cast(None, source)
        self.source_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Source)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Source.subclass:
            return Source.subclass(*args_, **kwargs_)
        else:
            return Source(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source

    sourceProp = property(get_source, set_source)

    def has__content(self):
        if ():
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Source",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Source")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Source":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Source"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Source",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Source"
    ):
        if self.source is not None and "source" not in already_processed:
            already_processed.add("source")
            outfile.write(
                " source=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.source), input_name="source"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Source",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("source", node)
        if value is not None and "source" not in already_processed:
            already_processed.add("source")
            self.source = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


class Specification(GeneratedsSuper):
    """This element declares the content model for `Specification`, which contains a string representing the specification for the bulk material or component and has one optional attribute, `authority`, for identifying an authoritative source of specifications."""

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self, authority: str = None, valueOf_=None, gds_collector_=None, **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.authority = _cast(None, authority)
        self.authority_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Specification)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Specification.subclass:
            return Specification.subclass(*args_, **kwargs_)
        else:
            return Specification(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_authority(self):
        return self.authority

    def set_authority(self, authority):
        self.authority = authority

    authorityProp = property(get_authority, set_authority)

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        self.valueOf_ = valueOf_

    def has__content(self):
        if 1 if type(self.valueOf_) in [int, float] else self.valueOf_:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Specification",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Specification")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Specification":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Specification"
        )
        outfile.write(">")
        self._exportChildren(
            outfile,
            level + 1,
            namespaceprefix_,
            namespacedef_,
            name_,
            pretty_print=pretty_print,
        )
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="Specification",
    ):
        if self.authority is not None and "authority" not in already_processed:
            already_processed.add("authority")
            outfile.write(
                " authority=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.authority), input_name="authority"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Specification",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("authority", node)
        if value is not None and "authority" not in already_processed:
            already_processed.add("authority")
            self.authority = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


class Uncertainty(GeneratedsSuper):
    """This element declares the content model for `Uncertainty`, which contains a description of the measurement uncertainty of the data.

    `Uncertainty` has 1 optional attributes:

    1. `Name` is a description of the nature of the uncertainty value, for example '6 sigma', 'Gaussian' or '2 std dev.'

    Uncertainty is composed of the following elements.

    - `Value` contains the value of the uncertainty and has one required attribute, format, for indicating the format of the value. `Value` must occur once and only once within the `Uncertainty` element.
    - `Units` contains the units for the value of the uncertainty and must occur once and only once within the `Uncertainty` element. For additional information, see the documentation for the `Units` element.
    - `Percentile` is a value indicating the percentage of the data population that have values less than or equal to that expressed by the `Uncertainty` value.  `Percentile` can occur zero or more times.  If `Percentile` is not given then `Value` is interpreted as being an equal and unspecified deviation above and below the property value(s). An uncertainty of 2 standard deviations below  the mean for a normally distributed dataset would have a uncertainty percentile of 5%, and 2 standard deviations above the mean would be 95%.
    - `Notes` contains any additional information concerning the uncertainty, such as a description of the evaluation of the uncertainty, and may occur once or not at all within the `Uncertainty` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        DistributionType: str = "Normal/Gaussian",
        Num_Std_Dev: float = 2,
        Percentile: float = None,
        ConfidenceLevel: float = None,
        Value: str = None,
        Units: Units = None,
        Unitless: Unitless = None,
        Notes: str = None,
        Scale="Linear",
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.DistributionType = _cast(None, DistributionType)
        self.DistributionType_nsprefix_ = None
        self.Num_Std_Dev = _cast(float, Num_Std_Dev)
        self.Num_Std_Dev_nsprefix_ = None
        self.Percentile = _cast(float, Percentile)
        self.Percentile_nsprefix_ = None
        self.ConfidenceLevel = _cast(float, ConfidenceLevel)
        self.ConfidenceLevel_nsprefix_ = None
        self.Value = Value
        self.Value_nsprefix_ = None
        self.Units = Units
        self.Units_nsprefix_ = None
        self.Unitless = Unitless
        self.Unitless_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None
        self.Scale = Scale
        self.validate_ScaleType(self.Scale)
        self.Scale_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Uncertainty)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Uncertainty.subclass:
            return Uncertainty.subclass(*args_, **kwargs_)
        else:
            return Uncertainty(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Value(self):
        return self.Value

    def set_Value(self, Value):
        self.Value = Value

    ValueProp = property(get_Value, set_Value)

    def get_Units(self):
        return self.Units

    def set_Units(self, Units):
        self.Units = Units

    UnitsProp = property(get_Units, set_Units)

    def get_Unitless(self):
        return self.Unitless

    def set_Unitless(self, Unitless):
        self.Unitless = Unitless

    UnitlessProp = property(get_Unitless, set_Unitless)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_Scale(self):
        return self.Scale

    def set_Scale(self, Scale):
        self.Scale = Scale

    ScaleProp = property(get_Scale, set_Scale)

    def get_DistributionType(self):
        return self.DistributionType

    def set_DistributionType(self, DistributionType):
        self.DistributionType = DistributionType

    DistributionTypeProp = property(get_DistributionType, set_DistributionType)

    def get_Num_Std_Dev(self):
        return self.Num_Std_Dev

    def set_Num_Std_Dev(self, Num_Std_Dev):
        self.Num_Std_Dev = Num_Std_Dev

    Num_Std_DevProp = property(get_Num_Std_Dev, set_Num_Std_Dev)

    def get_Percentile(self):
        return self.Percentile

    def set_Percentile(self, Percentile):
        self.Percentile = Percentile

    PercentileProp = property(get_Percentile, set_Percentile)

    def get_ConfidenceLevel(self):
        return self.ConfidenceLevel

    def set_ConfidenceLevel(self, ConfidenceLevel):
        self.ConfidenceLevel = ConfidenceLevel

    ConfidenceLevelProp = property(get_ConfidenceLevel, set_ConfidenceLevel)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def validate_ScaleType(self, value):
        result = True
        # Validate type ScaleType, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            value = value
            enumerations = ["Linear", "Logarithmic"]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ScaleType'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
        return result

    def has__content(self):
        if (
            self.Value is not None
            or self.Units is not None
            or self.Unitless is not None
            or self.Notes is not None
            or self.Scale != "Linear"
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Uncertainty",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Uncertainty")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Uncertainty":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Uncertainty"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Uncertainty",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="Uncertainty",
    ):
        if (
            self.DistributionType != "Normal/Gaussian"
            and "DistributionType" not in already_processed
        ):
            already_processed.add("DistributionType")
            outfile.write(
                " DistributionType=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.DistributionType),
                            input_name="DistributionType",
                        )
                    ),
                )
            )
        if self.Num_Std_Dev != 2 and "Num_Std_Dev" not in already_processed:
            already_processed.add("Num_Std_Dev")
            outfile.write(
                ' Num_Std_Dev="%s"'
                % self.gds_format_float(self.Num_Std_Dev, input_name="Num_Std_Dev")
            )
        if self.Percentile is not None and "Percentile" not in already_processed:
            already_processed.add("Percentile")
            outfile.write(
                ' Percentile="%s"'
                % self.gds_format_float(self.Percentile, input_name="Percentile")
            )
        if (
            self.ConfidenceLevel is not None
            and "ConfidenceLevel" not in already_processed
        ):
            already_processed.add("ConfidenceLevel")
            outfile.write(
                ' ConfidenceLevel="%s"'
                % self.gds_format_float(
                    self.ConfidenceLevel, input_name="ConfidenceLevel"
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Uncertainty",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Value is not None:
            namespaceprefix_ = (
                self.Value_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Value_nsprefix_)
                else ""
            )
            self.Value.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Value",
                pretty_print=pretty_print,
            )
        if self.Units is not None:
            namespaceprefix_ = (
                self.Units_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Units_nsprefix_)
                else ""
            )
            self.Units.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Units",
                pretty_print=pretty_print,
            )
        if self.Unitless is not None:
            namespaceprefix_ = (
                self.Unitless_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Unitless_nsprefix_)
                else ""
            )
            self.Unitless.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Unitless",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Scale != "Linear":
            namespaceprefix_ = (
                self.Scale_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Scale_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sScale>%s</%sScale>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Scale), input_name="Scale"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("DistributionType", node)
        if value is not None and "DistributionType" not in already_processed:
            already_processed.add("DistributionType")
            self.DistributionType = value
        value = find_attr_value_("Num_Std_Dev", node)
        if value is not None and "Num_Std_Dev" not in already_processed:
            already_processed.add("Num_Std_Dev")
            value = self.gds_parse_float(value, node, "Num_Std_Dev")
            self.Num_Std_Dev = value
        value = find_attr_value_("Percentile", node)
        if value is not None and "Percentile" not in already_processed:
            already_processed.add("Percentile")
            value = self.gds_parse_float(value, node, "Percentile")
            self.Percentile = value
        value = find_attr_value_("ConfidenceLevel", node)
        if value is not None and "ConfidenceLevel" not in already_processed:
            already_processed.add("ConfidenceLevel")
            value = self.gds_parse_float(value, node, "ConfidenceLevel")
            self.ConfidenceLevel = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Value":
            obj_ = Value.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Value = obj_
            obj_.original_tagname_ = "Value"
        elif nodeName_ == "Units":
            obj_ = Units.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Units = obj_
            obj_.original_tagname_ = "Units"
        elif nodeName_ == "Unitless":
            obj_ = Unitless.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Unitless = obj_
            obj_.original_tagname_ = "Unitless"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)
        elif nodeName_ == "Scale":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Scale")
            value_ = self.gds_validate_string(value_, node, "Scale")
            self.Scale = value_
            self.Scale_nsprefix_ = child_.prefix
            # validate type ScaleType
            self.validate_ScaleType(self.Scale)


class Unit(GeneratedsSuper):
    """This element declares the content model for `Unit`, which contains a unit and has two optional attributes.

    1. The first attribute, `power`, is used to indicate the exponent for `Unit`.
    2. The second attribute, `description`, is used to describe `Unit`.

    Note -	Multiple `Unit` elements are multiplied together to form units. Division is specified by setting the `power` attribute of `Unit` equal to "-1." For additional information, see the documentation for the `Units` element.

    `Unit` has a choice between two elements:

    - `Name` is the `Name` of the unit, and can occur only once in the Unit element.
    - `Currency` is the `CurrencyCode` for the unit, if it is a unit expressing cost in an ISO 4217 recognised currency.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        power: float = None,
        description: str = None,
        Name: str = None,
        Currency: CurrencyCode = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.power = _cast(float, power)
        self.power_nsprefix_ = None
        self.description = _cast(None, description)
        self.description_nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Currency = Currency
        self.validate_CurrencyCode(self.Currency)
        self.Currency_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Unit)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Unit.subclass:
            return Unit.subclass(*args_, **kwargs_)
        else:
            return Unit(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Currency(self):
        return self.Currency

    def set_Currency(self, Currency):
        self.Currency = Currency

    CurrencyProp = property(get_Currency, set_Currency)

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power

    powerProp = property(get_power, set_power)

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    descriptionProp = property(get_description, set_description)

    def validate_CurrencyCode(self, value):
        result = True
        # Validate type CurrencyCode, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            value = value
            enumerations = [
                "AFA",
                "ALL",
                "AMD",
                "ANG",
                "AOA",
                "ARS",
                "ATS",
                "AUD",
                "AWG",
                "AZM",
                "BAM",
                "BBD",
                "BDT",
                "BEF",
                "BGL",
                "BGN",
                "BHD",
                "BIF",
                "BMD",
                "BND",
                "BOB",
                "BOV",
                "BRL",
                "BSD",
                "BTN",
                "BWP",
                "BYB",
                "BYR",
                "BZD",
                "CAD",
                "CDF",
                "CHF",
                "CLF",
                "CLP",
                "CNY",
                "COP",
                "CRC",
                "CUP",
                "CVE",
                "CYP",
                "CZK",
                "DEM",
                "DJF",
                "DKK",
                "DOP",
                "DZD",
                "EEK",
                "EGP",
                "ERN",
                "ESP",
                "ETB",
                "EUR",
                "FIM",
                "FJD",
                "FKP",
                "FRF",
                "GBP",
                "GEL",
                "GHC",
                "GIP",
                "GMD",
                "GNF",
                "GRD",
                "GTQ",
                "GWP",
                "GYD",
                "HKD",
                "HNL",
                "HRK",
                "HTG",
                "HUF",
                "IDR",
                "IEP",
                "ILS",
                "INR",
                "IQD",
                "IRR",
                "ISK",
                "ITL",
                "JMD",
                "JOD",
                "JPY",
                "KES",
                "KGS",
                "KHR",
                "KMF",
                "KPW",
                "KRW",
                "KWD",
                "KYD",
                "KZT",
                "LAK",
                "LBP",
                "LKR",
                "LRD",
                "LSL",
                "LTL",
                "LUF",
                "LVL",
                "LYD",
                "MAD",
                "MDL",
                "MGF",
                "MKD",
                "MMK",
                "MNT",
                "MOP",
                "MRO",
                "MTL",
                "MUR",
                "MVR",
                "MWK",
                "MXN",
                "MXV",
                "MYR",
                "MZM",
                "NAD",
                "NGN",
                "NIO",
                "NLG",
                "NOK",
                "NPR",
                "NZD",
                "OMR",
                "PAB",
                "PEN",
                "PGK",
                "PHP",
                "PKR",
                "PLN",
                "PTE",
                "PYG",
                "QAR",
                "ROL",
                "RUB",
                "RUR",
                "RWF",
                "SAR",
                "SBD",
                "SCR",
                "SDD",
                "SEK",
                "SGD",
                "SHP",
                "SIT",
                "SKK",
                "SLL",
                "SOS",
                "SRG",
                "STD",
                "SVC",
                "SYP",
                "SZL",
                "THB",
                "TJR",
                "TMM",
                "TND",
                "TOP",
                "TPE",
                "TRL",
                "TTD",
                "TWD",
                "TZS",
                "UAH",
                "UGX",
                "USD",
                "UYU",
                "UZS",
                "VEB",
                "VND",
                "VUV",
                "WST",
                "XAF",
                "XCD",
                "XDR",
                "XOF",
                "XPF",
                "YER",
                "YUM",
                "ZAR",
                "ZMK",
                "ZWD",
            ]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on CurrencyCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
            if len(value) != 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd length restriction on CurrencyCode'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
        return result

    def has__content(self):
        if self.Name is not None or self.Currency is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Unit",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Unit")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Unit":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Unit"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Unit",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Unit"
    ):
        if self.power is not None and "power" not in already_processed:
            already_processed.add("power")
            outfile.write(
                ' power="%s"' % self.gds_format_decimal(self.power, input_name="power")
            )
        if self.description is not None and "description" not in already_processed:
            already_processed.add("description")
            outfile.write(
                " description=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.description), input_name="description"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Unit",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sName>%s</%sName>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(quote_xml(self.Name), input_name="Name")
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Currency is not None:
            namespaceprefix_ = (
                self.Currency_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Currency_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sCurrency>%s</%sCurrency>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Currency), input_name="Currency"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("power", node)
        if value is not None and "power" not in already_processed:
            already_processed.add("power")
            value = self.gds_parse_decimal(value, node, "power")
            self.power = value
        value = find_attr_value_("description", node)
        if value is not None and "description" not in already_processed:
            already_processed.add("description")
            self.description = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Name")
            value_ = self.gds_validate_string(value_, node, "Name")
            self.Name = value_
            self.Name_nsprefix_ = child_.prefix
        elif nodeName_ == "Currency":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Currency")
            value_ = self.gds_validate_string(value_, node, "Currency")
            self.Currency = value_
            self.Currency_nsprefix_ = child_.prefix
            # validate type CurrencyCode
            self.validate_CurrencyCode(self.Currency)


class Unitless(GeneratedsSuper):
    """This element declares the content model for `Unitless`, which is an empty element used whenever a property, parameter, or uncertainty value has no units."""

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Unitless)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Unitless.subclass:
            return Unitless.subclass(*args_, **kwargs_)
        else:
            return Unitless(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def has__content(self):
        if ():
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Unitless",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Unitless")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Unitless":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Unitless"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Unitless",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Unitless"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Unitless",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


class Units(GeneratedsSuper):
    """This element declares the content model for `Units`, which contains units and has four optional attributes.

    1. The first attribute, `system`, is used to indicate the units system, such as "SI."
    2. The second attribute, `factor`, is used to indicate a constant multiplier in floating point format.
    3. The third attribute, `name`, is used to indicate the name of the units
    4. The fourth attribute, `description`, is used to describe the units.

    `Units` is composed of the following elements.

    - `Unit` contains a unit and must occur one or more times within the `Units` element. For additional information, see the documentation for the `Unit` element.

    Note -	Multiple `Unit` elements are multiplied together to form the units. Division is specified by using setting the `power` attribute of `Unit` equal to "-1."
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        system: str = None,
        factor: float = None,
        name: str = None,
        description: str = None,
        Unit=None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.system = _cast(None, system)
        self.system_nsprefix_ = None
        self.factor = _cast(float, factor)
        self.factor_nsprefix_ = None
        self.name = _cast(None, name)
        self.name_nsprefix_ = None
        self.description = _cast(None, description)
        self.description_nsprefix_ = None
        if Unit is None:
            self.Unit = []
        else:
            self.Unit = Unit
        self.Unit_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Units)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Units.subclass:
            return Units.subclass(*args_, **kwargs_)
        else:
            return Units(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Unit(self):
        return self.Unit

    def set_Unit(self, Unit):
        self.Unit = Unit

    def add_Unit(self, value):
        self.Unit.append(value)

    def insert_Unit_at(self, index, value):
        self.Unit.insert(index, value)

    def replace_Unit_at(self, index, value):
        self.Unit[index] = value

    UnitProp = property(get_Unit, set_Unit)

    def get_system(self):
        return self.system

    def set_system(self, system):
        self.system = system

    systemProp = property(get_system, set_system)

    def get_factor(self):
        return self.factor

    def set_factor(self, factor):
        self.factor = factor

    factorProp = property(get_factor, set_factor)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    nameProp = property(get_name, set_name)

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    descriptionProp = property(get_description, set_description)

    def has__content(self):
        if self.Unit:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Units",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Units")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Units":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Units"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="Units",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def string(self, format: str | None = None) -> str:
        """Returns a formatted representation of the Units.

        Args:
            format (str | None, optional): the units string formatter. Say your units are pound-force (lbf) per square inch (in), the following formats will return: Defaults to None.

            - format = 'explicit': 'lbf^1·in^-2'
            - format = 'short': 'lbf·in^-2'
            - format = None (default): 'lbf / in^-2'

        Returns:
            str: the formatted string representation
        """
        s = ""
        match format:
            case "explicit":
                for unit in self.Unit:
                    u = unit.Name if unit.Name is not None else unit.Currency._value_
                    power = 1.0 if unit.power is None else float(unit.power)
                    s += u + "^" + str(power) + "·"
                return s[0 : len(s) - 3]
            case "short":
                for unit in self.Unit:
                    u = unit.Name if unit.Name is not None else unit.Currency._value_
                    power = 1.0 if unit.power is None else float(unit.power)
                    if power == 1.0:
                        s += u + "·"
                    elif power.is_integer():
                        s += u + "^" + str(int(power)) + "·"
                    else:
                        s += u + "^" + str(power) + "·"
                return s[0 : len(s) - 1]
            case _:
                numerator = ""
                denominator = ""
                for unit in self.Unit:
                    u = unit.Name if unit.Name is not None else unit.Currency._value_
                    power = 1.0 if unit.power is None else float(unit.power)
                    if power > 0:
                        if power == 1.0:
                            numerator += u + "·"
                        elif power.is_integer():
                            numerator += u + "^" + str(int(power)) + "·"
                        else:
                            numerator += u + "^" + str(power) + "·"
                    elif power < 0:
                        if power == -1.0:
                            denominator += u + "·"
                        elif power.is_integer():
                            denominator += u + "^" + str(abs(int(power))) + "·"
                        else:
                            denominator += u + "^" + str(abs(power)) + "·"
                if len(denominator) == 0:
                    return numerator[0:-1]
                else:
                    return numerator[0:-1] + " / " + denominator[0:-1]

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Units"
    ):
        if self.system is not None and "system" not in already_processed:
            already_processed.add("system")
            outfile.write(
                " system=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.system), input_name="system"
                        )
                    ),
                )
            )
        if self.factor is not None and "factor" not in already_processed:
            already_processed.add("factor")
            outfile.write(
                ' factor="%s"' % self.gds_format_float(self.factor, input_name="factor")
            )
        if self.name is not None and "name" not in already_processed:
            already_processed.add("name")
            outfile.write(
                " name=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.name), input_name="name"
                        )
                    ),
                )
            )
        if self.description is not None and "description" not in already_processed:
            already_processed.add("description")
            outfile.write(
                " description=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.description), input_name="description"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Units",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for Unit_ in self.Unit:
            namespaceprefix_ = (
                self.Unit_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Unit_nsprefix_)
                else ""
            )
            Unit_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Unit",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("system", node)
        if value is not None and "system" not in already_processed:
            already_processed.add("system")
            self.system = value
        value = find_attr_value_("factor", node)
        if value is not None and "factor" not in already_processed:
            already_processed.add("factor")
            value = self.gds_parse_float(value, node, "factor")
            self.factor = value
        value = find_attr_value_("name", node)
        if value is not None and "name" not in already_processed:
            already_processed.add("name")
            self.name = value
        value = find_attr_value_("description", node)
        if value is not None and "description" not in already_processed:
            already_processed.add("description")
            self.description = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Unit":
            obj_ = Unit.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Unit.append(obj_)
            obj_.original_tagname_ = "Unit"


class Value(GeneratedsSuper):
    """This element declares the content model for `Value`, which contains a string representing a value. `Value` has one required attribute, `format`, for indicating the format of the value."""

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self, format: DataFormat = None, valueOf_=None, gds_collector_=None, **kwargs_
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.format = _cast(None, format)
        self.format_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, Value)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Value.subclass:
            return Value.subclass(*args_, **kwargs_)
        else:
            return Value(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_format(self):
        return self.format

    def set_format(self, format):
        self.format = format

    formatProp = property(get_format, set_format)

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        self.valueOf_ = valueOf_

    def validate_DataFormat(self, value):
        # Validate type DataFormat, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            value = value
            enumerations = ["float", "integer", "string", "exponential", "mixed"]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DataFormat'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def has__content(self):
        if 1 if type(self.valueOf_) in [int, float] else self.valueOf_:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Value",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("Value")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "Value":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="Value"
        )
        outfile.write(">")
        self._exportChildren(
            outfile,
            level + 1,
            namespaceprefix_,
            namespacedef_,
            name_,
            pretty_print=pretty_print,
        )
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="Value"
    ):
        if self.format is not None and "format" not in already_processed:
            already_processed.add("format")
            outfile.write(
                " format=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.format), input_name="format"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="Value",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("format", node)
        if value is not None and "format" not in already_processed:
            already_processed.add("format")
            self.format = value
            self.validate_DataFormat(self.format)  # validate type DataFormat

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


class AuthorityDetails(GeneratedsSuper):
    """This element declares the content model for `AuthorityDetails`, which contains a description of an authority referenced by other elements, such as the `Specification` and `Name` elements.  An authority is typically an organisation that is the authoritative source of information about the element that is referencing it.

    `AuthorityDetails` has one required attribute, `id`, which may be arbitrarily assigned but must be unique among `id` attributes assigned elsewhere in a MatML document.

    `AuthorityDetails` additionally has two elements, `Name` and `Notes`.

    - `Name` contains the name of the Authority.  `Name` must occur once and only once within the `AuthorityDetails` element.
    - `Notes` contains any additional information concerning the parameter and may occur once or not at all within the `AuthorityDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        Name: Name = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, AuthorityDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AuthorityDetails.subclass:
            return AuthorityDetails.subclass(*args_, **kwargs_)
        else:
            return AuthorityDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if self.Name is not None or self.Notes is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="AuthorityDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("AuthorityDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "AuthorityDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="AuthorityDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="AuthorityDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="AuthorityDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="AuthorityDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class DataSourceDetails(GeneratedsSuper):
    """This element declares the content model for `DataSourceDetails`, which contains a description of a data source referenced by the `PropertyData` element.

    `DataSourceDetails` has one required attribute, `id`, which may be arbitrarily assigned but must be unique among `id` attributes assigned elsewhere in a MatML document.

    `DataSourceDetails` also has one optional attribute, `type`, for specifying the type of the data source (examples include "unpublished report," "journal," "handbook," etc.)

    `DataSourceDetails` is composed of the following elements.

    - Name contains the name of the data source and has one optional attribute, authority, for identifying an authoritative source of data source names. Name must occur once and only once within the DataSourceDetails element.
    - Notes contains any additional information concerning the data source and may occur once or not at all within the DataSourceDetails element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        type_: str = None,
        Name: Name = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, DataSourceDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DataSourceDetails.subclass:
            return DataSourceDetails.subclass(*args_, **kwargs_)
        else:
            return DataSourceDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def get_type(self):
        return self.type_

    def set_type(self, type_):
        self.type_ = type_

    typeProp = property(get_type, set_type)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if self.Name is not None or self.Notes is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="DataSourceDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("DataSourceDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "DataSourceDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="DataSourceDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="DataSourceDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="DataSourceDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )
        if self.type_ is not None and "type_" not in already_processed:
            already_processed.add("type_")
            outfile.write(
                " type=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.type_), input_name="type"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="DataSourceDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value
        value = find_attr_value_("type", node)
        if value is not None and "type" not in already_processed:
            already_processed.add("type")
            self.type_ = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class MeasurementTechniqueDetails(GeneratedsSuper):
    """This element declares the content model for `MeasurementTechniqueDetails`, which contains a description of a measurement technique referenced by the `PropertyData` element.

    `MeasurementTechniqueDetails` has one required attribute, `id`, which may be arbitrarily assigned but must be unique among `id` attributes assigned elsewhere in a MatML document.

    `MeasurementTechniqueDetails` is composed of the following elements.

    - `Name` contains the name of the measurement technique and has one optional attribute, `authority`, for identifying an authoritative source of measurement techniques. `Name` must occur once and only once within the `MeasurementTechniqueDetails` element.
    - `Notes` contains any additional information concerning the measurement technique, such as a description of the technique, and may occur once or not at all within the `MeasurementTechniqueDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        Name: Name = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MeasurementTechniqueDetails
            )
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MeasurementTechniqueDetails.subclass:
            return MeasurementTechniqueDetails.subclass(*args_, **kwargs_)
        else:
            return MeasurementTechniqueDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if self.Name is not None or self.Notes is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="MeasurementTechniqueDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("MeasurementTechniqueDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if (
            self.original_tagname_ is not None
            and name_ == "MeasurementTechniqueDetails"
        ):
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="MeasurementTechniqueDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="MeasurementTechniqueDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="MeasurementTechniqueDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="MeasurementTechniqueDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class ParameterDetails(GeneratedsSuper):
    """This element declares the content model for `ParameterDetails`, which contains a description of a parameter referenced by the `ParameterValue` element.

    `ParameterDetails` has one required attribute, `id`, which may be arbitrarily assigned but must be unique among `id` attributes assigned elsewhere in a MatML document.

    `ParameterDetails` is composed of the following elements.

    - `Name` contains the name of the parameter and has one optional attribute, `authority`, for identifying an authoritative source of parameter names. `Name` must occur once and only once within the `ParameterDetails` element.
    - `Units` and `Unitless` are mutually exclusive elements for describing the parameter's units. `Units` or `Unitless` must occur once and only once within the `ParameterDetails` element. For additional information, see the documentation for the `Units` and `Unitless` elements.
    - `Notes` contains any additional information concerning the parameter and may occur once or not at all within the `ParameterDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        Name: Name = None,
        Units: Units = None,
        Unitless: Unitless = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Units = Units
        self.Units_nsprefix_ = None
        self.Unitless = Unitless
        self.Unitless_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, ParameterDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParameterDetails.subclass:
            return ParameterDetails.subclass(*args_, **kwargs_)
        else:
            return ParameterDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Units(self):
        return self.Units

    def set_Units(self, Units):
        self.Units = Units

    UnitsProp = property(get_Units, set_Units)

    def get_Unitless(self):
        return self.Unitless

    def set_Unitless(self, Unitless):
        self.Unitless = Unitless

    UnitlessProp = property(get_Unitless, set_Unitless)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Name is not None
            or self.Units is not None
            or self.Unitless is not None
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ParameterDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("ParameterDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "ParameterDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="ParameterDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="ParameterDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="ParameterDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ParameterDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Units is not None:
            namespaceprefix_ = (
                self.Units_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Units_nsprefix_)
                else ""
            )
            self.Units.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Units",
                pretty_print=pretty_print,
            )
        if self.Unitless is not None:
            namespaceprefix_ = (
                self.Unitless_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Unitless_nsprefix_)
                else ""
            )
            self.Unitless.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Unitless",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Units":
            obj_ = Units.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Units = obj_
            obj_.original_tagname_ = "Units"
        elif nodeName_ == "Unitless":
            obj_ = Unitless.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Unitless = obj_
            obj_.original_tagname_ = "Unitless"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class PropertyDetails(GeneratedsSuper):
    """This element declares the content model for `PropertyDetails`, which contains a description of a property referenced by the `PropertyData` element.

    `PropertyDetails` has one required attribute, `id`, which may be arbitrarily assigned but must be unique among `id` attributes assigned elsewhere in a MatML document.

    `PropertyDetails` also has one optional attribute, `type`, for specifying the type of the property (examples include "thermal," "mechanical," "electrical," etc.).

    `PropertyDetails` is composed of the following elements.

    - `Name` contains the name of the property and has one optional attribute, `authority`, for identifying an authoritative source of property names. `Name` must occur once and only once within the `PropertyDetails` element.
    - `Units` and `Unitless` are mutually exclusive elements for describing the property's units. `Units` or `Unitless` must occur once and only once within the `PropertyDetails` element. For additional information, see the documentation for the `Units` and `Unitless` elements.
    - `Notes` contains any additional information concerning the property and may occur once or not at all within the `PropertyDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        type_: str = None,
        Name: Name = None,
        Units: Units = None,
        Unitless: Unitless = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Units = Units
        self.Units_nsprefix_ = None
        self.Unitless = Unitless
        self.Unitless_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, PropertyDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PropertyDetails.subclass:
            return PropertyDetails.subclass(*args_, **kwargs_)
        else:
            return PropertyDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Units(self):
        return self.Units

    def set_Units(self, Units):
        self.Units = Units

    UnitsProp = property(get_Units, set_Units)

    def get_Unitless(self):
        return self.Unitless

    def set_Unitless(self, Unitless):
        self.Unitless = Unitless

    UnitlessProp = property(get_Unitless, set_Unitless)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def get_type(self):
        return self.type_

    def set_type(self, type_):
        self.type_ = type_

    typeProp = property(get_type, set_type)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if (
            self.Name is not None
            or self.Units is not None
            or self.Unitless is not None
            or self.Notes is not None
        ):
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="PropertyDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("PropertyDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "PropertyDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="PropertyDetails"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="PropertyDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="PropertyDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )
        if self.type_ is not None and "type_" not in already_processed:
            already_processed.add("type_")
            outfile.write(
                " type=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.type_), input_name="type"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="PropertyDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Units is not None:
            namespaceprefix_ = (
                self.Units_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Units_nsprefix_)
                else ""
            )
            self.Units.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Units",
                pretty_print=pretty_print,
            )
        if self.Unitless is not None:
            namespaceprefix_ = (
                self.Unitless_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Unitless_nsprefix_)
                else ""
            )
            self.Unitless.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Unitless",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value
        value = find_attr_value_("type", node)
        if value is not None and "type" not in already_processed:
            already_processed.add("type")
            self.type_ = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Units":
            obj_ = Units.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Units = obj_
            obj_.original_tagname_ = "Units"
        elif nodeName_ == "Unitless":
            obj_ = Unitless.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Unitless = obj_
            obj_.original_tagname_ = "Unitless"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class SourceDetails(GeneratedsSuper):
    """This element declares the content model for `SourceDetails`, which contains the name of the source of the component.

    `Name` contains the name of the source and has one optional attribute, `Notes`.

    `Notes` contains any additional information concerning the data source and may occur once or not at all within the `DataSourceDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        type_: str = None,
        Name: Name = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, SourceDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SourceDetails.subclass:
            return SourceDetails.subclass(*args_, **kwargs_)
        else:
            return SourceDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def get_type(self):
        return self.type_

    def set_type(self, type_):
        self.type_ = type_

    typeProp = property(get_type, set_type)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if self.Name is not None or self.Notes is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="SourceDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("SourceDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "SourceDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="SourceDetails"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="SourceDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="SourceDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )
        if self.type_ is not None and "type_" not in already_processed:
            already_processed.add("type_")
            outfile.write(
                " type=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.type_), input_name="type"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="SourceDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value
        value = find_attr_value_("type", node)
        if value is not None and "type" not in already_processed:
            already_processed.add("type")
            self.type_ = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class SpecimenDetails(GeneratedsSuper):
    """This element declares the content model for `SpecimenDetails`, which contains a description of a specimen referenced by the `PropertyData` element.

    `SpecimenDetails` has one required attribute, `id`, which may be arbitrarily assigned but must be unique among `id` attributes assigned elsewhere in a MatML document.

    `SpecimenDetails` also has one optional attribute, `type`, for specifying the type of the specimen (examples include "cylindrical," "rectangular," "full cross-section," "pressed," etc.)

    `SpecimenDetails` is composed of the following elements. `SpecimenDetails` also has 3 optional elements, `Name`, `Geometry`, and `Notes`.

    - `Name` contains the name of the specimen and has one optional attribute, `authority`, for identifying an authoritative source of specimen names. `Name` may occur once or not at all within the `SpecimenDetails` element.
    - `Geometry` describes the dimensions of the Component.  For additional information, see the documentation for the `Geometry` type. `Geometry` may occur once or not at all within the `SpecimenDetails` element.
    - `Notes` contains any additional information concerning the specimen and may occur once or not at all within the `SpecimenDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        type_: str = None,
        Name: Name = None,
        Notes: str = None,
        Geometry: Geometry = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.type_ = _cast(None, type_)
        self.type__nsprefix_ = None
        self.Name = Name
        self.Name_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None
        self.Geometry = Geometry
        self.Geometry_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, SpecimenDetails)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SpecimenDetails.subclass:
            return SpecimenDetails.subclass(*args_, **kwargs_)
        else:
            return SpecimenDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_Name(self):
        return self.Name

    def set_Name(self, Name):
        self.Name = Name

    NameProp = property(get_Name, set_Name)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_Geometry(self):
        return self.Geometry

    def set_Geometry(self, Geometry):
        self.Geometry = Geometry

    GeometryProp = property(get_Geometry, set_Geometry)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def get_type(self):
        return self.type_

    def set_type(self, type_):
        self.type_ = type_

    typeProp = property(get_type, set_type)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if self.Name is not None or self.Notes is not None or self.Geometry is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="SpecimenDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("SpecimenDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "SpecimenDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="SpecimenDetails"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="SpecimenDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="SpecimenDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )
        if self.type_ is not None and "type_" not in already_processed:
            already_processed.add("type_")
            outfile.write(
                " type=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.type_), input_name="type"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="SpecimenDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.Name is not None:
            namespaceprefix_ = (
                self.Name_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Name_nsprefix_)
                else ""
            )
            self.Name.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Name",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )
        if self.Geometry is not None:
            namespaceprefix_ = (
                self.Geometry_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Geometry_nsprefix_)
                else ""
            )
            self.Geometry.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="Geometry",
                pretty_print=pretty_print,
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value
        value = find_attr_value_("type", node)
        if value is not None and "type" not in already_processed:
            already_processed.add("type")
            self.type_ = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "Name":
            obj_ = Name.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Name = obj_
            obj_.original_tagname_ = "Name"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)
        elif nodeName_ == "Geometry":
            obj_ = Geometry.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Geometry = obj_
            obj_.original_tagname_ = "Geometry"


class TestConditionDetails(GeneratedsSuper):
    """This element declares the content model for `TestConditionDetails`, which contains a description of the test conditions referenced by the `PropertyData` element.

    `TestConditionDetails` has one required attribute, `id`, which may be arbitrarily assigned but must be unique among `id` attributes assigned elsewhere in a MatML document.

    `TestConditionDetails` has two optional elements, `ParameterValue` and `Notes`.

    - `ParameterValue` contains the value(s) of a parameter, i.e., a test condition, and may occur zero or more times within the `TestConditionDetails` element. For additional information, see the documentation for the `ParameterValue` element.
    - `Notes` contains any additional information concerning the test conditions and may occur once or not at all within the `TestConditionDetails` element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(
        self,
        id: str = None,
        ParameterValue: ParameterValue = None,
        Notes: str = None,
        gds_collector_=None,
        **kwargs_,
    ):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        if ParameterValue is None:
            self.ParameterValue = []
        else:
            self.ParameterValue = ParameterValue
        self.ParameterValue_nsprefix_ = None
        self.Notes = Notes
        self.validate_Notes(self.Notes)
        self.Notes_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TestConditionDetails
            )
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TestConditionDetails.subclass:
            return TestConditionDetails.subclass(*args_, **kwargs_)
        else:
            return TestConditionDetails(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_ParameterValue(self, parameter=None):
        if parameter is not None:
            parameters = []
            for parameter_value in self.get_ParameterValue():
                if parameter_value.get_property() == property:
                    parameters.append(parameter_value)
            return parameters
        return self.ParameterValue

    def set_ParameterValue(self, ParameterValue):
        self.ParameterValue = ParameterValue

    def add_ParameterValue(self, value):
        self.ParameterValue.append(value)

    def insert_ParameterValue_at(self, index, value):
        self.ParameterValue.insert(index, value)

    def replace_ParameterValue_at(self, index, value):
        self.ParameterValue[index] = value

    ParameterValueProp = property(get_ParameterValue, set_ParameterValue)

    def get_Notes(self):
        return self.Notes

    def set_Notes(self, Notes):
        self.Notes = Notes

    NotesProp = property(get_Notes, set_Notes)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def validate_Notes(self, value):
        result = True
        # Validate type Notes, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            pass
        return result

    def has__content(self):
        if self.ParameterValue or self.Notes is not None:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="TestConditionDetails",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("TestConditionDetails")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "TestConditionDetails":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="TestConditionDetails",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="TestConditionDetails",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="TestConditionDetails",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="TestConditionDetails",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        for ParameterValue_ in self.ParameterValue:
            namespaceprefix_ = (
                self.ParameterValue_nsprefix_ + ":"
                if (UseCapturedNS_ and self.ParameterValue_nsprefix_)
                else ""
            )
            ParameterValue_.export(
                outfile,
                level,
                namespaceprefix_,
                namespacedef_="",
                name_="ParameterValue",
                pretty_print=pretty_print,
            )
        if self.Notes is not None:
            namespaceprefix_ = (
                self.Notes_nsprefix_ + ":"
                if (UseCapturedNS_ and self.Notes_nsprefix_)
                else ""
            )
            showIndent(outfile, level, pretty_print)
            outfile.write(
                "<%sNotes>%s</%sNotes>%s"
                % (
                    namespaceprefix_,
                    self.gds_encode(
                        self.gds_format_string(
                            quote_xml(self.Notes), input_name="Notes"
                        )
                    ),
                    namespaceprefix_,
                    eol_,
                )
            )

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        if nodeName_ == "ParameterValue":
            obj_ = ParameterValue.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.ParameterValue.append(obj_)
            obj_.original_tagname_ = "ParameterValue"
        elif nodeName_ == "Notes":
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, "Notes")
            value_ = self.gds_validate_string(value_, node, "Notes")
            self.Notes = value_
            self.Notes_nsprefix_ = child_.prefix
            # validate type Notes
            self.validate_Notes(self.Notes)


class ParentMaterialType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, id: str = None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ParentMaterialType
            )
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ParentMaterialType.subclass:
            return ParentMaterialType.subclass(*args_, **kwargs_)
        else:
            return ParentMaterialType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    idProp = property(get_id, set_id)

    def has__content(self):
        if ():
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ParentMaterialType",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("ParentMaterialType")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "ParentMaterialType":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile,
            level,
            already_processed,
            namespaceprefix_,
            name_="ParentMaterialType",
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="ParentMaterialType",
                pretty_print=pretty_print,
            )
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self,
        outfile,
        level,
        already_processed,
        namespaceprefix_="",
        name_="ParentMaterialType",
    ):
        if self.id is not None and "id" not in already_processed:
            already_processed.add("id")
            outfile.write(
                " id=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(quote_attrib(self.id), input_name="id")
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="ParentMaterialType",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("id", node)
        if value is not None and "id" not in already_processed:
            already_processed.add("id")
            self.id = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


class SymbolType(GeneratedsSuper):
    """This element declares the content model for `Symbol`, which contains the symbol for the chemical element. The entry for `Symbol` is selected from among the strings enumerated by the `ChemicalElementSymbol` datatype.

    `Symbol` has one optional attribute, `subscript`, for indicating the subscript (formula units) of the chemical element.
    """

    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, subscript="1", valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.subscript = _cast(None, subscript)
        self.subscript_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, SymbolType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if SymbolType.subclass:
            return SymbolType.subclass(*args_, **kwargs_)
        else:
            return SymbolType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_subscript(self):
        return self.subscript

    def set_subscript(self, subscript):
        self.subscript = subscript

    subscriptProp = property(get_subscript, set_subscript)

    def get_valueOf_(self):
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        self.valueOf_ = valueOf_

    def validate_ChemicalElementSymbol(self, value):
        result = True
        # Validate type ChemicalElementSymbol, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            value = value
            enumerations = [
                "H",
                "He",
                "Li",
                "Be",
                "B",
                "C",
                "N",
                "O",
                "F",
                "Ne",
                "Na",
                "Mg",
                "Al",
                "Si",
                "P",
                "S",
                "Cl",
                "Ar",
                "K",
                "Ca",
                "Sc",
                "Ti",
                "V",
                "Cr",
                "Mn",
                "Fe",
                "Co",
                "Ni",
                "Cu",
                "Zn",
                "Ga",
                "Ge",
                "As",
                "Se",
                "Br",
                "Kr",
                "Rb",
                "Sr",
                "Y",
                "Zr",
                "Nb",
                "Mo",
                "Tc",
                "Ru",
                "Rh",
                "Pd",
                "Ag",
                "Cd",
                "In",
                "Sn",
                "Sb",
                "Te",
                "I",
                "Xe",
                "Cs",
                "Ba",
                "La",
                "Ce",
                "Pr",
                "Nd",
                "Pm",
                "Sm",
                "Eu",
                "Gd",
                "Tb",
                "Dy",
                "Ho",
                "Er",
                "Tm",
                "Yb",
                "Lu",
                "Hf",
                "Ta",
                "W",
                "Re",
                "Os",
                "Ir",
                "Pt",
                "Au",
                "Hg",
                "Tl",
                "Pb",
                "Bi",
                "Po",
                "At",
                "Rn",
                "Fr",
                "Ra",
                "Ac",
                "Th",
                "Pa",
                "U",
                "Np",
                "Pu",
                "Am",
                "Cm",
                "Bk",
                "Cf",
                "Es",
                "Fm",
                "Md",
                "No",
                "Lr",
                "Rf",
                "Db",
                "Sg",
                "Bh",
                "Hs",
                "Mt",
                "Uun",
                "Uuu",
                "Uub",
                "Uuq",
                "Uuh",
                "Uuo",
            ]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ChemicalElementSymbol'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False
        return result

    def has__content(self):
        if 1 if type(self.valueOf_) in [int, float] else self.valueOf_:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="SymbolType",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("SymbolType")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "SymbolType":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="SymbolType"
        )
        outfile.write(">")
        self._exportChildren(
            outfile,
            level + 1,
            namespaceprefix_,
            namespacedef_,
            name_,
            pretty_print=pretty_print,
        )
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="SymbolType"
    ):
        if self.subscript != "1" and "subscript" not in already_processed:
            already_processed.add("subscript")
            outfile.write(
                " subscript=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.subscript), input_name="subscript"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="SymbolType",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("subscript", node)
        if value is not None and "subscript" not in already_processed:
            already_processed.add("subscript")
            self.subscript = value

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


class GraphType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, anytypeobjs_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        if anytypeobjs_ is None:
            self.anytypeobjs_ = []
        else:
            self.anytypeobjs_ = anytypeobjs_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, GraphType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GraphType.subclass:
            return GraphType.subclass(*args_, **kwargs_)
        else:
            return GraphType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_anytypeobjs_(self):
        return self.anytypeobjs_

    def set_anytypeobjs_(self, anytypeobjs_):
        self.anytypeobjs_ = anytypeobjs_

    def add_anytypeobjs_(self, value):
        self.anytypeobjs_.append(value)

    def insert_anytypeobjs_(self, index, value):
        self._anytypeobjs_[index] = value

    def has__content(self):
        if self.anytypeobjs_:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="GraphType",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("GraphType")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "GraphType":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="GraphType"
        )
        if self.has__content():
            outfile.write(">%s" % (eol_,))
            self._exportChildren(
                outfile,
                level + 1,
                namespaceprefix_,
                namespacedef_,
                name_="GraphType",
                pretty_print=pretty_print,
            )
            showIndent(outfile, level, pretty_print)
            outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))
        else:
            outfile.write("/>%s" % (eol_,))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="GraphType"
    ):
        pass

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="GraphType",
        fromsubclass_=False,
        pretty_print=True,
    ):
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if not fromsubclass_:
            for obj_ in self.anytypeobjs_:
                showIndent(outfile, level, pretty_print)
                outfile.write(str(obj_))
                outfile.write("\n")

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        pass

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        content_ = self.gds_build_any(child_, "GraphType")
        self.anytypeobjs_.append(content_)


class DataType(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None

    def __init__(self, format=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get("parent_object_")
        self.ns_prefix_ = None
        self.format = _cast(None, format)
        self.format_nsprefix_ = None
        self.valueOf_ = valueOf_

    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(CurrentSubclassModule_, DataType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DataType.subclass:
            return DataType.subclass(*args_, **kwargs_)
        else:
            return DataType(*args_, **kwargs_)

    factory = staticmethod(factory)

    def get_ns_prefix_(self):
        return self.ns_prefix_

    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix

    def get_format(self):
        return self.format

    def set_format(self, format):
        self.format = format

    formatProp = property(get_format, set_format)

    def get_valueOf_(self, delimiter=","):
        data_format = self.get_format()
        try:
            # Use the parent's delimiter if it exists. If the attribute exists, but is None, then the delimiter is by default ','.
            delimiter = (
                ","
                if self.parent_object_.delimiter is None
                else self.parent_object_.delimiter
            )
        except AttributeError:
            try:
                # If the parent doesn't have an attribute called `delimiter`, then check the grandparent and try again.
                delimiter = (
                    ","
                    if self.parent_object_.parent_object_.delimiter is None
                    else self.parent_object_.parent_object_.delimiter
                )
            except AttributeError:
                # Otherwise... turn to the default.
                delimeter = ","
        match data_format:
            case "float":
                return [float(item) for item in self.valueOf_.split(delimiter)]
            case "integer":
                return [int(item) for item in self.valueOf_.split(delimiter)]
            case "string":
                return [str(item) for item in self.valueOf_.split(delimiter)]
            case "exponential":
                return [float(item) for item in self.valueOf_.split(delimiter)]
            case "mixed":
                return [str(item) for item in self.valueOf_.split(delimiter)]
            case _:
                try:
                    return [float(item) for item in self.valueOf_.split(delimiter)]
                except ValueError:
                    return [str(item) for item in self.valueOf_.split(delimiter)]
        return self.valueOf_

    def set_valueOf_(self, valueOf_):
        self.valueOf_ = valueOf_

    def validate_DataFormat(self, value):
        # Validate type DataFormat, a restriction on xsd:string.
        if (
            value is not None
            and Validate_simpletypes_
            and self.gds_collector_ is not None
        ):
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s is not of the correct base simple type (str)'
                    % {
                        "value": value,
                        "lineno": lineno,
                    }
                )
                return False
            value = value
            enumerations = ["float", "integer", "string", "exponential", "mixed"]
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message(
                    'Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on DataFormat'
                    % {"value": encode_str_2_3(value), "lineno": lineno}
                )
                result = False

    def has__content(self):
        if 1 if type(self.valueOf_) in [int, float] else self.valueOf_:
            return True
        else:
            return False

    def export(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="DataType",
        pretty_print=True,
    ):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get("DataType")
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = "\n"
        else:
            eol_ = ""
        if self.original_tagname_ is not None and name_ == "DataType":
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ":"
        showIndent(outfile, level, pretty_print)
        outfile.write(
            "<%s%s%s"
            % (
                namespaceprefix_,
                name_,
                namespacedef_ and " " + namespacedef_ or "",
            )
        )
        already_processed = set()
        self._exportAttributes(
            outfile, level, already_processed, namespaceprefix_, name_="DataType"
        )
        outfile.write(">")
        self._exportChildren(
            outfile,
            level + 1,
            namespaceprefix_,
            namespacedef_,
            name_,
            pretty_print=pretty_print,
        )
        outfile.write(self.convert_unicode(self.valueOf_))
        outfile.write("</%s%s>%s" % (namespaceprefix_, name_, eol_))

    def _exportAttributes(
        self, outfile, level, already_processed, namespaceprefix_="", name_="DataType"
    ):
        if self.format is not None and "format" not in already_processed:
            already_processed.add("format")
            outfile.write(
                " format=%s"
                % (
                    self.gds_encode(
                        self.gds_format_string(
                            quote_attrib(self.format), input_name="format"
                        )
                    ),
                )
            )

    def _exportChildren(
        self,
        outfile,
        level,
        namespaceprefix_="",
        namespacedef_="",
        name_="DataType",
        fromsubclass_=False,
        pretty_print=True,
    ):
        pass

    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self._buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self._buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self

    def _buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_("format", node)
        if value is not None and "format" not in already_processed:
            already_processed.add("format")
            self.format = value
            self.validate_DataFormat(self.format)  # validate type DataFormat

    def _buildChildren(
        self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None
    ):
        pass


GDSClassesMapping = {}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    """Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    """
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = " ".join(
        ['xmlns:{}="{}"'.format(prefix, uri) for prefix, uri in nsmap.items()]
    )
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = "MatML_Doc"
        rootClass = MatML_Doc
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag, namespacedef_=namespacedefs, pretty_print=True
        )
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ("-" * 50) + "\n"
        sys.stderr.write(separator)
        sys.stderr.write(
            "----- Warnings -- count: {} -----\n".format(
                len(gds_collector.get_messages()),
            )
        )
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(
    inFileName,
    silence=False,
    print_warnings=True,
    mapping=None,
    reverse_mapping=None,
    nsmap=None,
):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = "MatML_Doc"
        rootClass = MatML_Doc
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None,
        name_=rootTag,
        mapping_=mapping,
        reverse_mapping_=reverse_mapping,
        nsmap_=nsmap,
    )
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True, xml_declaration=True, encoding="utf-8"
        )
        sys.stdout.write(str(content))
        sys.stdout.write("\n")
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ("-" * 50) + "\n"
        sys.stderr.write(separator)
        sys.stderr.write(
            "----- Warnings -- count: {} -----\n".format(
                len(gds_collector.get_messages()),
            )
        )
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    """Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    """
    parser = None
    rootNode = parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = "MatML_Doc"
        rootClass = MatML_Doc
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(sys.stdout, 0, name_=rootTag, namespacedef_="")
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ("-" * 50) + "\n"
        sys.stderr.write(separator)
        sys.stderr.write(
            "----- Warnings -- count: {} -----\n".format(
                len(gds_collector.get_messages()),
            )
        )
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = "MatML_Doc"
        rootClass = MatML_Doc
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write("#from MatML_api import *\n\n")
        sys.stdout.write("import MatML_api as model_\n\n")
        sys.stdout.write("rootObj = model_.rootClass(\n")
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(")\n")
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ("-" * 50) + "\n"
        sys.stderr.write(separator)
        sys.stderr.write(
            "----- Warnings -- count: {} -----\n".format(
                len(gds_collector.get_messages()),
            )
        )
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    main()

RenameMappings_ = {}

# Mapping of namespaces to types defined in them and the file in which each is defined. simpleTypes are marked "ST" and complexTypes "CT".
NamespaceToDefMappings_ = {}

__all__ = [
    "AssociationDetails",
    "AuthorityDetails",
    "BulkDetails",
    "Characterization",
    "ChemicalComposition",
    "Class",
    "ComponentDetails",
    "Compound",
    "Concentration",
    "DataSourceDetails",
    "DataType",
    "DataType",
    "DimensionalDetails",
    "Element",
    "Form",
    "Geometry",
    "Glossary",
    "GlossaryTerm",
    "GraphType",
    "Graphs",
    "MatML_Doc",
    "Material",
    "MeasurementTechniqueDetails",
    "Metadata",
    "Name",
    "ParameterDetails",
    "ParameterValue",
    "ParentMaterialType",
    "PhaseComposition",
    "ProcessingDetails",
    "PropertyData",
    "PropertyDetails",
    "Source",
    "SourceDetails",
    "Specification",
    "SpecimenDetails",
    "SymbolType",
    "TestConditionDetails",
    "Uncertainty",
    "Unit",
    "Unitless",
    "Units",
    "Value",
]
