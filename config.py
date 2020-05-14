import os

class Config:
    '''
    General configuration parent class
    '''
    API_BASE_URL='http://ws.audioscrobbler.com/2.0/'
  
    
class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
    

config_options = {
'development':DevConfig,
'production':ProdConfig
}