import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                b'0ccd512f8c3493797a23557c32db38e7d51ed74f14fa7580'


class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
