from typing import List
from datetime import datetime

import sys

from paper_blitz.config import db, ma


class Article(db.Model):
    __tablename__ = "article"

    id = db.Column(db.Integer(), primary_key = True)
    title = db.Column(db.String)
    authors = db.Column(db.String)
    link = db.Column(db.String, unique = True)
    timestamp = db.Column(db.DateTime, 
                            default = datetime.utcnow,
                            onupdate = datetime.utcnow)

    def __repr__(self):
        return f"<Article {self.id} : {self.title}>"

class ArticleSchema(ma.ModelSchema):
    class Meta: 
        model = Article
        sqla_session = db.session