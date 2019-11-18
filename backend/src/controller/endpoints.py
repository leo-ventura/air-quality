# -*- coding: utf-8 -*-
import json
import sys

from sqlalchemy.sql import text
from flask import Blueprint
from flask import request

from src.util.logger import get_logger
from src.util.mysqlConnector import get_session

from src.model.Estacao import Estacao
from src.model.Analise import Analise

logger = get_logger(sys.argv[0])

blueprint = Blueprint("endpoints", __name__)

@blueprint.route("/estacoes", methods=['GET'])
def get_estacoes():
    logger.info("Buscando informações de sobre as estações")

    session = get_session()

    data = session.query(Estacao).all()
    data = [d.format() for d in data]

    session.close()

    return json.dumps(data)
