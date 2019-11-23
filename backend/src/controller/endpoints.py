# -*- coding: utf-8 -*-
import json
import sys

from sqlalchemy.sql import text
from flask import Blueprint
from flask import request
from flask import jsonify

from src.util.logger import get_logger
from src.util.mysqlConnector import get_session

from src.model.Estacao import Estacao
from src.model.Analise import Analise
from src.model.QualidadeDoAr import QualidadeDoAr
from src.model.Zona import Zona

logger = get_logger(sys.argv[0])

blueprint = Blueprint("endpoints", __name__)

LIMIT = 200

@blueprint.route("/", methods=['GET'])
def get_endpoints():
    data = {
        "endpoints": [
            {
                "url": "/estacoes",
                "desc": "Retorna todas as estações disponíveis"
            },
            {
                "url": "/estacao",
                "desc": "Recebe filtros via parâmetro e retorna a estação correspondente"
            },
            {
                "url": "/analises",
                "desc": "Retorna todas as análises disponíveis"
            },
            {
                "url": "/analise",
                "desc": "Recebe filtros via parâmetro e retorna a(s) análise(s) correspondente(s)"
            },
            {
                "url": "/todasQualidadeDoAr",
                "desc": "Retorna todas as informações sobre qualidade do ar relativas a poluentes"
            },
            {
                "url": "/qualidadeDoAr",
                "desc": "Recebe filtros e retorna informações sobre a qualidade do ar relativa ao filtro aplicado"
            },
            {
                "url": "/zonas",
                "desc": "Retorna todas as zonas disponíveis"
            },
            {
                "url": "/zona",
                "desc": "Recebe filtros e retornas as zonas que encaixam no filtro aplicado"
            }
        ],
        "OBS": "Para todos endpoints que recebem filtro, o mesmo segue o padrão do nome da coluna no banco de dados. Exemplo: /analise?CO=0.6. Para colunas que o nome seja uma palavra, comece com letra minúscula. Exemplo: /qualidadeDoAr?siglaLocalEstacao=AV"
    }

    return jsonify(data)


@blueprint.route("/estacoes", methods=['GET'])
def get_estacoes():
    logger.info("Buscando informações de sobre as estações")

    session = get_session()

    data = session.query(Estacao).all()
    data = [d.format() for d in data]

    session.close()

    return jsonify(data)

@blueprint.route("/estacao", methods=['GET'])
def get_estacao():
    logger.info(f'Buscando informações de sobre estacao')

    codigoEstacao = request.args.get("codigo")
    siglaLocal    = request.args.get("siglaLocal")
    latitude      = request.args.get("latitude")
    longitude     = request.args.get("longitude")

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

    return jsonify(data)

@blueprint.route("/analises", methods=['GET'])
def get_analises():
    logger.info("Buscando informações sobre as análises")

    session = get_session()

    data = session.query(Analise).limit(LIMIT).all()
    logger.debug(f'Quantidade de Analises: {len(data)}')
    data = [d.format() for d in data]

    session.close()

    return jsonify(data)

@blueprint.route("/analise", methods=['GET'])
def get_analise():
    logger.info(f'Buscando informações de sobre um grupo de análises')

    analise_id          = request.args.get("id")
    CO                  = request.args.get("CO")
    CH4                 = request.args.get("CH4")
    NO                  = request.args.get("NO")
    NO2                 = request.args.get("NO2")
    NOx                 = request.args.get("NOx")
    PM_10               = request.args.get("PM_10")
    PM_2_5              = request.args.get("PM_2_5")
    temperatura         = request.args.get("temperatura")
    chuva               = request.args.get("chuva")
    pressao             = request.args.get("pressao")
    radiacaoSolar       = request.args.get("radiacaoSolar")
    umidadeRelativaDoAr = request.args.get("umidadeRelativaDoAr")
    direcaoVento        = request.args.get("direcaoVento")
    velocidadeVento     = request.args.get("velocidadeVento")
    estacaoCodigo       = request.args.get("estacaoCodigo")

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

    logger.debug(f'Query: {query}')

    data = query.limit(LIMIT).all()
    data = [d.format() for d in data]

    logger.debug(f'Quantidade de análises: {len(data)}')

    session.close()

    return jsonify(data)

@blueprint.route("/todasQualidadeDoAr", methods=['GET'])
def get_todas_qualidade_do_ar():
    logger.info("Buscando informações sobre qualidade do ar")

    session = get_session()

    data = session.query(QualidadeDoAr).all()
    data = [d.format() for d in data]

    session.close()

    return jsonify(data)

@blueprint.route("/qualidadeDoAr", methods=['GET'])
def get_qualidade_do_ar():
    logger.info("Buscando informações sobre qualidade do ar filtradas por colunas")

    ID = request.args.get("id")
    IQAR = request.args.get("iqar")
    Data = request.args.get("data")
    Poluente = request.args.get("poluente")
    Classificacao = request.args.get("classificacao")
    SiglaLocalEstacao = request.args.get("siglaLocalEstacao")

    session = get_session()

    query = session.query(QualidadeDoAr)

    if ID is not None:
        query = query.filter(QualidadeDoAr.ID == ID)
    if IQAR is not None:
        query = query.filter(QualidadeDoAr.IQAR == IQAR)
    if Data is not None:
        query = query.filter(QualidadeDoAr.Data == Data)
    if Poluente is not None:
        query = query.filter(QualidadeDoAr.Poluente == Poluente)
    if Classificacao is not None:
        query = query.filter(QualidadeDoAr.Classificacao == Classificacao)
    if SiglaLocalEstacao is not None:
        query = query.filter(QualidadeDoAr.SiglaLocalEstacao == SiglaLocalEstacao)

    data = query.all()
    data = [d.format() for d in data]

    session.close()

    return jsonify(data)

@blueprint.route("/zonas", methods=['GET'])
def get_zonas():
    logger.info("Buscando informações sobre as zonas")

    session = get_session()

    data = session.query(Zona).all()
    data = [d.format() for d in data]

    session.close()

    return jsonify(data)

@blueprint.route("/zona", methods=['GET'])
def get_zona():
    logger.info(f'Buscando informações de sobre zona')

    Zona_id = request.args.get("zona_id")
    Nome = request.args.get("nome")
    Raio = request.args.get("raio")
    Latitude = request.args.get("latitude")
    Longitude = request.args.get("longitude")

    logger.debug(f'Filtros: {Zona_id} {Nome} {Raio} {Latitude} {Longitude}')

    session = get_session()

    query = session.query(Zona)

    if Zona_id is not None:
        query = query.filter(Zona.Zona_id == Zona_id)
    if Nome is not None:
        query = query.filter(Zona.Nome == Nome)
    if Raio is not None:
        query = query.filter(Zona.Raio == Raio)
    if Latitude is not None:
        query = query.filter(Zona.Latitude == Latitude)
    if Longitude is not None:
        query = query.filter(Zona.Longitude == Longitude)

    logger.debug(f'Query: {str(query)}')

    data = query.all()
    data = [d.format() for d in data]

    session.close()

    return jsonify(data)