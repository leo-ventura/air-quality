# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Date, Numeric, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.model.base import Base

class Analise(Base):
    __tablename__ = 'Analise'
    Analise_id          = Column(Integer, primary_key=True)
    CO                  = Column(Float)
    CH4                 = Column(Float)
    NO                  = Column(Float)
    NO2                 = Column(Float)
    NOx                 = Column(Float)
    PM_10               = Column(Float)
    PM_2_5              = Column(Float)
    Temperatura         = Column(Float)
    Chuva               = Column(Float)
    Pressao             = Column(Float)
    RadiacaoSolar       = Column(Float)
    UmidadeRelativaDoAr = Column(Float)
    DirecaoVento        = Column(Float)
    VelocidadeVento     = Column(Float)
    EstacaoCodigo       = Column(Integer, ForeignKey('Estacao.Codigo'))

    def format():
        return {}