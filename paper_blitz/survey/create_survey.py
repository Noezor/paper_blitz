from paper_blitz.stack.model import Participant, Stack, Group
from paper_blitz.articles.article import Article
from paper_blitz.config import db

from datetime import datetime, timedelta


class Article_Selector_Survey(object):
    def select_articles(self, group : Group):
        non_presented_articles = group.non_presented_articles()
        
        articles_current_week = [article for article in non_presented_articles if self.is_submission_current_week(article)]
        old_articles = [article for article in non_presented_articles if article not in articles_current_week]

        return articles_current_week, old_articles

    def is_submission_current_week(self, article : Stack):
        return (article.added + timedelta(days = 7)) > datetime.now()

