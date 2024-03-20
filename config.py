class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://USERNAME:PASSWORD@localhost/TarekChaalan-449a1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
