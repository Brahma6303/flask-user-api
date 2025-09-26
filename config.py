# config.py
DB_USERNAME = 'root'
DB_PASSWORD = 'python'
DB_HOST = 'localhost'
DB_NAME = 'flask_users'

SQLALCHEMY_DATABASE_URI = f'mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False