from paper_blitz.config import ma, db
from .model import Participant, Stack
from paper_blitz.articles.schema import ArticleSchema


class ParticipantSchema(ma.ModelSchema):
    class Meta:
        model = Participant
        sqla_session = db.session


class StackSchema(ma.ModelSchema):
    class Meta: 
        model = Stack
        sqla_session = db.session
    article = ma.Nested(ArticleSchema)