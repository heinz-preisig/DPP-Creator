"""
Data model for SHACL template knowledge graph

http://knublauch.com/

namespace in rdflib: https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.namespace.html
from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD


"""

from rdflib import Graph
from rdflib import Namespace

from rdflib.namespace import CSVW, DC, DCAT, DCTERMS, DOAP, FOAF, ODRL2, ORG, OWL, \
                           PROF, PROV, RDF, RDFS, SDO, SH, SKOS, SOSA, SSN, TIME, \
                           VOID, XMLNS, XSD



EX = "http://example.org"




ITEM_SEPARATOR = "#"
CLASS_SEPARATOR = "/"