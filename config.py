import os
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data/notes.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False