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
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'ridemyway')
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'andela21')
    DB_CONN = connect('dbname=' + DATABASE_NAME +
                      ' host=' + DATABASE_HOST +
                      ' user=' + DATABASE_USERNAME +
                      ' password=' + DATABASE_PASSWORD)


class TestingConfig(Config):
    """
        Application configuration for testing
    """
    TEST_DATABASE_NAME = os.getenv('TEST_DATABASE_NAME', 'testdb')
    DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
    DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'tester')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'andela21')
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
