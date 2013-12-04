#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask.ext.uploads import (UploadSet, IMAGES)
basedir = os.path.abspath(os.path.dirname(__file__))
photos = UploadSet('photos', IMAGES)


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
    UPLOADS_FOLDER = os.path.realpath('.') + '/static/uploads/'
    UPLOADED_PHOTOS_DEST = (os.path.realpath('.') +
                            '/saef_app/static/uploads/photos/')


class TestingConfig(Config):
    TESTING = True
