"""Get all configurations."""

from .development import DevelopmentConfig
from .production import ProductionConfig
from .testing import TestingConfig


configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
