from article import Article, Author

class Arxiv_Parser:
    def parse(self, link : str) -> Article:
        pass

    def correct(self, link : str) -> str:
        """
        returns corrected arxiv link
        """
        link = self._correct_pdf_link(self, link)
        return link

    def _correct_pdf(self, link : str ) -> str:
        return link.replace('/pdf/', '/abs/')