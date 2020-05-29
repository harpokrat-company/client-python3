#! /usr/bin/python3

import argparse
import sys

from dataclasses import dataclass

import pyfiglet

from HarpokratClientLibrary.HarpokratAPI import HarpokratAPI

from utils.ask_password import ask_password

from commands.command import Command
from commands.list import List
from commands.add import Add
from commands.delete import Delete
from commands.info import Info
from commands.modify import Modify

from shell import shell_mode

harpokrat_api = HarpokratAPI('https://api.harpokrat.com/v1')

@dataclass
class ArgCommand:
    name: str
    action: type(Command)

argcommands = [
    ArgCommand('list', List),
    ArgCommand('add', Add),
    ArgCommand('delete', Delete),
    ArgCommand('info', Info),
    ArgCommand('modify', Modify),
]


def retrieve_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("-l", "--list", help="list passwords",
                        action="store_true")
    parser.add_argument("-a", "--add", help="add a new password",
                        action="store_true")
    parser.add_argument("-d", "--delete", help="delete a password",
                        action="store_true")
    parser.add_argument("-m", "--modify", help="modify a password",
                        action="store_true")
    parser.add_argument("-i", "--info", help="give information about user",
                        action="store_true")
    parser.add_argument("--shell", help="activate shell mode",
                        action="store_true")
    args = parser.parse_args()
    return args, parser


def if_arg(args):
    for argcommand in argcommands:
        if vars(args)[argcommand.name]:
            return True
    return False


def main():
    print(pyfiglet.figlet_format('Harpokrat'))
    args, parser = retrieve_args()
    if not args.shell and not if_arg(args):
        parser.print_help()
        return
    password = ask_password()
    if args.shell:
        return shell_mode(harpokrat_api, args.username, password)
    elif if_arg(args):
        connexion_result = harpokrat_api.token_service.login(args.username, password)
        for argcommand in argcommands:
            if vars(args)[argcommand.name]:
                argcommand.action().run(harpokrat_api, None)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
