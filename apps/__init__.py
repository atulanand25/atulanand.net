# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
Copyright (c) 2024 Atul Anand

"""

from flask import Flask
from importlib import import_module



def register_blueprints(app):
    for module_name in ['home']:
        module = import_module('apps.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    # register_extensions(app)
    register_blueprints(app)
    return app
