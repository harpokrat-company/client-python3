#! /usr/bin/python3

from HarpokratClientLibrary.HarpokratAPI import HarpokratAPI
from HarpokratClientLibrary.models.domain.Password import Password
from HarpokratClientLibrary.models.domain.User import User

# Fonctionne sans mais peut être utile
# from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import argparse

harpokrat_api = HarpokratAPI('https://api.harpokrat.com/v1')

def retrieve_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("-l", "--list", help="list passwords",
                        action="store_true")
    parser.add_argument("--shell", help="activate shell mode",
                        action="store_true")
    args = parser.parse_args()
    #print(args)
    return args

def exit_error(code = 0, message=None):
    if message != None:
        print("ERROR: " + message)
    exit(code)    


def ask_password():
#    return 'aledoskour1234'
    questions = [
        {
            'type': 'password',
            'name': 'password',
            'message': 'Enter your HPK password:',
        }
    ]
    answers = prompt(questions)
    if not answers.get('password'):
       exit_error(-1, "Password needed.")
    return answers.get('password')


def shell_mode():
    s = None
    while s != "exit":
        print('> ', end="")
        s = input()
        print(s)


def action(login, password, actions):
    connexion_result = harpokrat_api.token_service.login(login, password);
 #   print(type(connexion_result))
    me = harpokrat_api.me_service.me()
    secrets = harpokrat_api.user_password_service.read_all()
    for s in secrets.data:
        owner_id = s.relationships.get('owner').data.id
        attributes = s.attributes
        if attributes == None or s.relationships.get('owner').data.id != me.data.id:
            continue
        print("===================================")
        print("Login: " + s.attributes.login)
        print("Password: " + s.attributes.password)
        print("Domain: " + s.attributes.domain)
        #print(type(s.attributes))
        #print(s.relationships.get('owner').data.id)
        #print(s.relationships.owner.data.id)


def main():
#    print("python main function")
    args = retrieve_args()
#    print('ARGUMENTS : ', args)
    if args.shell:
        return shell_mode()
    action(args.username, ask_password(), [])


if __name__ == '__main__':
    main()
