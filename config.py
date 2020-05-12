import os

class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/group_project'

class ProdConfig(Config):

    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/group_project'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}