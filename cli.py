#! /usr/bin/python3

import argparse
import sys

import pyfiglet

from HarpokratClientLibrary.HarpokratAPI import HarpokratAPI

from utils.ask_password import ask_password
from utils.exit_error import exit_error

from commands.list import List
from commands.add import Add

from shell import shell_mode

harpokrat_api = HarpokratAPI('https://api.harpokrat.com/v1')


def retrieve_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("-l", "--list", help="list passwords",
                        action="store_true")
    parser.add_argument("-a", "--add", help="add a new password",
                        action="store_true")
    parser.add_argument("--shell", help="activate shell mode",
                        action="store_true")
    args = parser.parse_args()
    return args, parser


def main():
    print(pyfiglet.figlet_format('Harpokrat'))
    args, parser = retrieve_args()
    password = ask_password()
    ### TODO Améliorer cette partie (important parce que c'est moche)
    if args.shell:
        return shell_mode(harpokrat_api, args.username, password)
    elif args.list:
        connexion_result = harpokrat_api.token_service.login(args.username, password)
        List().run(harpokrat_api, None)
    elif args.add:
        connexion_result = harpokrat_api.token_service.login(args.username, password)
        Add().run(harpokrat_api, None)
    else:
        parser.print_help()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
