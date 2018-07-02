"""
    App configurations
"""

import os
from psycopg2 import connect


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Application configuration base class
    """
    SECRET_KEY = 'secret'
    WTF_CSRF_ENABLED = False
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DB_CONN = connect("dbname=ridemyway host=localhost user=postgres password=Andela21")


class TestingConfig(Config):
    """
        Application configuration for testing
    """
    DEBUG = True
    DB_CONN = connect("dbname=ridemyway host=localhost user=postgres password=Andela21")


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
