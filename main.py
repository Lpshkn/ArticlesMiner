import sys
import asyncio
from miner.console.handler import ConsoleHandler
from miner.database.db import Database
from miner.habr.parser import Parser


async def main():
    console_handler = ConsoleHandler(sys.argv[1:])
    db = None
    try:
        db = Database.connect([{'host': console_handler.host, 'port': console_handler.port}])
    except ConnectionError:
        print("The hostname or port of the Elasticsearch server is incorrect, please check it", file=sys.stderr)
        exit(-1)

    parser = Parser(database=db, concurrent=console_handler.concurrent, timeout=console_handler.timeout)
    await parser.parse(count=console_handler.count,
                       min_post=console_handler.min_post, max_post=console_handler.max_post)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
