from flask import Blueprint, request, render_template, redirect, url_for


from back.models import Article, ArticleType

web_blueprint = Blueprint('web',__name__)

@web_blueprint.route('/index/',methods=['GET'])
def web_index():
    if request.method == 'GET':
        articles = Article.query.limit(14).all()

        return render_template('web/index.html',articles=articles)


@web_blueprint.route('/article/',methods=['GET'])
def web_article():
    if request.method == 'GET':
        article = Article.query.all()
        return render_template('web/article.html',article=article)


@web_blueprint.route('/about/', methods=['GET'])
def web_about():
    if request.method == 'GET':
        return render_template('web/about.html')


@web_blueprint.route('/newlist/', methods=['GET'])
def newlist():
    if request.method == 'GET':
        articles = Article.query.limit(5).all()
        return render_template('web/newlist.html',articles=articles)