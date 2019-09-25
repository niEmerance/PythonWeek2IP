import os

class Config:
    SOURCE_API_BASE_URL='https://newsapi.org/v2/sources?category={}&apiKey=ca646ffdcd7c47028f4fd29cd28644da'
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}' 
    SOURCE_API_KEY=os.environ.get('SOURCE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}