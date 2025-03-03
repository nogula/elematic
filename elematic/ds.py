"""Defines the data structure of the MatML 3.1 schema used in elematic."""
# pylint: disable=too-many-lines

from __future__ import annotations

from decimal import Decimal
from enum import Enum

from typing_extensions import Self
from pydantic import BaseModel, ConfigDict, model_validator
from xsdata_pydantic.fields import field


class _DSModel(BaseModel):
    """Base class for all elements in the elematic.ds namespace. Changes the pydantic
    BaseModel"""

    model_config = ConfigDict(defer_build=True, validate_assignment=True)


class AssociationDetails(_DSModel):
    """AssociationDetails class represents the content model for association details in
    a complex material system.

    It contains a description of the relationship of a component to another component,
    such as in composites, welds, or multilayer materials.

    Attributes:
        associate (str, optional): The name of a component's associate. For example,
            in a TiC coating on AISI 1018 steel coupons, the associate of the steel is
            the "titanium carbide coating". Defaults to None.
        relationship (str, optional): A description of the relationship between a
            component and its associate. For example, the relationship of the "steel"
            component to the "titanium carbide coating" is that the steel is the
            "substrate" for the coating. Defaults to None.
        notes (str, optional): Any additional information concerning the association.
            Defaults to None.
    """

    associate: None | str = field(
        default=None,
        metadata={
            "name": "Associate",
            "type": "Element",
        },
    )
    relationship: None | str = field(
        default=None,
        metadata={
            "name": "Relationship",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class ChemicalElementSymbol(Enum):
    """Enum which provides the valid strings representing chemical elements, which may
    be used in the [elematic.ds.Element.Symbol][] element.
    """

    H = "H"
    HE = "He"
    LI = "Li"
    BE = "Be"
    B = "B"
    C = "C"
    N = "N"
    O = "O"
    F = "F"
    NE = "Ne"
    NA = "Na"
    MG = "Mg"
    AL = "Al"
    SI = "Si"
    P = "P"
    S = "S"
    CL = "Cl"
    AR = "Ar"
    K = "K"
    CA = "Ca"
    SC = "Sc"
    TI = "Ti"
    V = "V"
    CR = "Cr"
    MN = "Mn"
    FE = "Fe"
    CO = "Co"
    NI = "Ni"
    CU = "Cu"
    ZN = "Zn"
    GA = "Ga"
    GE = "Ge"
    AS = "As"
    SE = "Se"
    BR = "Br"
    KR = "Kr"
    RB = "Rb"
    SR = "Sr"
    Y = "Y"
    ZR = "Zr"
    NB = "Nb"
    MO = "Mo"
    TC = "Tc"
    RU = "Ru"
    RH = "Rh"
    PD = "Pd"
    AG = "Ag"
    CD = "Cd"
    IN = "In"
    SN = "Sn"
    SB = "Sb"
    TE = "Te"
    I = "I"
    XE = "Xe"
    CS = "Cs"
    BA = "Ba"
    LA = "La"
    CE = "Ce"
    PR = "Pr"
    ND = "Nd"
    PM = "Pm"
    SM = "Sm"
    EU = "Eu"
    GD = "Gd"
    TB = "Tb"
    DY = "Dy"
    HO = "Ho"
    ER = "Er"
    TM = "Tm"
    YB = "Yb"
    LU = "Lu"
    HF = "Hf"
    TA = "Ta"
    W = "W"
    RE = "Re"
    OS = "Os"
    IR = "Ir"
    PT = "Pt"
    AU = "Au"
    HG = "Hg"
    TL = "Tl"
    PB = "Pb"
    BI = "Bi"
    PO = "Po"
    AT = "At"
    RN = "Rn"
    FR = "Fr"
    RA = "Ra"
    AC = "Ac"
    TH = "Th"
    PA = "Pa"
    U = "U"
    NP = "Np"
    PU = "Pu"
    AM = "Am"
    CM = "Cm"
    BK = "Bk"
    CF = "Cf"
    ES = "Es"
    FM = "Fm"
    MD = "Md"
    NO = "No"
    LR = "Lr"
    RF = "Rf"
    DB = "Db"
    SG = "Sg"
    BH = "Bh"
    HS = "Hs"
    MT = "Mt"
    UUN = "Uun"
    UUU = "Uuu"
    UUB = "Uub"
    UUQ = "Uuq"
    UUH = "Uuh"
    UUO = "Uuo"


class CurrencyCode(Enum):
    """Enumerates the ISO4217 currency codes."""

    AFA = "AFA"
    ALL = "ALL"
    AMD = "AMD"
    ANG = "ANG"
    AOA = "AOA"
    ARS = "ARS"
    ATS = "ATS"
    AUD = "AUD"
    AWG = "AWG"
    AZM = "AZM"
    BAM = "BAM"
    BBD = "BBD"
    BDT = "BDT"
    BEF = "BEF"
    BGL = "BGL"
    BGN = "BGN"
    BHD = "BHD"
    BIF = "BIF"
    BMD = "BMD"
    BND = "BND"
    BOB = "BOB"
    BOV = "BOV"
    BRL = "BRL"
    BSD = "BSD"
    BTN = "BTN"
    BWP = "BWP"
    BYB = "BYB"
    BYR = "BYR"
    BZD = "BZD"
    CAD = "CAD"
    CDF = "CDF"
    CHF = "CHF"
    CLF = "CLF"
    CLP = "CLP"
    CNY = "CNY"
    COP = "COP"
    CRC = "CRC"
    CUP = "CUP"
    CVE = "CVE"
    CYP = "CYP"
    CZK = "CZK"
    DEM = "DEM"
    DJF = "DJF"
    DKK = "DKK"
    DOP = "DOP"
    DZD = "DZD"
    EEK = "EEK"
    EGP = "EGP"
    ERN = "ERN"
    ESP = "ESP"
    ETB = "ETB"
    EUR = "EUR"
    FIM = "FIM"
    FJD = "FJD"
    FKP = "FKP"
    FRF = "FRF"
    GBP = "GBP"
    GEL = "GEL"
    GHC = "GHC"
    GIP = "GIP"
    GMD = "GMD"
    GNF = "GNF"
    GRD = "GRD"
    GTQ = "GTQ"
    GWP = "GWP"
    GYD = "GYD"
    HKD = "HKD"
    HNL = "HNL"
    HRK = "HRK"
    HTG = "HTG"
    HUF = "HUF"
    IDR = "IDR"
    IEP = "IEP"
    ILS = "ILS"
    INR = "INR"
    IQD = "IQD"
    IRR = "IRR"
    ISK = "ISK"
    ITL = "ITL"
    JMD = "JMD"
    JOD = "JOD"
    JPY = "JPY"
    KES = "KES"
    KGS = "KGS"
    KHR = "KHR"
    KMF = "KMF"
    KPW = "KPW"
    KRW = "KRW"
    KWD = "KWD"
    KYD = "KYD"
    KZT = "KZT"
    LAK = "LAK"
    LBP = "LBP"
    LKR = "LKR"
    LRD = "LRD"
    LSL = "LSL"
    LTL = "LTL"
    LUF = "LUF"
    LVL = "LVL"
    LYD = "LYD"
    MAD = "MAD"
    MDL = "MDL"
    MGF = "MGF"
    MKD = "MKD"
    MMK = "MMK"
    MNT = "MNT"
    MOP = "MOP"
    MRO = "MRO"
    MTL = "MTL"
    MUR = "MUR"
    MVR = "MVR"
    MWK = "MWK"
    MXN = "MXN"
    MXV = "MXV"
    MYR = "MYR"
    MZM = "MZM"
    NAD = "NAD"
    NGN = "NGN"
    NIO = "NIO"
    NLG = "NLG"
    NOK = "NOK"
    NPR = "NPR"
    NZD = "NZD"
    OMR = "OMR"
    PAB = "PAB"
    PEN = "PEN"
    PGK = "PGK"
    PHP = "PHP"
    PKR = "PKR"
    PLN = "PLN"
    PTE = "PTE"
    PYG = "PYG"
    QAR = "QAR"
    ROL = "ROL"
    RUB = "RUB"
    RUR = "RUR"
    RWF = "RWF"
    SAR = "SAR"
    SBD = "SBD"
    SCR = "SCR"
    SDD = "SDD"
    SEK = "SEK"
    SGD = "SGD"
    SHP = "SHP"
    SIT = "SIT"
    SKK = "SKK"
    SLL = "SLL"
    SOS = "SOS"
    SRG = "SRG"
    STD = "STD"
    SVC = "SVC"
    SYP = "SYP"
    SZL = "SZL"
    THB = "THB"
    TJR = "TJR"
    TMM = "TMM"
    TND = "TND"
    TOP = "TOP"
    TPE = "TPE"
    TRL = "TRL"
    TTD = "TTD"
    TWD = "TWD"
    TZS = "TZS"
    UAH = "UAH"
    UGX = "UGX"
    USD = "USD"
    UYU = "UYU"
    UZS = "UZS"
    VEB = "VEB"
    VND = "VND"
    VUV = "VUV"
    WST = "WST"
    XAF = "XAF"
    XCD = "XCD"
    XDR = "XDR"
    XOF = "XOF"
    XPF = "XPF"
    YER = "YER"
    YUM = "YUM"
    ZAR = "ZAR"
    ZMK = "ZMK"
    ZWD = "ZWD"


class DataFormat(Enum):
    """Enumerates allowable dataformats used by the `format` attributes of the
    [elematic.ds.Value][], [elematic.ds.ParameterValue][],
    [elematic.ds.ParameterValue.Data][],  and [elematic.ds.PropertyData.Data][]
    elements.

    Attributes:
        FLOAT: float
        INTEGER: int
        STRING: str
        EXPONENTIAL: float
        MIXED: str

    Notes:
        `MIXED` is only used for a group of data where each individual member of the
        group can be given a unique format."""

    FLOAT = "float"
    INTEGER = "integer"
    STRING = "string"
    EXPONENTIAL = "exponential"
    MIXED = "mixed"


class Geometry(_DSModel):
    """Descibes the geometry of the bulk material, component, or specimen.

    Attributes:
        shape (str): A string describing the shape of the bulk material or component.
        dimensions (str, optional): A string describing the dimensions of the bulk
            material or component. Defaults to None.
        orientation (str, optional): A string describing the orientation of the bulk
            material or component. Defaults to None.
        notes (str, optional): Contains any additional information concerning the
            geometry. Defaults to None.
    """

    shape: str = field(
        metadata={
            "name": "Shape",
            "type": "Element",
            "required": True,
        }
    )
    dimensions: None | str = field(
        default=None,
        metadata={
            "name": "Dimensions",
            "type": "Element",
        },
    )
    orientation: None | str = field(
        default=None,
        metadata={
            "name": "Orientation",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class Graphs(_DSModel):
    """Contains [elematic.ds.Graphs.Graph][] elements.

    Attributes:
        graph (list[Graphs.Graph]): Contains [elematic.ds.Graphs.Graph][] elements.
    """

    graph: list[Graphs.Graph] = field(
        default_factory=list,
        metadata={
            "name": "Graph",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    class Graph(_DSModel):
        """Contains a single SVG graph element. Graph uses the W3C's Scalable Vector
        Graphics markup language (SVG) for describing two dimensional graphics and
        allows for three types of graphical objects: vector graphics shapes, images, and
        text. Graph must occur one or more times within the Graphs element. For more
        information concerning SVG, see the documentation at http://www.w3.org/TR/SVG/.

        Attributes:
            w3_org_2000_svg_element (list[object]): Contains a single SVG graph element.
        """

        w3_org_2000_svg_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "http://www.w3.org/2000/svg",
            },
        )


class Name(_DSModel):
    """Represents a name with an optional authority attribute.

    Attributes:
        value (str): A string representing the name. This attribute is required.
        authority (str, optional): An optional attribute for identifying an
            authoritative source of names in the context in which the Name element is
            used. Defaults to None.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    authority: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class Source(_DSModel):
    """The source of the bulk material or component.
    Attributes:
        source (str, optional): An optional attribute representing the source of the
            bulk material or component. Defaults to None.
    """

    source: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class Specification(_DSModel):
    """Represents a specification for bulk material or component. It contains a string
    value representing the specification and an optional attribute, authority,
    for identifying an authoritative source of specifications.

    Attributes:
        value (str): The specification content. This field is required.
        authority (str, optional): An optional attribute for identifying an
            authoritative source of specifications. Defaults to None.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    authority: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class UncertaintyScale(Enum):
    """
    An enumeration representing different scales of uncertainty.

    Attributes:
        LINEAR (str): Represents a linear scale of uncertainty.
        LOGARITHMIC (str): Represents a logarithmic scale of uncertainty.
    """

    LINEAR = "Linear"
    LOGARITHMIC = "Logarithmic"


class Unitless(_DSModel):
    """An empty element used whenever a property, parameter, or uncertainty value has
    no units."""


class AuthorityDetails(_DSModel):
    """This class represents the AuthorityDetails element, which contains a description
    of an authority referenced by other elements, such as the Specification and Name
    elements. An authority is typically an organization that is the authoritative
    source of information about the element that is referencing it.

    Attributes:
        name (Name): The name of the Authority. This attribute is required and must
            occur once and only once within the AuthorityDetails element.
        notes (str, optional): Any additional information concerning the parameter.
            Defaults to None.
        id (str): A unique identifier for the AuthorityDetails element. This attribute
            is required and must be unique among id attributes assigned elsewhere in
            a MatML document.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class Class(_DSModel):
    """The material class to which the Material belongs. The Class can either have a
    Name or ParentMaterial element.

    Attributes:
        name (Name, optional): Contains a string representing the name of the
            material's class. Defaults to None.
        parent_material (list[Class.ParentMaterial]): A list of references to parent
            material. Defaults to an empty list.
        parent_sub_class (list[Class]): A list of references to parent sub-class.
    """

    name: None | Name = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    parent_material: list[Class.ParentMaterial] = field(
        default_factory=list,
        metadata={
            "name": "ParentMaterial",
            "type": "Element",
        },
    )
    parent_sub_class: list[Class] = field(
        default_factory=list,
        metadata={
            "name": "ParentSubClass",
            "type": "Element",
        },
    )

    class ParentMaterial(_DSModel):

        id: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


class DataSourceDetails(_DSModel):
    """Describes the form of the bulk material or component.

    Attributes:
        description (Name): Contains a string representing the description of the
            bulk material or component's form.
        geometry (Geometry, optional): Contains a description of the geometry of the
            bulk material or component. Defaults to None.
        notes (str, optional): Contains any additional information concerning the
            form. Defaults to None.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


class Form(_DSModel):
    """Describes the form of the bulk material or component.

    Attributes:
        description (Name): Contains a string representing the description of the
            bulk material or component's form.
        geometry (Geometry, optional): Contains a description of the geometry of the
            bulk material or component. Defaults to None.
        notes (str, optional): Contains any additional information concerning the
            form. Defaults to None.
    """

    description: Name = field(
        metadata={
            "name": "Description",
            "type": "Element",
            "required": True,
        }
    )
    geometry: None | Geometry = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class GlossaryTerm(_DSModel):
    """Provides the definition of a term in the glossary.

    Attributes:
        name (Name): Contains the name of the term.
        definition (str): Contains the definition of the term.
        abbreviation (list[str], optional): Contains any abbreviations for the term.
            Defaults to an empty list.
        synonym (list[str], optional): Contains any synonyms for the term. Defaults to
            an empty list.
        notes (str, optional): Any additional information concerning the term.
            Defaults to None.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    definition: str = field(
        metadata={
            "name": "Definition",
            "type": "Element",
            "required": True,
        }
    )
    abbreviation: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Abbreviation",
            "type": "Element",
        },
    )
    synonym: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Synonym",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class MeasurementTechniqueDetails(_DSModel):
    """Describes the measurement technique referenced by the
    [elematic.ds.PropertyData][] element.

    Attributes:
        name (Name): Contains the name of the measurement technique.
        id (str): A unique identifier for the MeasurementTechniqueDetails element.
            This attribute may be arbitrarily assigned but must be unique among id
            attributes assigned elsewhere in a MatML document.
        notes (str, optional): Any additional information concerning the measurement
            technique. Defaults to None.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class SourceDetails(_DSModel):
    """Contains the name of the source of the component.

    Attributes:
        name (Name): Contains the name of the source.
        id (str): A unique identifier for the SourceDetails element. This attribute
            may be arbitrarily assigned but must be unique among id attributes
            assigned elsewhere in a MatML document.
        notes (str, optional): Any additional information concerning the source.
            Defaults to None.
        type_value (str, optional): The type of the source (e.g., unpublished report,
            journal, handbook, etc.). Defaults to None.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


class SpecimenDetails(_DSModel):
    """Describes a specimen referenced by the [elematic.ds.PropertyData][] element.

    Attributes:
        id (str): A unique identifier for the SpecimenDetails element. This attribute
            may be arbitrarily assigned but must be unique among id attributes
            assigned elsewhere in a MatML document.
        name (Name, optional): Contains the name of the specimen. Defaults to None.
        notes (str, optional): Any additional information concerning the specimen.
            Defaults to None.
        geometry (Geometry, optional): Contains a description of the geometry of the
            component. Defaults to None.
        type_value (str, optional): The type of the specimen (e.g., "cylindrical,"
            "rectangular," "full cross-section," "pressed," etc.). Defaults to None.
    """

    name: None | Name = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    geometry: None | Geometry = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )


class Unit(_DSModel):
    """Defines a unit of measurement. Unit has the choice of two attributes: name or
    currency.

    Attributes:
        name (str, optional): Contains the name of the unit. Defaults to None.
        currency (CurrencyCode, optional): Contains the currency code of the unit.
            Defaults to None.
        power (Decimal, optional): Contains the power of the unit. Defaults to None.
        description (str, optional): Contains a description of the unit. Defaults to
            None.

    Notes:
        Multiple Unit elements are multiplied together to form units. Division is
        specified by setting the power attribute of the Unit to "-1".
    """

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
        },
    )
    currency: None | CurrencyCode = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
        },
    )
    power: None | Decimal = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class Value(_DSModel):
    """Contains a string representation of a value, and a format attribute.

    Attributes:
        value (str): A string representing a value.
        format (DataFormat): The format of the value.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    format: DataFormat = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class Glossary(_DSModel):
    """Contains one or more [elematic.ds.GlossaryTerm][] elements.

    Attributes:
        term (list[GlossaryTerm]): Contains one or more [elematic.ds.GlossaryTerm][].
    """

    term: list[GlossaryTerm] = field(
        default_factory=list,
        metadata={
            "name": "Term",
            "type": "Element",
            "min_occurs": 1,
        },
    )


class Units(_DSModel):
    """
    A class to represent a collection of units with associated metadata.

    Attributes:
        unit (list[Unit]): A list of Unit objects.
        system (str, optional): The system attribute. Defaults to None.
        factor (float, optional): The factor attribute. Defaults to None.
        name (str, optional): The name attribute. Defaults to None.
        description (str, optional): The description attribute. Defaults to None.
    """

    unit: list[Unit] = field(
        default_factory=list,
        metadata={
            "name": "Unit",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    system: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    factor: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class ParameterDetails(_DSModel):
    """Provides the definition of a [elematic.ds.ParameterValue][] element.

    Attributes:
        name (Name): Contains the name of the parameter.
        id (str):  This attribute
            may be arbitrarily assigned but must be unique among id attributes
            assigned elsewhere in a MatML document.
        units (Units, optional): Describes the parameter's units. This attribute is
            mutually exclusive with `unitless`.
        unitless (Unitless, optional): Indicates that the parameter is unitless. This
            attribute is mutually exclusive with `units`.
        notes (str, optional): Contains any additional information concerning the
            parameter.

    Warning:
        Setting either of `units` or `unitless` to a non-None value will set the other
        to None.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    units: None | Units = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
        },
    )
    unitless: None | Unitless = field(
        default=None,
        metadata={
            "name": "Unitless",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @model_validator(mode="after")
    def check_units_or_unitless(self) -> Self:
        if self.units is None and self.unitless is None:
            raise ValueError("Either units or unitless must be provided.")
        if self.units is not None and self.unitless is not None:
            raise ValueError("One of units or unitless must be None.")
        return self

    def __setattr__(self, name, value):
        if name == "units" and value is not None:
            super().__setattr__("unitless", None)
        if name == "unitless" and value is not None:
            super().__setattr__("units", None)
        super().__setattr__(name, value)


class PropertyDetails(_DSModel):
    """Provides the defition of a [elematic.ds.PropertyData][] element.

    Attributes:
        name (Name): Contains the name of the property.
        id (str): A unique identifier for the PropertyDetails element. This attribute
            may be arbitrarily assigned but must be unique among id attributes
            assigned elsewhere in a MatML document.
        units (Units, optional): Describes the property's units. This attribute is
            mutually exclusive with `unitless`.
        unitless (Unitless, optional): Indicates that the property is unitless. This
            attribute is mutually exclusive with `units`.
        notes (str, optional): Contains any additional information concerning the
            property.

    Warning:
        Setting either of `units` or `unitless` to a non-None value will set the other
        to None.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    units: None | Units = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
        },
    )
    unitless: None | Unitless = field(
        default=None,
        metadata={
            "name": "Unitless",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )

    @model_validator(mode="after")
    def check_units_or_unitless(self) -> Self:
        if self.units is None and self.unitless is None:
            raise ValueError("Either units or unitless must be provided.")
        if self.units is not None and self.unitless is not None:
            raise ValueError("One of units or unitless must be None.")
        return self

    def __setattr__(self, name, value):
        if name == "units" and value is not None:
            super().__setattr__("unitless", None)
        if name == "unitless" and value is not None:
            super().__setattr__("units", None)
        super().__setattr__(name, value)


class Uncertainty(_DSModel):
    """Describes the measurement uncertainty of the data.

    Attributes:
        value (Value): Contains the value of the uncertainty.
        units (Units, optional): Contains the units for the value of the uncertainty.
            This attribute is mutually exclusive with `unitless`.
        unitless (Unitless, optional): Indicates if the value is unitless. This
            attribute is mutually exclusive with `units`.
        notes (str, optional): Contains any additional information concerning the
            uncertainty, such as a description of the evaluation of the uncertainty.
        scale (UncertaintyScale, optional): Represents the scale of the uncertainty.
        distribution_type (str, scale): The type of distribution, default is
            "Normal/Gaussian".
        num_std_dev (float, optional): Number of standard deviations, default is 2.0.
        percentile (float, optional): A value indicating the percentage of the data
            population value. If Percentile is not given then Value is interpreted as
            being an equal and unspecified deviation above and below the Property
            value(s).
        confidence_level (float, optional): The confidence level of the uncertainty.

    Warning:
        Setting either of `units` or `unitless` to a non-None value will set the other
        to None.
    """

    value: Value = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        }
    )
    units: None | Units = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
        },
    )
    unitless: None | Unitless = field(
        default=None,
        metadata={
            "name": "Unitless",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    scale: None | UncertaintyScale = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Element",
        },
    )
    distribution_type: None | str = field(
        default="Normal/Gaussian",
        metadata={
            "name": "DistributionType",
            "type": "Attribute",
        },
    )
    num_std_dev: None | float = field(
        default=2.0,
        metadata={
            "name": "Num_Std_Dev",
            "type": "Attribute",
        },
    )
    percentile: None | float = field(
        default=None,
        metadata={
            "name": "Percentile",
            "type": "Attribute",
        },
    )
    confidence_level: None | float = field(
        default=None,
        metadata={
            "name": "ConfidenceLevel",
            "type": "Attribute",
        },
    )

    @model_validator(mode="after")
    def check_units_or_unitless(self) -> Self:
        if self.units is None and self.unitless is None:
            raise ValueError("Either units or unitless must be provided.")
        if self.units is not None and self.unitless is not None:
            raise ValueError("One of units or unitless must be None.")
        return self

    def __setattr__(self, name, value):
        if name == "units" and value is not None:
            super().__setattr__("unitless", None)
        if name == "unitless" and value is not None:
            super().__setattr__("units", None)
        super().__setattr__(name, value)


class Concentration(_DSModel):
    """Defines the concentration of a [Compound][elematic.ds.Compound],
    [Element][elematic.ds.Element], or [PhaseComposition][elematic.ds.PhaseComposition].

    Attributes:
        value (Value): Contains the value of the concentration.
        units (Units): Contains the units for the value of the concentration.
        qualifier (list[str]): Contains any qualifier pertinent to the value of the
            concentration (e.g., "min," "max," etc.).
        uncertainty (list[Uncertainty]): Contains the measurement uncertainty(ies) of
            the data.
        notes (None | str): Contains any additional information concerning the
            concentration and may occur once or not at all within the Concentration
            element.
    """

    value: Value = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        }
    )
    units: Units = field(
        metadata={
            "name": "Units",
            "type": "Element",
            "required": True,
        }
    )
    qualifier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
        },
    )
    uncertainty: list[Uncertainty] = field(
        default_factory=list,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class DimensionalDetails(_DSModel):
    """Describes a dimensional characteristic (e.g., grain size, porosity, precipitate
    size and distribution, etc.) of the bulk material or component.

    Attributes:
        name (Name): Contains the name of the characteristic.
        value (Value): Contains the value of the dimensional characteristic.
        units (Units): Contains the units for the value of the dimensional
            characteristic.
        qualifier (Optional[str]): Contains any qualifier pertinent to the value of the
            dimensional characteristic (e.g., "min," "max," etc.).
        uncertainty (List[Uncertainty]): Contains the measurement uncertainty(ies) of
            the data.
        notes (Optional[str]): Contains any additional information concerning the dimensional
            DimensionalDetails element.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    value: Value = field(
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        }
    )
    units: Units = field(
        metadata={
            "name": "Units",
            "type": "Element",
            "required": True,
        }
    )
    qualifier: None | str = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
        },
    )
    uncertainty: list[Uncertainty] = field(
        default_factory=list,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class ParameterValue(_DSModel):
    """Represents the value of a parameter with associated metadata.

    Attributes:
        data (ParameterValue.Data): Contains the property data.
        uncertainty (list[Uncertainty]): Contains the measurement uncertainties of the
            data.
        qualifier (list[str]): Contains any qualifiers pertinent to the data.
        notes (str, optional): Contains any additional information concerning the
            property data.
        parameter (str): References an id attribute specified in a ParameterDetails
            element.
        format (DataFormat): Indicates the format of the value.
    """

    data: ParameterValue.Data = field(
        metadata={
            "name": "Data",
            "type": "Element",
            "required": True,
        }
    )
    uncertainty: list[Uncertainty] = field(
        default_factory=list,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
        },
    )
    qualifier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    parameter: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    format: DataFormat = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    class Data(_DSModel):
        """Contains the property data.

        Attributes:
            value (str): The value of the data.
            format (DataFormat, optional): The format of the value.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        format: None | DataFormat = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )


class Element(_DSModel):
    """Represents a chemical element with its symbol, concentration, and notes.
    symbol (Element.Symbol): Symbol of the chemical element. It must be one of the
        strings enumerated by the ChemicalElementSymbol datatype.
    concentration (Concentration, optional): Concentration of the element.
    notes (str, optional): Additional information concerning the element.
    """

    symbol: Element.Symbol = field(
        metadata={
            "name": "Symbol",
            "type": "Element",
            "required": True,
        }
    )
    concentration: None | Concentration = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )

    class Symbol(_DSModel):
        """Symbol of the chemical element. It must be one of the strings enumerated by
        the ChemicalElementSymbol datatype.

        Attributes:
            value (ChemicalElementSymbol): The symbol of the chemical element.
            subscript (str): The subscript of the element, default is "1".
        """

        value: ChemicalElementSymbol = field(
            metadata={
                "required": True,
            }
        )
        subscript: str = field(
            default="1",
            metadata={
                "type": "Attribute",
            },
        )


class ProcessingDetails(_DSModel):
    """Represents a processing step for bulk material or component.

    Attributes:
        name (Name): The name of the processing step.
        parameter_value (list[ParameterValue]): A list of parameter values under which
            the processing step occurred.
        result (str, optional): A description of the outcome or result of the processing
            step.
        notes (str, optional): Any additional information concerning the processing
            step.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    parameter_value: list[ParameterValue] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
        },
    )
    result: None | str = field(
        default=None,
        metadata={
            "name": "Result",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class PropertyData(_DSModel):
    """Represents property data.

    Attributes:
        data (PropertyData.Data): Contains the property data.
        uncertainty (list[Uncertainty]): Contains the measurement uncertainty(ies)
            of the data.
        qualifier (list[str]): Contains any qualifier(s) pertinent to the data (e.g.
            "min," "max," etc.).
        parameter_value (list[ParameterValue]): Contains the value(s) of a parameter
            under which the data were determined.
        notes (None | str): Contains any additional information concerning the
            property data.
        property (str): Required attribute that references an id attribute specified
            in a PropertyDetails element.
        technique (None | str): Optional attribute that references an id attribute
            specified in a MeasurementTechniqueDetails element.
        source (None | str): Optional attribute that references an id attribute
            specified in a DataSourceDetails element.
        specimen (None | str): Optional attribute that references an id attribute
            specified in a SpecimenDetails element.
        test (None | str): Optional attribute that references an id attribute
            specified in a TestConditionDetails element.
        delimiter (str): Specifies the delimiter that separates multiple values in
            the Data, Qualifier, Uncertainty, and ParameterValue elements. The
            default value is a comma (',').
        quote (None | str): Specifies the string that is used to quote values in the
            Data, Qualifier, Uncertainty, and ParameterValue elements. The default
            value is a null string, which is equivalent to saying that the values
            are not quoted.
    """

    data: PropertyData.Data = field(
        metadata={
            "name": "Data",
            "type": "Element",
            "required": True,
        }
    )
    uncertainty: list[Uncertainty] = field(
        default_factory=list,
        metadata={
            "name": "Uncertainty",
            "type": "Element",
        },
    )
    qualifier: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Qualifier",
            "type": "Element",
        },
    )
    parameter_value: list[ParameterValue] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    property: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    technique: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    source: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    specimen: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    test: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    delimiter: str = field(
        default=",",
        metadata={
            "type": "Attribute",
            "min_length": 1,
            "white_space": "preserve",
        },
    )
    quote: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )

    class Data(_DSModel):
        """
        Data class that represents the data values used by [elematic.ds.PropertyData][].

        Attributes:
            value (str): A string value with a default of an empty string.
            format (DataFormat): A DataFormat object.

        Note:
            This class is distinct from [elematic.ds.ParameterValue.Data][], in that the
            `format` attribute herein is required, whereas in
            [elematic.ds.ParameterValue][], it is optional.
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        format: DataFormat = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


class TestConditionDetails(_DSModel):
    """Describes a test condition referenced by the [elematic.ds.PropertyData][]
    element.

    Attributes:
        parameter_value (list[ParameterValue]): Contains the value(s) of a parameter,
            i.e., a test condition.
        notes (str, optional): Contains any additional information concerning the test
            conditions.
        id (str): A required attribute that must be unique among id attributes assigned
            elsewhere in a MatML document.
    """

    parameter_value: list[ParameterValue] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class Compound(_DSModel):
    """The elemental description of a chemical compound.

    Attributes:
        element (list[Element]): Contains the description of a chemical element.
        concentration (Concentration, optional): Contains the concentration of the
            compound.
        notes (str, optional): Contains any additional information concerning the
            compound.
    """

    element: list[Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    concentration: None | Concentration = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class Metadata(_DSModel):
    """Provides the metadata information for a [MatML][elematic.ds.MatMLDoc] document.

    Attributes:
        authority_details (list[AuthorityDetails]): Contains a description of
            authorities referenced from the Specification and Name elements.
        data_source_details (list[DataSourceDetails]): Contains a description of a data
            source referenced using the PropertyData element.
        measurement_technique_details (list[MeasurementTechniqueDetails]): Contains a
            description of a measurement technique referenced using the PropertyData
            element.
        parameter_details (list[ParameterDetails]): Contains a description of a
            parameter referenced using
            the PropertyData element.
        property_details (list[PropertyDetails]): Contains a description of a property
            for which materials data are encoded using the PropertyData element.
        source_details (list[SourceDetails]): Contains a description of the source of a
            material or component.
        specimen_details (list[SpecimenDetails]): Contains a description of a specimen
            referenced using the PropertyData element.
        test_condition_details (list[TestConditionDetails]): Contains a description of
            the test condition(s) referenced using the PropertyData element.
    """

    authority_details: list[AuthorityDetails] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityDetails",
            "type": "Element",
        },
    )
    data_source_details: list[DataSourceDetails] = field(
        default_factory=list,
        metadata={
            "name": "DataSourceDetails",
            "type": "Element",
        },
    )
    measurement_technique_details: list[MeasurementTechniqueDetails] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementTechniqueDetails",
            "type": "Element",
        },
    )
    parameter_details: list[ParameterDetails] = field(
        default_factory=list,
        metadata={
            "name": "ParameterDetails",
            "type": "Element",
        },
    )
    property_details: list[PropertyDetails] = field(
        default_factory=list,
        metadata={
            "name": "PropertyDetails",
            "type": "Element",
        },
    )
    source_details: list[SourceDetails] = field(
        default_factory=list,
        metadata={
            "name": "SourceDetails",
            "type": "Element",
        },
    )
    specimen_details: list[SpecimenDetails] = field(
        default_factory=list,
        metadata={
            "name": "SpecimenDetails",
            "type": "Element",
        },
    )
    test_condition_details: list[TestConditionDetails] = field(
        default_factory=list,
        metadata={
            "name": "TestConditionDetails",
            "type": "Element",
        },
    )

    @model_validator(mode="after")
    def check_unique_ids(self) -> Self:
        """Verify that all id attributes are unique between the different elements."""
        # Collect all IDs from the different elements
        ids = (
            [authority.id for authority in self.authority_details]
            + [data_source.id for data_source in self.data_source_details]
            + [
                measurement_technique.id
                for measurement_technique in self.measurement_technique_details
            ]
            + [parameter.id for parameter in self.parameter_details]
            + [property.id for property in self.property_details]
            + [source.id for source in self.source_details]
            + [specimen.id for specimen in self.specimen_details]
            + [test.id for test in self.test_condition_details]
        )

        # Check if all IDs are unique
        if len(ids) != len(set(ids)):
            raise ValueError("Duplicate id attributes found across different elements.")

        return self


class PhaseComposition(_DSModel):
    """Represents a phase that comprises the bulk material or component.

    Attributes:
        name (Name): The name of the phase.
        concentration (Concentration, optional): The concentration of the phase.
        property_data (list[PropertyData]): Property data for the phase.
        notes (str, optional): Any additional information concerning the phase.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    concentration: None | Concentration = field(
        default=None,
        metadata={
            "name": "Concentration",
            "type": "Element",
        },
    )
    property_data: list[PropertyData] = field(
        default_factory=list,
        metadata={
            "name": "PropertyData",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class ChemicalComposition(_DSModel):
    """Describes the compounds or elements that comprise the bulk material or component.

    Attributes:
        compound (list[Compound], optional): A list of Compound elements. This attribute
            is mutually exclusive with `element`.
        element (list[Element], optional): A list of Element elements. This attribute is
            mutually exclusive with `compound`.

    Warning:
        Setting either of `compound` or `element` to a non-empty list will set the other
        to an empty list.
    """

    compound: list[Compound] = field(
        default_factory=list,
        metadata={
            "name": "Compound",
            "type": "Element",
        },
    )
    element: list[Element] = field(
        default_factory=list,
        metadata={
            "name": "Element",
            "type": "Element",
        },
    )

    @model_validator(mode="after")
    def check_compound_or_element(self) -> Self:
        if not self.compound and not self.element:
            raise ValueError("At least one Compound or Element must be provided.")
        if self.compound and self.element:
            raise ValueError("Only one of Compound or Element may be provided.")
        return self

    def __setattr__(self, name, value):
        if name == "compound" and value is not None:
            super().__setattr__("element", [])
        if name == "element" and value is not None:
            super().__setattr__("compound", [])
        super().__setattr__(name, value)


class Characterization(_DSModel):
    """Describes the chemical composition of the bulk material or component.

    Attributes:
        formula (str): A string representation of the chemical formula for the bulk
            material or component.
        chemical_composition (ChemicalComposition, optional): A description of the
            compounds and elements that comprise the bulk material or component.
        phase_composition (list[PhaseComposition]): A description of the phases that
            comprise the bulk material or component.
        dimensional_details (list[DimensionalDetails]): Information relating to
            component or bulk precipitate size and distribution, etc.
        notes (str, optional): Any additional information concerning the
            Characterization.
    """

    formula: str = field(
        metadata={
            "name": "Formula",
            "type": "Element",
            "required": True,
        }
    )
    chemical_composition: None | ChemicalComposition = field(
        default=None,
        metadata={
            "name": "ChemicalComposition",
            "type": "Element",
        },
    )
    phase_composition: list[PhaseComposition] = field(
        default_factory=list,
        metadata={
            "name": "PhaseComposition",
            "type": "Element",
        },
    )
    dimensional_details: list[DimensionalDetails] = field(
        default_factory=list,
        metadata={
            "name": "DimensionalDetails",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class BulkDetails(_DSModel):
    """Describes the bulk material.

    Attributes:
        name (Name): Contains the material's name and has one optional attribute,
        class_value (list[Class], optional): Contains the material's class.
        subclass (list[Class], optional): Contains the material's subclass(es).
        specification (list[Specification], optional): Contains the material's
            specification(s).
        source (Source, optional): Contains the name of the source of the material.
        form (Form, optional): Describes the form of the material.
        processing_details (list[ProcessingDetails], optional): Contains a description
            of a processing step for the material.
        characterization (Characterization, optional): Contains the characterization.
        property_data (list[PropertyData], optional): Contains the property data for the
            material.
        notes (str, optional): Contains any additional information concerning the bulk
            material.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    class_value: list[Class] = field(
        default_factory=list,
        metadata={
            "name": "Class",
            "type": "Element",
        },
    )
    subclass: list[Class] = field(
        default_factory=list,
        metadata={
            "name": "Subclass",
            "type": "Element",
        },
    )
    specification: list[Specification] = field(
        default_factory=list,
        metadata={
            "name": "Specification",
            "type": "Element",
        },
    )
    source: None | Source = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
        },
    )
    form: None | Form = field(
        default=None,
        metadata={
            "name": "Form",
            "type": "Element",
        },
    )
    processing_details: list[ProcessingDetails] = field(
        default_factory=list,
        metadata={
            "name": "ProcessingDetails",
            "type": "Element",
        },
    )
    characterization: None | Characterization = field(
        default=None,
        metadata={
            "name": "Characterization",
            "type": "Element",
        },
    )
    property_data: list[PropertyData] = field(
        default_factory=list,
        metadata={
            "name": "PropertyData",
            "type": "Element",
        },
    )
    notes: None | str = field(
        default=None,
        metadata={
            "name": "Notes",
            "type": "Element",
        },
    )


class ComponentDetails(_DSModel):
    """Contains a description of a component within the bulk material and is used to
    support encoding of information for complex materials systems such as composites.

    Attributes:
        name (Name): Contains the component's name.
        class_value (list[Class]): Contains the component's material class.
        subclass (list[Class]): Contains the component's material subclass(es).
        specification (list[Specification]): Contains the component's specification(s).
        source (Source, optional): Contains the name of the source of the component.
        form (Form, optional): Contains the form of the component.
        processing_details (list[ProcessingDetails]): Contains a description of a
            processing step for the component.
        characterization (Characterization, optional): Contains the characterization of
            the component,
        property_data (list[PropertyData]): Contains the property data for the component.
        association_details (list[AssociationDetails]): Contains a description of a
            relationship of the component to another component.
        notes (str, optional): Contains any additional information concerning the
            component.
        component_details (list[ComponentDetails]): Contains a description of a
            component within the component.
        id (str, optional): An optional attribute used as an identification specifier
            for the component.
    """

    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
        }
    )
    class_value: list[Class] = field(
        default_factory=list,
        metadata={
            "name": "Class",
            "type": "Element",
        },
    )
    subclass: list[Class] = field(
        default_factory=list,
        metadata={
            "name": "Subclass",
            "type": "Element",
        },
    )
    specification: list[Specification] = field(
        default_factory=list,
        metadata={
            "name": "Specification",
            "type": "Element",
        },
    )
    source: None | Source = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
        },
    )
    form: None | Form = field(
        default=None,
        metadata={
            "name": "Form",
            "type": "Element",
        },
    )
    processing_details: list[ProcessingDetails] = field(
        default_factory=list,
        metadata={
            "name": "ProcessingDetails",
            "type": "Element",
        },
    )
    characterization: None | Characterization = field(
        default=None,
        metadata={
            "name": "Characterization",
            "type": "Element",
        },
    )
    property_data: list[PropertyData] = field(
        default_factory=list,
        metadata={
            "name": "PropertyData",
            "type": "Element",
        },
    )
    association_details: list[AssociationDetails] = field(
        default_factory=list,
        metadata={
            "name": "AssociationDetails",
            "type": "Element",
        },
    )
    component_details: list[ComponentDetails] = field(
        default_factory=list,
        metadata={
            "name": "ComponentDetails",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class Material(_DSModel):
    """Material class represents the content model for materials data.

    Attributes:
        bulk_details (BulkDetails): Contains a description of the bulk material.
        component_details (list[ComponentDetails], optional): Contains descriptions
            of components within the bulk material.
        graphs (Graphs, optional): Contains descriptions of two-dimensional graphics.
        glossary (Glossary, optional): Contains descriptions of the material and
            property terms used in the document.
        id (str, optional): An optional identification specifier for the material,
            useful for complex systems such as composite laminates.
        layers (int, optional): An optional attribute indicating the number of layers in
            complex systems such as composite laminates.
        local_frame_of_reference (str, optional): An optional identification specifier
            for the local material orientation relative to the global frame of
            reference, useful for complex systems such as anisotropic materials.
    """

    bulk_details: BulkDetails = field(
        metadata={
            "name": "BulkDetails",
            "type": "Element",
            "required": True,
        }
    )
    component_details: list[ComponentDetails] = field(
        default_factory=list,
        metadata={
            "name": "ComponentDetails",
            "type": "Element",
        },
    )
    graphs: None | Graphs = field(
        default=None,
        metadata={
            "name": "Graphs",
            "type": "Element",
        },
    )
    glossary: None | Glossary = field(
        default=None,
        metadata={
            "name": "Glossary",
            "type": "Element",
        },
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    layers: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    local_frame_of_reference: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


class MatMLDoc(_DSModel):
    """Defines the top-level element of a MatML document.

    Attributes:
        material (list[Material]): A list of Material elements.
        metadata (Metadata, optional): An optional Metadata element. Defaults to None.
    """

    material: list[Material] = field(
        metadata={"name": "Material", "type": "Element", "min_occurs": 1},
    )
    metadata: None | Metadata = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
        },
    )
