#added after changing folder structure
import os

class Config:
    SECRET_KEY = 'SECRET_KEY'

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://segem:2020Segem@localhost/blog_test'


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # or other relevant config var
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    # rest of connection code using the connection string `uri`



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://segem:2020Segem@localhost/personal'

    DEBUG= True



#added after changing folder structure
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}