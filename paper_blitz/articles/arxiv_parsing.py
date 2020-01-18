from article import Article

class Arxiv_Parser:
    def parse(self, link : str) -> Article:
        return Article(link = link, title = title, authors = authors, date_publication = date_publication,
            venue = venue)

    def corrects_link(self, link : str) -> str:
        """
        returns corrected arxiv link
        """
        link = self._correct_pdf_link(self, link)
        return link

    def _correct_pdf(self, link : str ) -> str:
        return link.replace('/pdf/', '/abs/')