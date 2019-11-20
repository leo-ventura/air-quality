# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.model.base import Base
import json

class Zona(Base):
    __tablename__ = 'Zona'
    Zona_id   = Column(Integer)
    Nome      = Column(String)
    Raio      = Column(Float)
    Latitude  = Column(Float)
    Longitude = Column(Float)


    def format(self):
        return {
            "Zona_id": f'{self.Zona_id}',
            "Nome": self.Nome,
            "Raio": f'{self.Raio}',
            "Latitude": f'{self.Latitude}'
            "Longitude": f'{self.Longitude}'
        }