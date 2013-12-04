from flask import current_app
from flask.ext.uploads import (UploadSet, configure_uploads, IMAGES,
                               UploadNotAllowed)
from saef_app.core.config import photos
from saef_app.modules.home import bundle as home_bundle
from saef_app.modules.admin import bundle as admin_bundle
from saef_app.core.database import db


def build_app(app):
    app.register_blueprint(home_bundle)
    app.register_blueprint(admin_bundle)
    # Config to Flask from objects
    app.config.from_object('saef_app.core.config.DevelopmentConfig')
    db.init_app(app)
    configure_uploads(app, photos)


def create_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def drop_db(app):
    db.init_app(app)
    with app.app_context():
        db.drop_all()
