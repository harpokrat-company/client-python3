from PyInquirer import prompt
from commands.command import Command

from HarpokratClientLibrary.models.domain.Password import Password

# from HarpokratClientLibrary.models.domain.User import User

questions = [
    {
        'type': 'input',
        'name': 'name',
        'message': 'Nom du password:'
    },
    {
        'type': 'input',
        'name': 'username',
        'message': 'Identifiant associé:'
    },
    {
        'type': 'password',
        'name': 'password',
        'message': 'Mot de passe:'
    },
    {
        'type': 'password',
        'name': 'conf_password',
        'message': 'Confirmez mot de passe:'
    },
    {
        'type': 'input',
        'name': 'url',
        'message': 'URL associé:'
    },
    {
        'type': 'confirm',
        'name': 'confirm',
        'message': 'Confirmez:'
    }
]


# TODO faire les lambda validate pour les questions (éviter les inputs vides ou les mdp différents

class Add(Command):
    def __init__(self):
        super().__init__('add')

    def run(self, harpokrat_api, args):
        answers = prompt(questions)
        if not answers.get('confirm'):
            print("Ajout annulé.")
            return
        if answers.get('password') != answers.get('conf_password'):
            print("Mots de passe incorrectes")
            return
        new_pass = Password(answers.get('name'), answers.get('username'), answers.get('password'), answers.get('url'))
        response4 = harpokrat_api.user_password_service.create(new_pass)
        print("Ajout effectué !")
