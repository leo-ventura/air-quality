# -*- coding: utf-8 -*-

import argparse
import logging
import os
import sys

from flask import Flask
from src.util import conf
from src.util import log_handler
from flask_cors import CORS

'''
Blueprints (routes)
'''
from src.controller.endpoints import blueprint as endpointBlueprint

if __name__ == "__main__":
    app = Flask(__name__)
    CORS(app)

    app.logger.addHandler(log_handler.get_handler())

    @app.errorhandler(ConnectionError)
    def handle_connection_error(e):
        app.logger.error(f"Connection error: {e}")
        return "Connection error; try again later..", 502

    @app.errorhandler(Exception)
    def handle_unhandled_exception(e):
        app.logger.exception(e)
        return "Ops, something went wrong..", 500

    app.register_blueprint(endpointBlueprint, url_prefix="/api")

    app.run(port=8081, host="0.0.0.0")