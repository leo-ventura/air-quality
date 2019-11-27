import sys

from src.model.Zona import Zona
from src.model.Analise import Analise
from src.model.Estacao import Estacao
from src.model.EstacaoZona import EstacaoZona
from src.model.QualidadeDoAr import QualidadeDoAr

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)