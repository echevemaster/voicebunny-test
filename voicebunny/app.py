# -*- coding: utf-8 -*-
import flask

__version__ = '0.1.1'
__author__ = 'Eduardo Echeverria'

# Init application
app = flask.Flask(__name__)
app.config.from_object('voicebunny.config.DevelopmentConfig')

# TODO: Set up the logging

# Import specific blueprints
from voicebunny.ui.backend.views import bp as backend_bp

# Register blueprints
app.register_blueprint(backend_bp)
