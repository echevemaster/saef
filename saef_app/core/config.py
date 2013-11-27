#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,
                              'saefdb.db')
    SQLALCHEMY_ECHO = True
    DATABASE_CONNECT_OPTIONS = {}
    CSRF_ENABLED = True
    CSRF_SESSION_KEY = 'your-session-key'
    RESULTS_PER_PAGE = 10


class TestingConfig(Config):
    TESTING = True
