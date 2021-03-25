"""
This module represents functions for options of the command line.
Also module implements a class containing information about the project and all the information that
will be printed in the command line.
"""
import os
import re
import argparse


class ConsoleHandler:
    NAME = 'articles-miner'
    DESCRIPTION = ''
    EPILOG = 'LPSHKN, 2021'

    def __init__(self, args):
        self._parser = self._get_parser(ConsoleHandler.NAME, ConsoleHandler.DESCRIPTION, ConsoleHandler.EPILOG)

        # Get parameters from the arguments received from the command line
        self._parameters = self._get_parameters(args)

    @staticmethod
    def _get_parser(program_name: str = None, description: str = None, epilog: str = None) -> argparse.ArgumentParser:
        """
        Method creates the instance of the ArgumentParser class, adds arguments in here and returns that instance.

        :param program_name: name of the program
        :param description: description of the program
        :param epilog: epilog of the program
        :return: an instance of the ArgumentParser class
        """
        parser = argparse.ArgumentParser(prog=program_name, description=description, epilog=epilog)
        subparsers = parser.add_subparsers(title='Sites', dest='site')

        # Info mode
        habr = subparsers.add_parser('habr',
                                     help='parse Habr.com')
        habr.add_argument('-host',
                          help='the host address of the Elasticsearch cluster',
                          default=os.getenv('ES_HOST'),
                          type=str)

        habr.add_argument('-port',
                          help='the port of the Elasticsearch cluster',
                          default=os.getenv('ES_PORT'),
                          type=str)

        habr.add_argument('--min_post',
                          help='the number of the first post to be parsed from',
                          default='1',
                          type=str)

        habr.add_argument('--max_post',
                          help='the number of the post to which the parsing will be performed',
                          type=str)

        habr.add_argument('-c', '--count',
                          help='the count of parsed articles',
                          type=int)

        return parser

    def _get_parameters(self, args):
        """
        This method gets all parameters from the args of the command line.

        :param args: list of the arguments of the command line
        :return: parsed arguments
        """
        parameters = self._parser.parse_args(args)

        if parameters.site is None:
            self._parser.error("You must specify a command: habr")

        return parameters

    @property
    def command(self) -> str:
        return self._parameters.command

    @property
    def host(self) -> str:
        if (host := self._parameters.host) is None:
            self._parser.error("hostname of Elasticsearch server wasn't specify, please, enter it or set ES_HOST "
                               "environment value")

        return host

    @property
    def port(self) -> str:
        if (port := self._parameters.port) is None:
            self._parser.error("port of Elasticsearch server wasn't specify, please, enter it or set ES_PORT "
                               "environment value")

        return port
