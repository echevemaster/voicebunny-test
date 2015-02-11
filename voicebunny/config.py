# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    DATABASE_CONNECT_OPTIONS = {}
    SECRET_KEY = 'key'
    CSRF_SESSION_KEY = "somethingimpossibletoguess"


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'This string will be replaced with a proper key in production'
    CSRF_SESSION_KEY = "somethingimpossibletoguess"
    BUNNY_KEY = '43775'
    BUNNY_TOKEN = 'b3d4ef64d49f7bc153de1b7da2ff74a0'


class TestingConfig(Config):
    TESTING = True
