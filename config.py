import os

class Config:
    #https: // api.themoviedb.org / 3 / movie / {}?api_key = {}

    NEWS_API_BASE_URL ='https://newsapi.org/v2/{}?api_key={}'
    NEWs_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}