# config.py
# Third party import
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
