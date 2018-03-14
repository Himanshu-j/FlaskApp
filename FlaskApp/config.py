import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'Thisissupposedtobesecret!'
    # Database path can be defined as environment variable and can be
    # accessed from os.environ
    SQLALCHEMY_DATABASE_URI = 'mysql://[user]:[password]@localhost/database'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
