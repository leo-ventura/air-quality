# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Date, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.model.base import Base
import json

class QualidadeDoAr(Base):
    __tablename__     = 'QualidadeDoAr'
    ID                = Column(Integer, primary_key=True)
    IQAR              = Column(Integer)
    Data              = Column(Date)
    Poluente          = Column(String)
    Classificacao     = Column(String)
    SiglaLocalEstacao = Column(String, ForeignKey('Estacao.SiglaLocal'))
    Estacao           = relationship("Estacao")

    def format(self):
        return {
            "ID": self.ID,
            "IQAR": self.IQAR,
            "Data": f'{self.Data}',
            "Poluente": self.Poluente,
            "Classificacao": self.Classificacao,
            "SiglaLocalEstacao": self.SiglaLocalEstacao
        }