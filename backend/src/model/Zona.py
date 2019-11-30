# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.model.base import Base
from src.model.EstacaoZona import EstacaoZona
import json

class Zona(Base):
    __tablename__ = 'Zona'
    Zona_id   = Column(Integer, primary_key=True)
    Nome      = Column(String)
    Raio      = Column(Float)
    Latitude  = Column(Float)
    Longitude = Column(Float)
    Estacoes  = relationship('Estacao', secondary=EstacaoZona)
    Tags      = relationship('Tag')

    def format(self):
        return {
            "Zona_id": f'{self.Zona_id}',
            "Nome": self.Nome,
            "Raio": f'{self.Raio}',
            "Latitude": f'{self.Latitude}',
            "Longitude": f'{self.Longitude}'
        }