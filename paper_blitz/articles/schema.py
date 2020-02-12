from paper_blitz.config import ma, db
from .article import Article


class Article_Schema(ma.ModelSchema):
    class Meta: 
        model = Article
        sqla_session = db.session
        fields = ("title","authors","link","timestamp")