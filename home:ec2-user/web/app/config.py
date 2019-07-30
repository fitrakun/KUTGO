import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '65a6b5e4a3204bdd87adb7b1a98eafaa'