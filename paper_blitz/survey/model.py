import sys
print(sys.path)

from paper_blitz.config import db


class Vote(db.Model):
    __tablename__ = "vote"

    id = db.Column(db.Integer(), primary_key = True)
    voter_id = db.Column(db.Integer, db.ForeignKey("participant.id"))
    stack_id = db.Column(db.Integer, db.ForeignKey("stack.id"))

    voter = db.relationship("Participant")
    article = db.relationship("Stack", back_populates = "votes")

    def __repr__(self):
        return f"<Vote {self.id}> : ({self.voter.username}) -> [{self.article.article.title}]"