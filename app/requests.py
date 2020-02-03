import urllib.request, json
from .models import Source, NewsArticle
from datetime import datetime

api_key = None
sources_url = None
articles_url = None


def configure_request(app):
    global api_key, base_url, articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = _url = app.config['NEWS_SOURCES_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']


def get_sources(category):
    """
    Function that receives json response and returns the results
    :param category:
    :return: sources_results
    """
    url = sources_url.format(category, api_key)

    with urllib.request.urlopen(url) as url:
        data = url.read()
        response = json.loads(data)
        results = None

        if response['sources']:
            sources_results_list = response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    """
    Function that processes json response into a list of the sources
    :param sources_list:
    :return: a list of the news sources
    """
    sources_results = []

    for item in sources_list:
        id = item.get('id')
        name = item.get('name')
        description = item.get('description')
        url = item.get('url')
        category = item.get('category')
        language = item.get('language')
        country = item.get('country')

        source = Source(id, name, description, url, category, country, language)
        sources_results.append(source)

    return sources_results
