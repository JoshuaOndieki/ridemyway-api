"""
    App configurations
"""

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Application configuration base class
    """
    SECRET_KEY = 'secret'
    WTF_CSRF_ENABLED = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class TestingConfig(Config):
    """
        Application configuration for testing
    """
    DEBUG = True


class DevelopmentConfig(Config):
    """
        Application configuration for development
    """
    DEBUG = True


class ProductionConfig(Config):
    """
        Application configuration for production
    """
    DEBUG = False


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig}
