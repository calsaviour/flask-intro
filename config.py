import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '.7\xfe\x88\x14 \x18\x95\xabU\xf4\xe6\xb2bi\xf6\xc6)\xacA\xb9e;8'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
