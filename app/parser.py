
import argparse
from dataclasses import dataclass
from collections import deque


@dataclass
class Arguments:
    username: str
    actions: deque

class Parser:
    '''Parser class allows to abstract the deal with argparse

    It allows to initialise the ArgumentParser from argparse,
    retrieve args, print help and print usage.
    '''

    def __init__(self):
        self._parser = argparse.ArgumentParser(description="The Python Command Line Interface of Harpokrat")
        self.__populate_parser_arguments()

    def __populate_parser_arguments(self):
        '''Private method that sets up the parser from argparse
        '''
        self._parser.add_argument("username")
        self._parser.add_argument("-l", "--list", help="list passwords",
                            action="store_true", dest="list")
        self._parser.add_argument("-a", "--add", help="add a new password",
                            action="store_true", dest="add")
        self._parser.add_argument("-d", "--delete", help="delete a password",
                            action="store_true", dest="delete")
        self._parser.add_argument("-m", "--modify", help="modify a password",
                            action="store_true", dest="modify")
        self._parser.add_argument("-i", "--info", help="give information about user",
                            action="store_true", dest="info")
        self._parser.add_argument("--shell", help="activate shell mode",
                            action="store_true", dest="shell")

    def parse_arg(self) -> Arguments:
        '''Public method that retrieves the args from argparse and format them
        in order to be easily usable (output an Arguments dataclass described above)
        '''
        args = vars(self._parser.parse_args())
        return Arguments(args["username"], deque([key for key in args.keys() if args[key] is True]))

    def print_help(self):
        self._parser.print_help()

    def print_usage(self):
        self._parser.print_usage()
