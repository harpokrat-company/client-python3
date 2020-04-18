#! /usr/bin/python3

import argparse
import sys

import pyfiglet

from HarpokratClientLibrary.HarpokratAPI import HarpokratAPI

from utils.ask_password import ask_password
from utils.exit_error import exit_error

from commands.list import List
from commands.add import Add
from commands.delete import Delete
from commands.info import Info

from shell import shell_mode

harpokrat_api = HarpokratAPI('https://api.harpokrat.com/v1')


def retrieve_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("-l", "--list", help="list passwords",
                        action="store_true")
    parser.add_argument("-a", "--add", help="add a new password",
                        action="store_true")
    parser.add_argument("-d", "--delete", help="delete a password",
                        action="store_true")
    parser.add_argument("-i", "--info", help="give information about user",
                        action="store_true")
    parser.add_argument("--shell", help="activate shell mode",
                        action="store_true")
    args = parser.parse_args()
    return args, parser


def if_arg(args):
    if args.list or args.add or args.delete or args.info:
        return True
    return False


def main():
    print(pyfiglet.figlet_format('Harpokrat'))
    args, parser = retrieve_args()
    if not args.shell and not if_arg(args):
        parser.print_help()
        return
    password = ask_password()
    ### TODO Améliorer cette partie (important parce que c'est moche)
    if args.shell:
        return shell_mode(harpokrat_api, args.username, password)
    elif if_arg(args):
        connexion_result = harpokrat_api.token_service.login(args.username, password)
        if args.list:
            List().run(harpokrat_api, None)
        if args.add:
            Add().run(harpokrat_api, None)
        if args.delete:
            Delete().run(harpokrat_api, None)
        if args.info:
            Info().run(harpokrat_api, None)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
