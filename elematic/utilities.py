import sys
import io
from elematic import api


def report(
    material: api.Material, type: str = "full", out: io.TextIOWrapper = sys.stdout
):
    """Creates a human-readable report of the materials information.

    Args:
        material (MatML_api.Material): _description_
        type (str, optional): _description_. Defaults to "full".
        out (io.TextIOWrapper, optional): _description_. Defaults to sys.stdout.
    """
    metadata = material.parent_object_.Metadata
    indent = ["", "├── ", "│   ├── ", "│   │   ├── "]
    # Material
    out.write(f"Material ID: {material.id}\n")

    # BulkDetails
    if material.BulkDetails is not None:
        bulk_details = material.BulkDetails
        out.write("Bulk Details\n")
        out.write("‾‾‾‾‾‾‾‾‾‾‾‾\n")
        out.write(indent[0] + f"Name: {bulk_details.Name.valueOf_}\n")
        if bulk_details.Class is not None:
            for _class in bulk_details.Class:
                out.write(indent[0] + f"Class: {_class.Name.valueOf_}\n")
        if bulk_details.Subclass is not None:
            for subclass in bulk_details.Subclass:
                out.write(indent[0] + f"Subclass: {subclass.Name.valueOf_}\n")
        if bulk_details.Specification is not None:
            for specification in bulk_details.Specification:
                out.write(indent[0] + f"Specification: {specification.valueOf_}\n")
        if bulk_details.Source is not None:
            source = bulk_details.Source.source
            source_details = metadata.get_SourceDetails(id=source)
            out.write(indent[0] + f"Source: {source_details.Name.valueOf_}\n")
            if source_details.Notes:
                out.write(indent[1] + source_details.Notes + "\n")
        if bulk_details.Form is not None:
            form = bulk_details.Form
            out.write(indent[1] + f"Form: {form.Description}\n")
            if form.Geometry.Shape:
                out.write(indent[1] + f"Shape: {form.Geometry.Shape}\n")
            if form.Geometry.Dimensions:
                out.write(indent[1] + f"Dimensions: {form.Geometry.Dimensions}\n")
            if form.Geometry.Orientation:
                out.write(indent[1] + f"Orientation: {form.Geometry.Orientation}\n")
            if form.Geometry.Notes:
                out.write(indent[1] + f"{form.Geometry.Notes}\n")
        if bulk_details.ProcessingDetails is not None:
            processing_details = bulk_details.ProcessingDetails
            for processing_detail in processing_details:
                out.write(
                    indent[0] + f"Processing: {processing_detail.Name.valueOf_}\n"
                )
                for parameter_value in processing_detail.ParameterValue:
                    parameter = parameter_value.parameter
                    parameter_details = metadata.get_ParameterDetails(id=parameter)
                    out.write(
                        indent[1] + f"Parameter: {parameter_details.Name.valueOf_}\n"
                    )
                    out.write(indent[2] + f"Data: {parameter_value.Data.valueOf_}\n")
                    if parameter_details.Units:
                        out.write(
                            indent[2] + f"Units: {parameter_details.Units.string()}\n"
                        )
                    if parameter_value.Qualifier is not None:
                        for qualifier in parameter_value.Qualifier:
                            out.write(indent[2] + f"Qualifier: {qualifier}")
                    if parameter_value.Uncertainty is not None:
                        # TODO implement this
                        pass
                    if parameter_value.Notes:
                        out.write(indent[2] + f"Notes: {parameter_value.Notes}\n")
                if processing_detail.Result:
                    for result in processing_detail.Result:
                        out.write(indent[1] + f"Result: {result}")
                if processing_detail.Notes:
                    out.write(indent[1] + f"{processing_detail.Notes}\n")
        if bulk_details.Characterization is not None:
            # TODO
            pass
        if bulk_details.PropertyData is not None:
            for property_data in bulk_details.PropertyData:
                property = property_data.property
                property_details = metadata.get_PropertyDetails(id=property)
                out.write(
                    indent[0] + f"Property data: {property_details.Name.valueOf_}\n"
                )
                out.write(indent[1] + f"Data: {property_data.Data.valueOf_}\n")
                if property_details.Units:
                    out.write(indent[1] + f"Units: {property_details.Units.string()}\n")
                else:
                    out.write(indent[1] + f"Units: unitless\n")
                for parameter_value in property_data.ParameterValue:
                    parameter = parameter_value.parameter
                    parameter_details = metadata.get_ParameterDetails(id=parameter)
                    out.write(
                        indent[1] + f"Parameter: {parameter_details.Name.valueOf_}\n"
                    )
                    out.write(indent[2] + f"Data: {parameter_value.Data.valueOf_}\n")
                    if parameter_details.Units:
                        out.write(
                            indent[2] + f"Units: {parameter_details.Units.string()}\n"
                        )
                    if parameter_value.Qualifier is not None:
                        for qualifier in parameter_value.Qualifier:
                            out.write(indent[2] + f"Qualifier: {qualifier}")
                    if parameter_value.Uncertainty is not None:
                        # TODO implement this
                        pass
                    if parameter_value.Notes:
                        out.write(indent[2] + f"Notes: {parameter_value.Notes}\n")
                if property_data.technique is not None:
                    # TODO implement this
                    pass
                if property_data.source is not None:
                    # TODO implement this
                    pass
                if property_data.specimen is not None:
                    # TODO implement this
                    pass
                if property_data.test is not None:
                    # TODO implement this
                    pass
                if property_data.Notes:
                    out.write(indent[1] + f"{processing_detail.Notes}\n")
        out.write("\n")

        # ComponentDetails
        if material.ComponentDetails is not None:
            for component_details in material.ComponentDetails:
                out.write("Component Details\n")
                out.write("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾\n")
                out.write(indent[0] + f"Name: {component_details.Name.valueOf_}\n")
                if component_details.Class is not None:
                    for _class in component_details.Class:
                        out.write(indent[0] + f"Class: {_class.Name.valueOf_}\n")
                if component_details.Subclass is not None:
                    for subclass in component_details.Subclass:
                        out.write(indent[0] + f"Subclass: {subclass.Name.valueOf_}\n")
                if component_details.Specification is not None:
                    for specification in component_details.Specification:
                        out.write(
                            indent[0] + f"Specification: {specification.valueOf_}\n"
                        )
                if component_details.Source is not None:
                    source = component_details.Source.source
                    source_details = metadata.get_SourceDetails(id=source)
                    out.write(indent[0] + f"Source: {source_details.Name.valueOf_}\n")
                    if source_details.Notes:
                        out.write(indent[1] + source_details.Notes + "\n")
                if component_details.Form is not None:
                    form = component_details.Form
                    out.write(indent[1] + f"Form: {form.Description}\n")
                    if form.Geometry.Shape:
                        out.write(indent[1] + f"Shape: {form.Geometry.Shape}\n")
                    if form.Geometry.Dimensions:
                        out.write(
                            indent[1] + f"Dimensions: {form.Geometry.Dimensions}\n"
                        )
                    if form.Geometry.Orientation:
                        out.write(
                            indent[1] + f"Orientation: {form.Geometry.Orientation}\n"
                        )
                    if form.Geometry.Notes:
                        out.write(indent[1] + f"{form.Geometry.Notes}\n")
                if component_details.ProcessingDetails is not None:
                    processing_details = component_details.ProcessingDetails
                    for processing_detail in processing_details:
                        out.write(
                            indent[0]
                            + f"Processing: {processing_detail.Name.valueOf_}\n"
                        )
                        for parameter_value in processing_detail.ParameterValue:
                            parameter = parameter_value.parameter
                            parameter_details = metadata.get_ParameterDetails(
                                id=parameter
                            )
                            out.write(
                                indent[1]
                                + f"Parameter: {parameter_details.Name.valueOf_}\n"
                            )
                            out.write(
                                indent[2] + f"Data: {parameter_value.Data.valueOf_}\n"
                            )
                            if parameter_details.Units:
                                out.write(
                                    indent[2]
                                    + f"Units: {parameter_details.Units.string()}\n"
                                )
                            if parameter_value.Qualifier is not None:
                                for qualifier in parameter_value.Qualifier:
                                    out.write(indent[2] + f"Qualifier: {qualifier}")
                            if parameter_value.Uncertainty is not None:
                                # TODO implement this
                                pass
                            if parameter_value.Notes:
                                out.write(
                                    indent[2] + f"Notes: {parameter_value.Notes}\n"
                                )
                        if processing_detail.Result:
                            for result in processing_detail.Result:
                                out.write(indent[1] + f"Result: {result}")
                        if processing_detail.Notes:
                            out.write(indent[1] + f"{processing_detail.Notes}\n")
                if component_details.Characterization is not None:
                    # TODO
                    pass
                if component_details.PropertyData is not None:
                    for property_data in component_details.PropertyData:
                        property = property_data.property
                        property_details = metadata.get_PropertyDetails(id=property)
                        out.write(
                            indent[0]
                            + f"Property data: {property_details.Name.valueOf_}\n"
                        )
                        out.write(indent[1] + f"Data: {property_data.Data.valueOf_}\n")
                        if property_details.Units:
                            out.write(
                                indent[1]
                                + f"Units: {property_details.Units.string()}\n"
                            )
                        else:
                            out.write(indent[1] + f"Units: unitless\n")
                        for parameter_value in property_data.ParameterValue:
                            parameter = parameter_value.parameter
                            parameter_details = metadata.get_ParameterDetails(
                                id=parameter
                            )
                            out.write(
                                indent[1]
                                + f"Parameter: {parameter_details.Name.valueOf_}\n"
                            )
                            out.write(
                                indent[2] + f"Data: {parameter_value.Data.valueOf_}\n"
                            )
                            if parameter_details.Units:
                                out.write(
                                    indent[2]
                                    + f"Units: {parameter_details.Units.string()}\n"
                                )
                            if parameter_value.Qualifier is not None:
                                for qualifier in parameter_value.Qualifier:
                                    out.write(indent[2] + f"Qualifier: {qualifier}")
                            if parameter_value.Uncertainty is not None:
                                # TODO implement this
                                pass
                            if parameter_value.Notes:
                                out.write(
                                    indent[2] + f"Notes: {parameter_value.Notes}\n"
                                )
                        if property_data.technique is not None:
                            # TODO implement this
                            pass
                        if property_data.source is not None:
                            # TODO implement this
                            pass
                        if property_data.specimen is not None:
                            # TODO implement this
                            pass
                        if property_data.test is not None:
                            # TODO implement this
                            pass
                        if property_data.Notes:
                            out.write(indent[1] + f"{processing_detail.Notes}\n")
                out.write("\n")

    # Graphs
    # not yet implemented

    # Glossary
    if material.Glossary is not None:
        out.write("Glossary\n")
        out.write("‾‾‾‾‾‾‾‾\n")
        for glossary_term in material.Glossary.Term:
            out.write(f"Term: {glossary_term.Name.valueOf_}\n")
            out.write(f"Definition: {glossary_term.Definition}\n\n")
