# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.model.base import Base
from src.model.EstacaoZona import EstacaoZona

class Estacao(Base):
    """
        Mapeamento da tabela de Estacao
        Analise e QualidadeDoAr possui um relacionamento One to Many
        Enquanto Zonas é Many to Many relacionado pela tabela de ligação EstacaoZona
    """
    __tablename__ = 'Estacao'
    Codigo        = Column(Integer, primary_key=True)
    SiglaLocal    = Column(String)
    NomeEstacao   = Column(String)
    Latitude      = Column(Numeric)
    Longitude     = Column(Numeric)
    Analises      = relationship('Analise')
    QualidadeDoAr = relationship('QualidadeDoAr')
    Zonas         = relationship('Zona', secondary=EstacaoZona)

    def format(self):
        return {
            "Codigo": f'{self.Codigo}',
            "SiglaLocal": self.SiglaLocal,
            "NomeEstacao": self.NomeEstacao,
            "Latitude": f'{self.Latitude}',
            "Longitude": f'{self.Longitude}'
        }