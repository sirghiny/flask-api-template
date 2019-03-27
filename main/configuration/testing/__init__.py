"""Testing configuration."""

from os import getenv


class TestingConfig:
    """Configuration for testing environment."""

    DEBUG = True
    SECRET_KEY = getenv('APP_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('TESTING_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
