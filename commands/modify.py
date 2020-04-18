from PyInquirer import prompt
from commands.command import Command
import json
from utils.ask_value import ask_value
from HarpokratClientLibrary.models.domain.Password import Password
# from HarpokratClientLibrary.models.domain.User import User

question_selection = {
    'type': 'list',
    'name': 'choice',
    'message': 'Quel mot de passe souhaitez vous modifier ?',
    'choices': []
}

question_choix_modif = {
    'type': 'list',
    'name': 'field',
    'message': 'Que souhaitez vous modifier ?',
    'choices': ['Identifiant', 'Login', 'Mot de passe', 'Domaine']
}


class Modify(Command):
    def __init__(self):
        super().__init__('modify')

    def run(self, harpokrat_api, args):
        choice = []
        secrets = harpokrat_api.user_password_service.read_all()
        me = harpokrat_api.me_service.me()
        filtered_secret = []
        separation = ' - '
        for s in secrets.data:
            attributes = s.attributes
            if attributes == None or s.relationships.get('owner').data.id != me.data.id:
                continue
            choice.append(attributes.domain + separation + attributes.login)
            filtered_secret.append(s)
        question_selection['choices'] = choice
        answers = prompt([question_selection, question_choix_modif])
        if not answers.get('choice'):
            return
        [domain, login] = answers.get('choice').split(separation)
        field = answers.get('field')
        value = ask_value("Nouvelle valeur: ")
        if value == None:
            print("Annulation")
            return
        for s in filtered_secret:
            if s.attributes.login == login and s.attributes.domain == domain:
                new_pass = Password(s.attributes.name,  s.attributes.login, s.attributes.password, s.attributes.domain)
                if field == 'Identifiant':
                    print('dd')
                    new_pass = Password(value, s.attributes.login, s.attributes.password, s.attributes.domain)
                if field == 'Login':
                    print('cc')
                    new_pass = Password(s.attributes.name, value, s.attributes.password, s.attributes.domain)
                if field == 'Mot de passe':
                    print('bb')
                    new_pass = Password(s.attributes.name, s.attributes.login, value, s.attributes.domain)
                if field == 'Domaine':
                    print('aa')
                    new_pass = Password(s.attributes.name, s.attributes.login, s.attributes.password, value)
                print(json.dumps(new_pass))
                harpokrat_api.password_service.update(s.id, new_pass)
                print("Mot de passe modifié")
