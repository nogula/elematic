#!/usr/bin/env python

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

import os
import sys
from lxml import etree as etree_

import MatML_api as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
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
# Globals
#

ExternalEncoding = ''
SaveElementTreeNode = True

#
# Data representation classes
#


class MatML_DocSub(supermod.MatML_Doc):
    def __init__(self, Material=None, Metadata=None, **kwargs_):
        super(MatML_DocSub, self).__init__(Material, Metadata,  **kwargs_)
supermod.MatML_Doc.subclass = MatML_DocSub
# end class MatML_DocSub


class AssociationDetailsSub(supermod.AssociationDetails):
    def __init__(self, Associate=None, Relationship=None, Notes=None, **kwargs_):
        super(AssociationDetailsSub, self).__init__(Associate, Relationship, Notes,  **kwargs_)
supermod.AssociationDetails.subclass = AssociationDetailsSub
# end class AssociationDetailsSub


class BulkDetailsSub(supermod.BulkDetails):
    def __init__(self, Name=None, Class=None, Subclass=None, Specification=None, Source=None, Form=None, ProcessingDetails=None, Characterization=None, PropertyData=None, Notes=None, **kwargs_):
        super(BulkDetailsSub, self).__init__(Name, Class, Subclass, Specification, Source, Form, ProcessingDetails, Characterization, PropertyData, Notes,  **kwargs_)
supermod.BulkDetails.subclass = BulkDetailsSub
# end class BulkDetailsSub


class CharacterizationSub(supermod.Characterization):
    def __init__(self, Formula=None, ChemicalComposition=None, PhaseComposition=None, DimensionalDetails=None, Notes=None, **kwargs_):
        super(CharacterizationSub, self).__init__(Formula, ChemicalComposition, PhaseComposition, DimensionalDetails, Notes,  **kwargs_)
supermod.Characterization.subclass = CharacterizationSub
# end class CharacterizationSub


class ChemicalCompositionSub(supermod.ChemicalComposition):
    def __init__(self, Compound=None, Element=None, **kwargs_):
        super(ChemicalCompositionSub, self).__init__(Compound, Element,  **kwargs_)
supermod.ChemicalComposition.subclass = ChemicalCompositionSub
# end class ChemicalCompositionSub


class ClassSub(supermod.Class):
    def __init__(self, Name=None, ParentMaterial=None, ParentSubClass=None, **kwargs_):
        super(ClassSub, self).__init__(Name, ParentMaterial, ParentSubClass,  **kwargs_)
supermod.Class.subclass = ClassSub
# end class ClassSub


class ComponentDetailsSub(supermod.ComponentDetails):
    def __init__(self, id=None, Name=None, Class=None, Subclass=None, Specification=None, Source=None, Form=None, ProcessingDetails=None, Characterization=None, PropertyData=None, AssociationDetails=None, ComponentDetails_member=None, **kwargs_):
        super(ComponentDetailsSub, self).__init__(id, Name, Class, Subclass, Specification, Source, Form, ProcessingDetails, Characterization, PropertyData, AssociationDetails, ComponentDetails_member,  **kwargs_)
supermod.ComponentDetails.subclass = ComponentDetailsSub
# end class ComponentDetailsSub


class CompoundSub(supermod.Compound):
    def __init__(self, Element=None, Concentration=None, Notes=None, **kwargs_):
        super(CompoundSub, self).__init__(Element, Concentration, Notes,  **kwargs_)
supermod.Compound.subclass = CompoundSub
# end class CompoundSub


class ConcentrationSub(supermod.Concentration):
    def __init__(self, Value=None, Units=None, Qualifier=None, Uncertainty=None, Notes=None, **kwargs_):
        super(ConcentrationSub, self).__init__(Value, Units, Qualifier, Uncertainty, Notes,  **kwargs_)
supermod.Concentration.subclass = ConcentrationSub
# end class ConcentrationSub


class DimensionalDetailsSub(supermod.DimensionalDetails):
    def __init__(self, Name=None, Value=None, Units=None, Qualifier=None, Uncertainty=None, Notes=None, **kwargs_):
        super(DimensionalDetailsSub, self).__init__(Name, Value, Units, Qualifier, Uncertainty, Notes,  **kwargs_)
supermod.DimensionalDetails.subclass = DimensionalDetailsSub
# end class DimensionalDetailsSub


class ElementSub(supermod.Element):
    def __init__(self, Symbol=None, Concentration=None, Notes=None, **kwargs_):
        super(ElementSub, self).__init__(Symbol, Concentration, Notes,  **kwargs_)
supermod.Element.subclass = ElementSub
# end class ElementSub


class FormSub(supermod.Form):
    def __init__(self, Description=None, Geometry=None, Notes=None, **kwargs_):
        super(FormSub, self).__init__(Description, Geometry, Notes,  **kwargs_)
supermod.Form.subclass = FormSub
# end class FormSub


class GeometrySub(supermod.Geometry):
    def __init__(self, Shape=None, Dimensions=None, Orientation=None, Notes=None, **kwargs_):
        super(GeometrySub, self).__init__(Shape, Dimensions, Orientation, Notes,  **kwargs_)
supermod.Geometry.subclass = GeometrySub
# end class GeometrySub


class GlossarySub(supermod.Glossary):
    def __init__(self, Term=None, **kwargs_):
        super(GlossarySub, self).__init__(Term,  **kwargs_)
supermod.Glossary.subclass = GlossarySub
# end class GlossarySub


class GlossaryTermSub(supermod.GlossaryTerm):
    def __init__(self, Name=None, Definition=None, Abbreviation=None, Synonym=None, Notes=None, **kwargs_):
        super(GlossaryTermSub, self).__init__(Name, Definition, Abbreviation, Synonym, Notes,  **kwargs_)
supermod.GlossaryTerm.subclass = GlossaryTermSub
# end class GlossaryTermSub


class GraphsSub(supermod.Graphs):
    def __init__(self, Graph=None, **kwargs_):
        super(GraphsSub, self).__init__(Graph,  **kwargs_)
supermod.Graphs.subclass = GraphsSub
# end class GraphsSub


class MaterialSub(supermod.Material):
    def __init__(self, id=None, layers=None, local_frame_of_reference=None, BulkDetails=None, ComponentDetails=None, Graphs=None, Glossary=None, **kwargs_):
        super(MaterialSub, self).__init__(id, layers, local_frame_of_reference, BulkDetails, ComponentDetails, Graphs, Glossary,  **kwargs_)
supermod.Material.subclass = MaterialSub
# end class MaterialSub


class MetadataSub(supermod.Metadata):
    def __init__(self, AuthorityDetails=None, DataSourceDetails=None, MeasurementTechniqueDetails=None, ParameterDetails=None, PropertyDetails=None, SourceDetails=None, SpecimenDetails=None, TestConditionDetails=None, **kwargs_):
        super(MetadataSub, self).__init__(AuthorityDetails, DataSourceDetails, MeasurementTechniqueDetails, ParameterDetails, PropertyDetails, SourceDetails, SpecimenDetails, TestConditionDetails,  **kwargs_)
supermod.Metadata.subclass = MetadataSub
# end class MetadataSub


class NameSub(supermod.Name):
    def __init__(self, authority=None, valueOf_=None, **kwargs_):
        super(NameSub, self).__init__(authority, valueOf_,  **kwargs_)
supermod.Name.subclass = NameSub
# end class NameSub


class ParameterValueSub(supermod.ParameterValue):
    def __init__(self, parameter=None, format=None, Data=None, Uncertainty=None, Qualifier=None, Notes=None, **kwargs_):
        super(ParameterValueSub, self).__init__(parameter, format, Data, Uncertainty, Qualifier, Notes,  **kwargs_)
supermod.ParameterValue.subclass = ParameterValueSub
# end class ParameterValueSub


class PhaseCompositionSub(supermod.PhaseComposition):
    def __init__(self, Name=None, Concentration=None, PropertyData=None, Notes=None, **kwargs_):
        super(PhaseCompositionSub, self).__init__(Name, Concentration, PropertyData, Notes,  **kwargs_)
supermod.PhaseComposition.subclass = PhaseCompositionSub
# end class PhaseCompositionSub


class ProcessingDetailsSub(supermod.ProcessingDetails):
    def __init__(self, Name=None, ParameterValue=None, Result=None, Notes=None, **kwargs_):
        super(ProcessingDetailsSub, self).__init__(Name, ParameterValue, Result, Notes,  **kwargs_)
supermod.ProcessingDetails.subclass = ProcessingDetailsSub
# end class ProcessingDetailsSub


class PropertyDataSub(supermod.PropertyData):
    def __init__(self, property=None, technique=None, source=None, specimen=None, test=None, delimiter=',', quote=None, Data=None, Uncertainty=None, Qualifier=None, ParameterValue=None, Notes=None, **kwargs_):
        super(PropertyDataSub, self).__init__(property, technique, source, specimen, test, delimiter, quote, Data, Uncertainty, Qualifier, ParameterValue, Notes,  **kwargs_)
supermod.PropertyData.subclass = PropertyDataSub
# end class PropertyDataSub


class SourceSub(supermod.Source):
    def __init__(self, source=None, **kwargs_):
        super(SourceSub, self).__init__(source,  **kwargs_)
supermod.Source.subclass = SourceSub
# end class SourceSub


class SpecificationSub(supermod.Specification):
    def __init__(self, authority=None, valueOf_=None, **kwargs_):
        super(SpecificationSub, self).__init__(authority, valueOf_,  **kwargs_)
supermod.Specification.subclass = SpecificationSub
# end class SpecificationSub


class UncertaintySub(supermod.Uncertainty):
    def __init__(self, DistributionType='Normal/Gaussian', Num_Std_Dev=2, Percentile=None, ConfidenceLevel=None, Value=None, Units=None, Unitless=None, Notes=None, Scale='Linear', **kwargs_):
        super(UncertaintySub, self).__init__(DistributionType, Num_Std_Dev, Percentile, ConfidenceLevel, Value, Units, Unitless, Notes, Scale,  **kwargs_)
supermod.Uncertainty.subclass = UncertaintySub
# end class UncertaintySub


class UnitSub(supermod.Unit):
    def __init__(self, power=None, description=None, Name=None, Currency=None, **kwargs_):
        super(UnitSub, self).__init__(power, description, Name, Currency,  **kwargs_)
supermod.Unit.subclass = UnitSub
# end class UnitSub


class UnitlessSub(supermod.Unitless):
    def __init__(self, **kwargs_):
        super(UnitlessSub, self).__init__( **kwargs_)
supermod.Unitless.subclass = UnitlessSub
# end class UnitlessSub


class UnitsSub(supermod.Units):
    def __init__(self, system=None, factor=None, name=None, description=None, Unit=None, **kwargs_):
        super(UnitsSub, self).__init__(system, factor, name, description, Unit,  **kwargs_)
supermod.Units.subclass = UnitsSub
# end class UnitsSub


class ValueSub(supermod.Value):
    def __init__(self, format=None, valueOf_=None, **kwargs_):
        super(ValueSub, self).__init__(format, valueOf_,  **kwargs_)
supermod.Value.subclass = ValueSub
# end class ValueSub


class AuthorityDetailsSub(supermod.AuthorityDetails):
    def __init__(self, id=None, Name=None, Notes=None, **kwargs_):
        super(AuthorityDetailsSub, self).__init__(id, Name, Notes,  **kwargs_)
supermod.AuthorityDetails.subclass = AuthorityDetailsSub
# end class AuthorityDetailsSub


class DataSourceDetailsSub(supermod.DataSourceDetails):
    def __init__(self, id=None, type_=None, Name=None, Notes=None, **kwargs_):
        super(DataSourceDetailsSub, self).__init__(id, type_, Name, Notes,  **kwargs_)
supermod.DataSourceDetails.subclass = DataSourceDetailsSub
# end class DataSourceDetailsSub


class MeasurementTechniqueDetailsSub(supermod.MeasurementTechniqueDetails):
    def __init__(self, id=None, Name=None, Notes=None, **kwargs_):
        super(MeasurementTechniqueDetailsSub, self).__init__(id, Name, Notes,  **kwargs_)
supermod.MeasurementTechniqueDetails.subclass = MeasurementTechniqueDetailsSub
# end class MeasurementTechniqueDetailsSub


class ParameterDetailsSub(supermod.ParameterDetails):
    def __init__(self, id=None, Name=None, Units=None, Unitless=None, Notes=None, **kwargs_):
        super(ParameterDetailsSub, self).__init__(id, Name, Units, Unitless, Notes,  **kwargs_)
supermod.ParameterDetails.subclass = ParameterDetailsSub
# end class ParameterDetailsSub


class PropertyDetailsSub(supermod.PropertyDetails):
    def __init__(self, id=None, type_=None, Name=None, Units=None, Unitless=None, Notes=None, **kwargs_):
        super(PropertyDetailsSub, self).__init__(id, type_, Name, Units, Unitless, Notes,  **kwargs_)
supermod.PropertyDetails.subclass = PropertyDetailsSub
# end class PropertyDetailsSub


class SourceDetailsSub(supermod.SourceDetails):
    def __init__(self, id=None, type_=None, Name=None, Notes=None, **kwargs_):
        super(SourceDetailsSub, self).__init__(id, type_, Name, Notes,  **kwargs_)
supermod.SourceDetails.subclass = SourceDetailsSub
# end class SourceDetailsSub


class SpecimenDetailsSub(supermod.SpecimenDetails):
    def __init__(self, id=None, type_=None, Name=None, Notes=None, Geometry=None, **kwargs_):
        super(SpecimenDetailsSub, self).__init__(id, type_, Name, Notes, Geometry,  **kwargs_)
supermod.SpecimenDetails.subclass = SpecimenDetailsSub
# end class SpecimenDetailsSub


class TestConditionDetailsSub(supermod.TestConditionDetails):
    def __init__(self, id=None, ParameterValue=None, Notes=None, **kwargs_):
        super(TestConditionDetailsSub, self).__init__(id, ParameterValue, Notes,  **kwargs_)
supermod.TestConditionDetails.subclass = TestConditionDetailsSub
# end class TestConditionDetailsSub


class ParentMaterialTypeSub(supermod.ParentMaterialType):
    def __init__(self, id=None, **kwargs_):
        super(ParentMaterialTypeSub, self).__init__(id,  **kwargs_)
supermod.ParentMaterialType.subclass = ParentMaterialTypeSub
# end class ParentMaterialTypeSub


class SymbolTypeSub(supermod.SymbolType):
    def __init__(self, subscript='1', valueOf_=None, **kwargs_):
        super(SymbolTypeSub, self).__init__(subscript, valueOf_,  **kwargs_)
supermod.SymbolType.subclass = SymbolTypeSub
# end class SymbolTypeSub


class GraphTypeSub(supermod.GraphType):
    def __init__(self, anytypeobjs_=None, **kwargs_):
        super(GraphTypeSub, self).__init__(anytypeobjs_,  **kwargs_)
supermod.GraphType.subclass = GraphTypeSub
# end class GraphTypeSub


class DataTypeSub(supermod.DataType):
    def __init__(self, format=None, valueOf_=None, **kwargs_):
        super(DataTypeSub, self).__init__(format, valueOf_,  **kwargs_)
supermod.DataType.subclass = DataTypeSub
# end class DataTypeSub


class DataType1Sub(supermod.DataType1):
    def __init__(self, format=None, valueOf_=None, **kwargs_):
        super(DataType1Sub, self).__init__(format, valueOf_,  **kwargs_)
supermod.DataType1.subclass = DataType1Sub
# end class DataType1Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MatML_Doc'
        rootClass = supermod.MatML_Doc
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MatML_Doc'
        rootClass = supermod.MatML_Doc
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MatML_Doc'
        rootClass = supermod.MatML_Doc
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'MatML_Doc'
        rootClass = supermod.MatML_Doc
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from MatML_api import *\n\n')
        sys.stdout.write('import MatML_api as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
