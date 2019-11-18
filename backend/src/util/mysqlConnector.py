# -*- coding: utf-8 -*-
import sys

from sqlalchemy import create_engine
from src.util.logger import get_logger
from sqlalchemy.orm import sessionmaker

logger = get_logger(sys.argv[0])

logger.info("Criando conexão com o banco de dados")
engine = create_engine('mysql://root:dhdqdarj20192bd@172.10.0.2:3306/AirQuality', echo=True)

logger.info("Inicializando pool de conexões")
Session = sessionmaker(bind=engine)

def get_session():
    logger.info('Criando sessão')

    try:
        return Session()
    except:
        logger.error("Não foi possível criar sessão")