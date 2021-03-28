# ArticlesMiner

Articles scrapper from the follow sites: 
* [Habr](https://habr.com/ru)

# Using
1. `git clone https://github.com/Lpshkn/ArticlesMiner articlesminer`
2. `cd articlesminer`
3. `docker build -t articlesminer:1.0.0 .`
4. You must to specify Elasticsearch connection parameters as environment values 
   (using database.env, for example) or command line arguments. For example,  
   `docker run --env-file database.env articlesminer:1.0.0`
   
# Arguments and commands

The program has the follow commands:
* habr - to parsing [Habr](https://habr.com/ru) and saving posts to an Elasticsearch cluster.

## Arguments of the Habr command:

* `-host` - the host address of the Elasticsearch cluster
* `-port` - the port of the Elasticsearch cluster
* `--min_post` - the number of the first post to be parsed from (by default, 1)
* `--max_post` - the number of the post to which the parsing will be performed (by default, 1000000)
* `-c` - the count of parsed articles
* `--concurrent` - count of concurrent tasks: it may be speed up the process of parsing (by default, 4)
* `-t` - timeout to make request in seconds (by default, 0)

# Examples

## Using the `habr` command
The follow command will load 100 posts beginning from the 100000 post id using 8 concurrent tasks and timeout 5 seconds:
```shell
docker run --env-file database.env articlesminer:1.0.0 habr -c --min-post 100000 --concurrent 8 -t 5
```