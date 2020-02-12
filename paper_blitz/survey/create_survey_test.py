from paper_blitz.stack.model import Participant, Stack, Group
from paper_blitz.stack.schema import StackSchema
from paper_blitz.articles.article import Article
from paper_blitz.survey.model import Vote
from paper_blitz.config import db
from paper_blitz.survey.create_survey import Article_Selector_Survey


group = Group.query.all()[0]

print(group)
article_selector = Article_Selector_Survey()
print(article_selector.select_articles(group))

particpant = Participant.query.all()[0]
print(particpant)

stack_entry = Stack.query.all()[0]

for participant in Participant.query.all()[:2]:
    vote = Vote(article = stack_entry, voter = participant)
    db.session.add(vote)
db.session.commit()


print(Stack.query.all())
print(Vote.query.all())

schema = StackSchema(many = True)
print(schema.dump(Stack.query.all()))