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

@blueprint.route("/", methods=['GET'])
def get_endpoints():
    data = {
        "/estacoes": "Retorna todas as estacoes disponiveis",
        "/estacao": "Recebe filtros via parametro e retorna a estacao correspondente",
        "/analises": "Retorna todas as analises disponiveis",
        "/analise": "Recebe filtros via parametro e retorna a(s) analise(s) correspondente(s)"
    }

    return json.dumps(data)


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

@blueprint.route("/analise", methods=['GET'])
def get_analise():
    analise_id          = request.args.get("id")
    CO                  = request.args.get("CO")
    CH4                 = request.args.get("CH4")
    NO                  = request.args.get("NO")
    NO2                 = request.args.get("NO2")
    NOx                 = request.args.get("NOx")
    PM_10               = request.args.get("PM_10")
    PM_2_5              = request.args.get("PM_2_5")
    temperatura         = request.args.get("Temperatura")
    chuva               = request.args.get("Chuva")
    pressao             = request.args.get("Pressao")
    radiacaoSolar       = request.args.get("RadiacaoSolar")
    umidadeRelativaDoAr = request.args.get("UmidadeRelativaDoAr")
    direcaoVento        = request.args.get("DirecaoVento")
    velocidadeVento     = request.args.get("VelocidadeVento")
    estacaoCodigo       = request.args.get("EstacaoCodigo")
    
    logger.info(f'Buscando informações de sobre um grupo de análises')

    session = get_session()

    query = session.query(Analise)

    if analise_id is not None:
        query = query.filter(Analise.Analise_id == analise_id)
    if CO is not None:
        query = query.filter(Analise.CO == CO)
    if CH4 is not None:
        query = query.filter(Analise.CH4 == CH4)
    if NO is not None:
        query = query.filter(Analise.NO == NO)
    if NO2 is not None:
        query = query.filter(Analise.NO2 == NO2)
    if NOx is not None:
        query = query.filter(Analise.NOx == NOx)
    if PM_10 is not None:
        query = query.filter(Analise.PM_10 == PM_10)
    if PM_2_5 is not None:
        query = query.filter(Analise.PM_2_5 == PM_2_5)
    if temperatura is not None:
        query = query.filter(Analise.Temperatura == temperatura)
    if chuva is not None:
        query = query.filter(Analise.Chuva == chuva)
    if pressao is not None:
        query = query.filter(Analise.Pressao == pressao)
    if radiacaoSolar is not None:
        query = query.filter(Analise.RadiacaoSolar == radiacaoSolar)
    if umidadeRelativaDoAr is not None:
        query = query.filter(Analise.UmidadeRelativaDoAr == umidadeRelativaDoAr)
    if direcaoVento is not None:
        query = query.filter(Analise.DirecaoVento == direcaoVento)
    if velocidadeVento is not None:
        query = query.filter(Analise.VelocidadeVento == velocidadeVento)
    if estacaoCodigo is not None:
        query = query.filter(Analise.EstacaoCodigo == estacaoCodigo)

    logger.debug(f'Query: {str(query)}')

    data = query.all()
    data = [d.format() for d in data]

    session.close()

    return json.dumps(data)
