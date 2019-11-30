# -*- coding: utf-8 -*-
import json
import sys

from sqlalchemy.sql import text
from sqlalchemy.sql import func
from flask import Blueprint
from flask import request
from flask import jsonify

from src.util.logger import get_logger
from src.util.mysqlConnector import get_session
from src.util.stringUtility import str_to_class

from src.model.Tag import Tag
from src.model.Zona import Zona
from src.model.Estacao import Estacao
from src.model.Analise import Analise
from src.model.QualidadeDoAr import QualidadeDoAr

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
                "desc": "Recebe filtros e retorna as zonas que encaixam nos filtros aplicados"
            },
            {
                "url": "/tags",
                "desc": "Retorna todas as tags disponíveis"
            },
            {
                "url": "/tag",
                "desc": "Recebe filtros e retorna as tags que encaixam nos filtros"
            },
            {
                "url": "/avg",
                "desc": "Recebe o nome da tabela e o campo a retorna a média. Exemplo: /avg?tabela=Analise&coluna=CO"
            },
            {
                "url": "/max",
                "desc": "Recebe o nome da tabela e o campo a retorna o valor máximo. Exemplo: /max?tabela=Analise&coluna=CO"
            },
            {
                "url": "/min",
                "desc": "Recebe o nome da tabela e o campo a retorna o valor mínimo. Exemplo: /min?tabela=Analise&coluna=CO"
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

    # Test equality
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
    # Test `value` > parameter
    minAnalise_id          = request.args.get("minId")
    minCO                  = request.args.get("minCO")
    minCH4                 = request.args.get("minCH4")
    minNO                  = request.args.get("minNO")
    minNO2                 = request.args.get("minNO2")
    minNOx                 = request.args.get("minNOx")
    minPM_10               = request.args.get("minPM_10")
    minPM_2_5              = request.args.get("minPM_2_5")
    minTemperatura         = request.args.get("minTemperatura")
    minChuva               = request.args.get("minChuva")
    minPressao             = request.args.get("minPressao")
    minRadiacaoSolar       = request.args.get("minRadiacaoSolar")
    minUmidadeRelativaDoAr = request.args.get("minUmidadeRelativaDoAr")
    minDirecaoVento        = request.args.get("minDirecaoVento")
    minVelocidadeVento     = request.args.get("minVelocidadeVento")
    minData                = request.args.get("minData")
    minEstacaoCodigo       = request.args.get("minEstacaoCodigo")
    # Test `value` < parameter
    maxAnalise_id          = request.args.get("maxId")
    maxCO                  = request.args.get("maxCO")
    maxCH4                 = request.args.get("maxCH4")
    maxNO                  = request.args.get("maxNO")
    maxNO2                 = request.args.get("maxNO2")
    maxNOx                 = request.args.get("maxNOx")
    maxPM_10               = request.args.get("maxPM_10")
    maxPM_2_5              = request.args.get("maxPM_2_5")
    maxTemperatura         = request.args.get("maxTemperatura")
    maxChuva               = request.args.get("maxChuva")
    maxPressao             = request.args.get("maxPressao")
    maxRadiacaoSolar       = request.args.get("maxRadiacaoSolar")
    maxUmidadeRelativaDoAr = request.args.get("maxUmidadeRelativaDoAr")
    maxDirecaoVento        = request.args.get("maxDirecaoVento")
    maxVelocidadeVento     = request.args.get("maxVelocidadeVento")
    maxData                = request.args.get("maxData")
    maxEstacaoCodigo       = request.args.get("maxEstacaoCodigo")

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

    if minAnalise_id is not None:
        query = query.filter(Analise.Analise_id > minAnalise_id)
    if minCO is not None:
        query = query.filter(Analise.CO > minCO)
    if minCH4 is not None:
        query = query.filter(Analise.CH4 > minCH4)
    if minNO is not None:
        query = query.filter(Analise.NO > minNO)
    if minNO2 is not None:
        query = query.filter(Analise.NO2 > minNO2)
    if minNOx is not None:
        query = query.filter(Analise.NOx > minNOx)
    if minPM_10 is not None:
        query = query.filter(Analise.PM_10 > minPM_10)
    if minPM_2_5 is not None:
        query = query.filter(Analise.PM_2_5 > minPM_2_5)
    if minTemperatura is not None:
        query = query.filter(Analise.Temperatura > minTemperatura)
    if minChuva is not None:
        query = query.filter(Analise.Chuva > minChuva)
    if minPressao is not None:
        query = query.filter(Analise.Pressao > minPressao)
    if minRadiacaoSolar is not None:
        query = query.filter(Analise.RadiacaoSolar > minRadiacaoSolar)
    if minUmidadeRelativaDoAr is not None:
        query = query.filter(Analise.UmidadeRelativaDoAr > minUmidadeRelativaDoAr)
    if minDirecaoVento is not None:
        query = query.filter(Analise.DirecaoVento > minDirecaoVento)
    if minVelocidadeVento is not None:
        query = query.filter(Analise.VelocidadeVento > minVelocidadeVento)
    if minData is not None:
        query = query.filter(Analise.Data_e_hora > minData)
    if minEstacaoCodigo is not None:
        query = query.filter(Analise.EstacaoCodigo > minEstacaoCodigo)

    if maxAnalise_id is not None:
        query = query.filter(Analise.Analise_id < maxAnalise_id)
    if maxCO is not None:
        query = query.filter(Analise.CO < maxCO)
    if maxCH4 is not None:
        query = query.filter(Analise.CH4 < maxCH4)
    if maxNO is not None:
        query = query.filter(Analise.NO < maxNO)
    if maxNO2 is not None:
        query = query.filter(Analise.NO2 < maxNO2)
    if maxNOx is not None:
        query = query.filter(Analise.NOx < maxNOx)
    if maxPM_10 is not None:
        query = query.filter(Analise.PM_10 < maxPM_10)
    if maxPM_2_5 is not None:
        query = query.filter(Analise.PM_2_5 < maxPM_2_5)
    if maxTemperatura is not None:
        query = query.filter(Analise.Temperatura < maxTemperatura)
    if maxChuva is not None:
        query = query.filter(Analise.Chuva < maxChuva)
    if maxPressao is not None:
        query = query.filter(Analise.Pressao < maxPressao)
    if maxRadiacaoSolar is not None:
        query = query.filter(Analise.RadiacaoSolar < maxRadiacaoSolar)
    if maxUmidadeRelativaDoAr is not None:
        query = query.filter(Analise.UmidadeRelativaDoAr < maxUmidadeRelativaDoAr)
    if maxDirecaoVento is not None:
        query = query.filter(Analise.DirecaoVento < maxDirecaoVento)
    if maxVelocidadeVento is not None:
        query = query.filter(Analise.VelocidadeVento < maxVelocidadeVento)
    if maxData is not None:
        query = query.filter(Analise.Data_e_hora < maxData)
    if maxEstacaoCodigo is not None:
        query = query.filter(Analise.EstacaoCodigo < maxEstacaoCodigo)

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
    logger.info(f'Buscando informações sobre zona')

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

@blueprint.route("/tags", methods=['GET'])
def get_tags():
    logger.info("Buscando informação sobre as tags")

    session = get_session()

    data = session.query(Tag).all()
    data = [d.format() for d in data]

    logger.debug(data)

    return jsonify(data)

@blueprint.route("/tag", methods=['GET'])
def get_tag():
    logger.info(f'Buscando informações sobre tag')

    Tag_id    = request.args.get("tag_id")
    Descricao = request.args.get("tag")
    Zona_id   = request.args.get("zona_id")

    logger.debug(f'Filtros: {Tag_id} {Tag} {Zona_id}')

    session = get_session()

    query = session.query(Tag)

    if Tag_id is not None:
        query = query.filter(Tag.Tag_id == Tag_id)
    if Descricao is not None:
        query = query.filter(Tag.Tag == Descricao)
    if Zona_id is not None:
        query = query.filter(Tag.Zona_id == Zona_id)

    logger.debug(f'Query: {str(query)}')

    data = query.all()
    data = [d.format() for d in data]

    session.close()

    return jsonify(data)

@blueprint.route("/avg", methods=['GET'])
def get_avg():
    logger.info("Buscando informação de média")

    table = request.args.get("tabela")
    column = request.args.get("coluna")

    logger.debug(f"Tabela:\t{table}, coluna:\t{column}")

    table = str_to_class(table)
    column = getattr(table, column)

    session = get_session()

    data = session.query(func.avg(column)).one()

    logger.debug(data)

    data = float(data[0])

    data = {
        "avg": data,
    }

    return jsonify(data)

@blueprint.route("/max", methods=['GET'])
def get_max():
    logger.info("Buscando informação de máximo valor")

    table = request.args.get("tabela")
    column = request.args.get("coluna")

    logger.debug(f"Tabela:\t{table}, coluna:\t{column}")

    table = str_to_class(table)
    column = getattr(table, column)

    session = get_session()

    data = session.query(func.max(column)).one()

    logger.debug(data)

    data = float(data[0])

    data = {
        "max": data,
    }

    return jsonify(data)


@blueprint.route("/min", methods=['GET'])
def get_min():
    logger.info("Buscando informação de mínimo valor")

    table = request.args.get("tabela")
    column = request.args.get("coluna")

    logger.debug(f"Tabela:\t{table}, coluna:\t{column}")

    table = str_to_class(table)
    column = getattr(table, column)

    session = get_session()

    data = session.query(func.min(column)).one()

    logger.debug(data)

    data = float(data[0])

    data = {
        "min": data,
    }

    return jsonify(data)