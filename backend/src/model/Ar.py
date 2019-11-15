# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Date

from base import Base

class Ar(Base):
    __tablename__ = 'Ar'
    arId = Column(Integer, primary_key=true)
    CO  = Column(Number)
    CH4 = Column(Number)
    Nox = Column(Number)
    SO2 = Column(Number)
    PM10 = Column(Number)
    PM25 = Column(Number)

    def __init__(self, CO, CH4, Nox, SO2, PM10, PM25):
        self.CO = CO
        self.CH4 = CH4
        self.Nox = Nox
        self.SO2 = SO2
        self.PM10 = PM10
        self.PM25 = PM25
