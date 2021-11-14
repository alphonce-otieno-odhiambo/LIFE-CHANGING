
import os

class Config:
    SECRET_KEY = os.environ.get('SECRETE_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql + psycopg2://alphonce:alphonce@localhost/sql'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
