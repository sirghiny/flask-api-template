"""Development configuration."""

from os import getenv


class DevelopmentConfig:
    """Configuration for development environment."""

    DEBUG = True
    SECRET_KEY = getenv('APP_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
