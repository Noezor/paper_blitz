from paper_blitz.config import db
from paper_blitz.articles.article import Article
from paper_blitz.stack.model import Participant, Stack, Group



def test_1():
    group = Group(name = "3DV")
    poster = Participant(username = "npion", first_name = "Noe", last_name = "Pion", mail = "noe.pion@gmail.com", group = group)

    db.session.add(poster)
    db.session.commit()

    article = Article(title = "testtitle", authors = "Martin M.", link = "test_link")

    stack_entry = Stack(article = article, poster = poster)

    db.session.add(stack_entry)
    db.session.commit()

test_1()

print(Participant.query.get(1).submitted_articles[0].article)
