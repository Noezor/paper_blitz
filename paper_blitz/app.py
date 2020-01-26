#!flask/bin/python
import sys
sys.path.append("/home/pionn/paper_blitz")

from paper_blitz.articles.article import Article, ArticleSchema
from paper_blitz.articles.arxiv_parsing import Arxiv_Parser
from flask import jsonify, abort, request

from paper_blitz.config import app, db


@app.route('/api/v0.1/article/arxiv_link', methods=['POST'])
def add_article():
    """
    Creates a new article
    """
    link = request.json.get('link','')
    exist_article = Article.query.filter(Article.link == link).one_or_none()

    article_parser = Arxiv_Parser()
    if not exist_article :
        schema = ArticleSchema()
        article = article_parser.scrape(link)
        db.session.add(article)
        db.session.commit()

        return schema.dump(article), 201

    else :
        abort(409, f"Article {link} already in stack")


if __name__ == '__main__':
    app.run(debug=False)