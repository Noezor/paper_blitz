#!flask/bin/python
import sys
print(sys.path)

from articles.article import Article, ArticleSchema
from flask import jsonify, abort, request

from config import app

@app.route('/api/v0.1/article/arxiv_link', methods=['POST'])
def add_article():
    """
    Creates a new article
    """
    print(request)
    print(request.data)
    print(request.json)
    print(request.form)
    link = request.json.get('link','')
    print(link)
    exist_article = Article.query.filter(Article.link == link) \
        .one_or_none()


    if not exist_article :
        schema = ArticleSchema()
        new_article = schema.load(article, session = db.session).data

        db.session.add(new_article)
        db.session.commit()

        return schema.dump(new_article).data, 201

    else :
        abort(409, f"Article {link} already in stack")


if __name__ == '__main__':
    app.run()