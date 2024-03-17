from . import MatML_api
import sys



class Lexicon():
    def __init__(self):
        self.lexicon = {
            "NX" : {

            },
            "GRANTA" : {

            },
            "ANSYSWB" : {

            },
            "ANSYSAPDL" : {

            },
            "ABAQUS" : {

            },
            "CATIA" : {

            },
            "NASTRAN" : {

            },
            "CREO" : {

            },
            "SOLIDWORKS" : {

            }
        }
        self.formats = self._update_formats(self)
    
    def _update_formats(self):
        self.formats = list(self.lexicon.keys())

    def add_lexicon(self,new_lexicon):
        pass

    def del_lexicon(self,del_lexicon):
        pass

def translate(doc: MatML_api.MatML_Doc,from_format: str,to_format: str, lexicon:Lexicon=None) -> MatML_api.MatML_Doc:
    """Translates

    Args:
        doc (MatML_api.MatML_Doc): _description_
        from_format (str): _description_
        to_format (str): _description_
        lexicon (Lexicon, optional): _description_. Defaults to Lexicon().

    Returns:
        MatML_api.MatML_Doc: _description_
    """
    pass


def report(material=None, out=sys.stdout):
    """Creates a human-readable report of the materials information.

    Args:
        material (_type_, optional): _description_. Defaults to None.
        out (_type_, optional): _description_. Defaults to sys.stdout.
    """
    pass