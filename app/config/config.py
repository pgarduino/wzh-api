class Config(object):
    """Base Configuration"""
    DEBUG = False
    LOG_LEVEL = 'INFO'
    DB_PATH = 'data'

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    LOG_LEVEL = 'DEBUG'

class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True

class ProductionConfig(Config):
    ENV = 'production'
    LOG_LEVEL = 'INFO'

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': TestingConfig,
}