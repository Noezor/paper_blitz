from typing import List
from datetime import datetime

from config import db, ma


class Article(db.Model):
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    authors = db.Column(db.String)
    link = db.Column(db.String)
    timestamp = db.Column(db.DateTime, 
                            default = datetime.utcnow,
                            onupdate = datetime.utcnow)
    
    def from_link(link):
        # TODO
        return Article("test_article", None, 2020, None)

class ArticleSchema(ma.ModelSchema):
    class Meta: 
        model = Article
        sqla_session = db.session