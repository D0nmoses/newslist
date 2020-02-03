from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_sources
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
