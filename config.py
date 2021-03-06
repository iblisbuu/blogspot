import os
class Config:
    SECRET_KEY =os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:123456@localhost/blog'
    DEBUG=True

config_options = {
    'production': ProdConfig,
    'development' : DevConfig
}
