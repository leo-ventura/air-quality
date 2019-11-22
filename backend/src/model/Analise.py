# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Date, Numeric, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from src.model.base import Base

class Analise(Base):
    __tablename__       = 'Analise'
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

    def format(self):
        return {
            "Analise_id": f'{self.Analise_id}',
            "CO": f'{self.CO}',
            "CH4": f'{self.CH4}',
            "NO": f'{self.NO}',
            "NO2": f'{self.NO2}',
            "NOx": f'{self.NOx}',
            "PM_10": f'{self.PM_10}',
            "PM_2_5": f'{self.PM_2_5}',
            "Temperatura": f'{self.Temperatura}',
            "Chuva": f'{self.Chuva}',
            "Pressao": f'{self.Pressao}',
            "RadiacaoSolar": f'{self.RadiacaoSolar}',
            "UmidadeRelativaDoAr": f'{self.UmidadeRelativaDoAr}',
            "DirecaoVento": f'{self.DirecaoVento}',
            "VelocidadeVento": f'{self.VelocidadeVento}',
            "EstacaoCodigo": f'{self.EstacaoCodigo}'
        }