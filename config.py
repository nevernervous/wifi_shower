import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'da2b5019c6a2f8981c6848f257ebc0cb75c822a94d')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', "sqlite:///" + os.path.join(BASE_DIR, 'app.db'))


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

