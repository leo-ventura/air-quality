# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys

from flask import Flask
from src.util import logger
from waitress import serve
from flask_cors import CORS

'''
Blueprints (routes)
'''
from src.controller.endpoints import blueprint as endpointBlueprint

if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app)

    app.config['JSON_AS_ASCII'] = False

    app.logger.addHandler(logger.get_log_handler())

    @app.errorhandler(ConnectionError)
    def handle_connection_error(e):
        app.logger.error(f"Connection error: {e}")
        return "Connection error; try again later..", 502

    @app.errorhandler(Exception)
    def handle_unhandled_exception(e):
        app.logger.exception(e)
        return f'Acesse <a href="http://bd.amendo.im:8081/api/">/api/</a> para mais informações sobre como usar a API', 500

    app.register_blueprint(endpointBlueprint, url_prefix="/api")

    # app.run(port=8081, host="0.0.0.0")
    # using waitress instead of flask's default development server
    serve(app, host='0.0.0.0', port=8081)
