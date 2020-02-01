from typing import List
from datetime import datetime

import sys

from paper_blitz.config import db, ma


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer(), primary_key  = True)
    name = db.Column(db.String, unique = True)

    participants = db.relationship("Participant", back_populates="group")
    submitted_articles = db.relationship("Stack")
    
    def __repr__(self):
        return f"<Group {self.name}>"

    def non_presented_articles(self):
        articles = [article for participant in self.participants\
                        for article in participant.submitted_articles if not article.is_presented()]

        return articles

class Participant(db.Model):
    __tablename__ = "participant"

    id = db.Column(db.Integer(), primary_key = True)
    
    username = db.Column(db.String(32), unique = True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    mail = db.Column(db.String(128), unique = True)
    
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))
    group = db.relationship("Group", back_populates="participants")
    submitted_articles = db.relationship("Stack")

    def __repr__(self):
        return f"<Participant {self.username}>"

class Stack(db.Model):
    __tablename__ = "stack"

    id = db.Column(db.Integer(), primary_key = True)

    article_id = db.Column(db.Integer(), db.ForeignKey("article.id"))
    poster_id = db.Column(db.Integer(), db.ForeignKey("participant.id"))
    group_id = db.Column(db.Integer(), db.ForeignKey("group.id"))

    added = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)
    presented = db.Column(db.DateTime)

    article = db.relationship("Article")
    poster = db.relationship("Participant", back_populates = "submitted_articles")
    group = db.relationship("Group", back_populates = "submitted_articles")

    def is_presented(self):
        return bool(self.presented)