import requests
import urllib.request
from bs4 import BeautifulSoup
import re

from paper_blitz.articles.article import Article

class Arxiv_Parser:
    def scrape(self, link : str) -> Article:
        link_url = self.correct_link(link)
        print(f"Scrapping {link_url}")
        response = requests.get(link_url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        title = self.get_title(soup)
        # publication_date = self.get_submission_date(soup)
        authors = self.get_authors(soup)

        return Article(link = link, title = title, authors = authors)

    def get_title(self, soup):
        return re.sub("\[[0-9]*\.[0-9]*\] ","",soup.title.string)

    def get_submission_date(self, soup):
        return soup.find("div", class_= "dateline").string.lstrip().lstrip("(Submitted on ").rstrip(')')

    def get_authors(self, soup):
        return soup.find("div", class_= "authors").get_text().lstrip("Authors:")

    def correct_link(self, link : str) -> str:
        """
        returns corrected arxiv link
        """
        link = self._correct_pdf_link(link)
        return link

    def _correct_pdf_link(self, link : str ) -> str:
        return link.replace('/pdf/', '/abs/').rstrip(".pdf")