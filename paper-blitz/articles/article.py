from typing import List

class Author:
    def __init__(self, name : str, institution : str):
        self.name = name
        self.institution = institution

class Article:
    def __init__(self, title: str = None, authors : List[Author], year: int = None, abstract : str):
        self.title = title
        self.authors = authors
        self.year = year
        self.abstract = abstract