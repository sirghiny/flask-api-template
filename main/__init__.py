"""Create application."""

from os import getenv

from flask import Flask
from flask_restful import Api

from app.common.models import db
from .configuration import configurations
from .urls import add_resources


def create_app():
    """Create flask application."""
    app = Flask(__name__)
    configuration = getenv('FLASK_CONFIGURATION')
    app.config.from_object(configurations[configuration])
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    api = Api(app)
    add_resources(api)
    return app

app = create_app()
