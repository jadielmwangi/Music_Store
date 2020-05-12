import os

class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/group_project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '20-05-1939'

    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):

    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://derrick:montolivo@localhost/group_project'
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}