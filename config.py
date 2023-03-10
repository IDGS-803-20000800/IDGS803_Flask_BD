import os
from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY = "SUPER_SECRET_KEY"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/idgs803" #//nombreUsuario:contraseña@ubicaciónConexión/base_de_datos
    SQLALCHEMY_TRACK_MODIFICATION = False