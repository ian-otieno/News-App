from app import app
from flask import render_template
from .requests import businessArticles, entArticles, get_news_source, healthArticles, publishedArticles, randomArticles, scienceArticles, sportArticles, techArticles, topHeadlines

@app.route('/')
def home():
    articles = publishedArticles()

    return  render_template('home.html', articles = articles)

@app.route('/headlines')
def headlines():
    headlines = topHeadlines()

    return  render_template('headlines.html', headlines = headlines)

@app.route('/articles')
def articles():
    random = randomArticles()

    return  render_template('articles.html', random = random)

@app.route('/sources')
def sources():
    newsSource = get_news_source()

    return  render_template('sources.html', newsSource = newsSource)

@app.route('/category/business')
def business():
    sources = businessArticles()

    return  render_template('business.html', sources = sources)
