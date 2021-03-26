import sys
from miner.console.handler import ConsoleHandler
from miner.database.db import Database
from miner.habr.parser import Parser


def main():
    console_handler = ConsoleHandler(sys.argv[1:])
    db = None
    try:
        db = Database.connect([{'host': console_handler.host, 'port': console_handler.port}])
    except ConnectionError:
        print("The hostname or port of the Elasticsearch server is incorrect, please check it", file=sys.stderr)
        exit(-1)

    parser = Parser(10, timeout=0)
    parser.parse(database=db)


if __name__ == '__main__':
    main()
