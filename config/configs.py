class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:qwerty17@127.0.0.1:5432/EMS"
    SECRET_KEY = "some_random_key"


class ProductionConfig(Config):
    DEBUG = False

