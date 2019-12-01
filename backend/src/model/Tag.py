# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.model.base import Base

class Tag(Base):
    __tablename__ = 'Tag'
    Tag_id  = Column(Integer, primary_key=True)
    Tag     = Column(String)
    Zona_id = Column(Integer, ForeignKey('Zona.Zona_id'))
    Zona    = relationship('Zona')

    def format(self):
        return {
            "Tag_id": f'{self.Tag_id}',
            "Tag": self.Tag,
            "Zona_id": f'{self.Zona_id}'
        }