import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://default-007:expandebles7@localhost/jamz'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    UPLOADED_MUSIC_DEST = 'app/static/music'
    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI =os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://default-007:expandebles7@localhost/jamz'

config_options = {
'development':DevConfig,
'production':ProdConfig
}