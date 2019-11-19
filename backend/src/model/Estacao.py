# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.model.base import Base
import json

class Estacao(Base):
    __tablename__ = 'Estacao'
    Codigo        = Column(Integer, primary_key=True)
    SiglaLocal    = Column(String)
    NomeEstacao   = Column(String)
    Latitude      = Column(Numeric)
    Longitude     = Column(Numeric)
    Analises      = relationship('Analise')
    QualidadeDoAr = relationship('QualidadeDoAr')

    def format(self):
        return {
            "Codigo": self.Codigo,
            "SiglaLocal": self.SiglaLocal,
            "NomeEstacao": self.NomeEstacao,
            "Latitude": self.Latitude,
            "Longitude": self.Longitude
        }