from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import Source


# views
@main.route('/')
def index():
    """
	this view displays the index page showing different news sources
	:return: rendered html template
	"""
    sources = get_sources('business')
    sports = get_sources('sports')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    title = "NEWS LIST"

    return render_template('index.html', title=title, sources=sources, sports=sports,
                           technology=technology, entertainment=entertainment)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles=get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html', title=title, articles=articles)