# -*- coding: utf-8 -*-
import json
import sys

from sqlalchemy.sql import text
from flask import Blueprint
from flask import request

from src.util.logger import get_logger

logger = get_logger(sys.argv[0])

blueprint = Blueprint("endpoints", __name__)

@blueprint.route("/entidades", methods=['GET'])
def get_information():
    logger.info("Buscando informações de entidade")
    data = {
        "tabela": "Nome da Tabela",
        "colunas": {
            "codNum": 2,
            "estacao": "BG"
        }
    }
    return json.dumps(data)
