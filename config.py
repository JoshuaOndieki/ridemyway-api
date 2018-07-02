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
    DATABASE_NAME = os.environ.get('DATABASE_NAME')
    DATABASE_HOST = os.environ.get('DATABASE_HOST')
    DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
    DB_CONN = connect('dbname=' + DATABASE_NAME +
                      ' host=' + DATABASE_HOST +
                      ' user=' + DATABASE_USERNAME +
                      ' password=' + DATABASE_PASSWORD)


class TestingConfig(Config):
    """
        Application configuration for testing
    """
    TEST_DATABASE_NAME = os.environ.get('TEST_DATABASE_NAME') or 'testdb'
    DATABASE_HOST = os.environ.get('DATABASE_HOST')
    DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
    DEBUG = True
    DB_CONN = connect('dbname=' + TEST_DATABASE_NAME +
                      ' host=' + DATABASE_HOST +
                      ' user=' + DATABASE_USERNAME +
                      ' password=' + DATABASE_PASSWORD)


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
