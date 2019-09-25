from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources, get_articles

# Views
@main.route('/')
def index():
    sources=get_sources('general')
    title='Welcome to our articles'
    return render_template('index.html', title=title, general=sources)

@main.route('/articles/<id>')
def source(id):
    articles_source=get_articles(id)
    title='Welcome to our articles'
    return render_template('articles.html', title=title, articles=articles_source)