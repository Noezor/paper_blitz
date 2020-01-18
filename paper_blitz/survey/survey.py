from articles.article import Article

from typing import Tuple

class Survey:
    def __init__(self, link: str):
        self.link = link

    def create(self):
        raise NotImplementedError

class Survey_Articles(Survey):
    def read_results(self) -> List[Tuple[Article, int]]:
        assert self.link is not None
        pass

    def create(self, articles : List[Article]) -> str:
        """
        :returns: link to survey
        """
        pass