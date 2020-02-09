from paper_blitz.stack.model import Participant, Stack, Group
from paper_blitz.articles.article import Article
from paper_blitz.config import db
from paper_blitz.create_survey import Article_Selector_Survey


group = Group.query.filter(Group.name == "3DV").one_or_none()

article_selector = Article_Selector_Survey()
print(article_selector.select_articles(group, None))