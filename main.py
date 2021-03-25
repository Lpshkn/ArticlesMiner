import sys
from miner.console.handler import ConsoleHandler
from miner.database.db import Database


def main():
    console_handler = ConsoleHandler(sys.argv[1:])
    try:
        db = Database.connect([{'host': console_handler.host, 'port': console_handler.port}])
    except ConnectionError:
        print("The hostname or port of the Elasticsearch server is incorrect, please check it", file=sys.stderr)
        exit(-1)


if __name__ == '__main__':
    main()
