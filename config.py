class Config:

    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):

    ENV = 'development'
    DEBUG = True

class TestingConfig(Config):

    ENV = 'testing'
    TESTING = True


class ProductionConfig(Config):

    ENV = 'development'

app_config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig
}