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

@blueprint.route("/estacao", methods=['GET'])
def get_estacao():
    codigoEstacao = request.args.get("codigo")
    siglaLocal    = request.args.get("siglaLocal")
    latitude      = request.args.get("latitude")
    longitude     = request.args.get("longitude")

    logger.info(f'Buscando informações de sobre estacao')
    logger.debug(f'Filtros: {codigoEstacao} {siglaLocal} {latitude} {longitude}')

    session = get_session()

    query = session.query(Estacao)
    if codigoEstacao is not None:
        query = query.filter(Estacao.Codigo == codigoEstacao)
    if siglaLocal is not None:
        query = query.filter(Estacao.SiglaLocal == siglaLocal)
    if latitude is not None:
        query = query.filter(Estacao.Latitude == latitude)
    if longitude is not None:
        query = query.filter(Estacao.Longitude == longitude)

    logger.debug(f'Query: {str(query)}')

    data = query.one()
    data = data.format()

    session.close()

    return json.dumps(data)

@blueprint.route("/analises", methods=['GET'])
def get_analises():
    logger.info("Buscando informações sobre as análises")

    session = get_session()

    data = session.query(Analise).all()
    logger.debug(f'Quantidade de Analises: {len(data)}')
    data = [d.format() for d in data]

    session.close()

    return json.dumps(data)
