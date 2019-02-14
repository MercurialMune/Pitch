import os


class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY = 'averysecretkey'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:mercurial92@localhost/pitchusers'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'munenecyp@gmail.com'
    MAIL_PASSWORD = 'munene12345678'

    pass


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


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