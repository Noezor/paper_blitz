#!flask/bin/python
import sys
sys.path.append("/home/pionn/paper_blitz")

from paper_blitz.articles.article import Article, ArticleSchema
from paper_blitz.articles.arxiv_parsing import Arxiv_Parser
from flask import jsonify, abort, request

from paper_blitz.config import app, db


@app.route('/api/v0.1/stack/submit', methods=['POST'])
def add_article():
    """
    Creates a new article
    """
    link = request.json.get('link','')
    username = request.json.get('username','')
    user = Participant.query.find(Participant.username == username).first_or_404()

    exist_article = Article.query.filter(Article.link == link).one_or_none()
    if not exist_article :
        article_parser = Arxiv_Parser()
        article = article_parser.scrape(link)
    else :
        article = Article.query.filter(Article.link == link)[0]

    group = user.group

    if article in group.submitted_articles:
        return f"Article already submitted to {group.name}",201

    stack_entry = Stack(article = article, poster = user, group=user.group)

    return schema.dump(article), 201

if __name__ == '__main__':
    app.run(debug=False)