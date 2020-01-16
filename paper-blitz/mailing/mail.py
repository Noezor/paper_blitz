from articles.article import Article

from datetime import date
from typing import List

class Mail:
    def __init__(self, receiver : str, content : str):
        self.receiver = receiver
        self.content = content


class Article_Presentation_Mail(Mail):
    """
        mail to present a chosen article
    """
    def content(self, receiver : str, article : Article, date_presentation : date, place_presentation : place):  
        #TODO write mail
        content = f"""r
        """
        return content


class Survey_Mail(Mail):
    """
        mail to announce survey
    """
    def content(self, receiver : str, survey : Survey_Articles, presentation : Presentation):
        #TODO write mail
        content = f"""
        """
        return content

class Randomly_Picked_Mail(Mail):
    """
    Send mail to warn that an article submitted to stack by receiver was picked
    and that he should tell us if not available
    """
    def content(self, receiver : str, picked_article : Article, survey : Survey_Articles, presentation : Presentation):
        content = f"""
        """
        return content