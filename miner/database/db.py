import elasticsearch
from miner.database.model import Article


class Database:
    def __init__(self):
        self._es = None

    @staticmethod
    def connect(hosts, /):
        """
        Implements connecting to the Elasticsearch cluster and returns the Database object containing
        this connection.

        :param hosts: a list of hosts
        :return: Database object
        """
        database = Database()
        database._es = elasticsearch.Elasticsearch(hosts=hosts)

        if database._es.ping():
            Article.init(using=database._es)
            return database
        else:
            raise ConnectionError("The connection to Elasticsearch wasn't made")

    @property
    def connection(self):
        return self._es

    def add(self, doc_id: int, author: str, text: str, /, title: str = None, date: str = None):
        """
        Method inserts new document in the index.

        :param doc_id: the id of the document
        :param author: the nickname of the author
        :param text: the body of the document
        :param title: the title of the document
        :param date: the date of creating
        """
        article = Article(meta={'id': doc_id}, author=author, text=text, title=title, date=date)
        article.save(using=self.connection)
