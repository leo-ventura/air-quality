# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.model.base import Base

EstacaoZona = Table('EstacaoZona', Base.metadata,
    Column('EstacaoCodigo', Integer, ForeignKey('Estacao.Codigo')),
    Column('Zona_id', Integer, ForeignKey('Zona.Zona_id'))
)