from paper_blitz.config import ma, db
from .model import Participant, Stack
from paper_blitz.articles.schema import Article_Schema


class Participant_Schema(ma.ModelSchema):
    class Meta:
        model = Participant
        sqla_session = db.session


class Stack_Schema(ma.ModelSchema):
    class Meta: 
        model = Stack
        sqla_session = db.session
    article = ma.Nested(Article_Schema)

class Article_Stack_Schema(ma.ModelSchema):
    article = ma.Nested(Article_Schema)