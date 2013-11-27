#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":mod: saef_app.main' -- Program entry point
"""
import sys
sys.path[0:0] = [""]

import flask
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from saef_app.core.database import db
from saef_app.core.build import (build_app as build_application,
                                 create_db, drop_db)

app = flask.Flask(__name__)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


def build_app():
    build_application(app)


@manager.command
def create_database():
    """Creates all database tables"""
    create_db(app)
    print 'All tables created'


@manager.command
def drop_database():
    """Drop all database tables"""
    drop_db(app)
    print 'All tables deleted'


@manager.command
def run():
    """Run application"""
    app.run(debug=True)

if __name__ == '__main__':
    build_app()
    manager.run()
