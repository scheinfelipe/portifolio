from uuid import uuid4

class Config(object):
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SCHEDULER_API_ENABLED = True
    THREADED = True

class Prod(Config):
    SECRET_KEY = uuid4().hex


class Dev(Config):
    SECRET_KEY = "Cuicia"
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class Test(Config):
    TESTING = True
