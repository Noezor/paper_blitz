import sys
print(sys.path)

import random

from paper_blitz.config import db
from paper_blitz.articles.article import Article
from paper_blitz.stack.model import Participant, Stack, Group
from paper_blitz.articles.arxiv_parsing import Arxiv_Parser

def test_1():
    group = Group(name = "3DV")
    if Group.query.filter(Group.name == group.name).one_or_none():
       group =  Group.query.filter(Group.name == group.name).one_or_none()

    posters = [Participant(username = "npion", first_name = "Noe", last_name = "Pion", mail = "noe.pion@gmail.com", group = group),\
        Participant(username = "mhumenberger", first_name = "Martin", last_name = "Humenberger", mail = "martin.humenberger@gmail.com", group = group),\
        Participant(username = "asadek", first_name = "Assem", last_name = "Sadek", mail = "assem.sadek@gmail.com", group = group)\
    ]
 
    for poster in posters:
        db.session.add(poster)
    db.session.commit()
    print(Participant.query.filter(Participant.username == 'npion').one_or_none())

    links = ["https://arxiv.org/abs/2001.08972","https://arxiv.org/abs/2001.08248v1","https://arxiv.org/pdf/1511.06422.pdf","https://arxiv.org/abs/1912.00385","https://arxiv.org/abs/2001.07252",\
        "https://arxiv.org/abs/1811.04370","https://arxiv.org/abs/1809.09767","https://arxiv.org/abs/1911.11763","https://arxiv.org/abs/1909.06216"]

    for link in links :
        poster = random.choice(posters)
        if not Participant.query.filter(Participant.username == poster.username).one_or_none():
            db.session.add(poster)
            db.session.commit()
        else :
            poster = Participant.query.filter(Participant.username == poster.username).one_or_none()
            print("User already exists")
        
        article = Article.query.filter(Article.link == link).one_or_none()
        if not article :
            article_parser = Arxiv_Parser()
            article = article_parser.scrape(link)
        else :
            print("Article already exists")

        stack_entry = Stack(article = article, poster = poster, group = poster.group)

        db.session.add(stack_entry)
        db.session.commit()

    print([(group, group.submitted_articles) for group in Group.query.all()])

test_1()