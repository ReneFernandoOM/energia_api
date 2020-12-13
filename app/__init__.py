import os

from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
ma = Marshmallow()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)

    from app.api import bp as app_api
    app.register_blueprint(app_api, url_prefix='/api')

    return app