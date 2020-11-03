
from PyInquirer import prompt
from harpokrat_client_library.models.domain.password import Password

from actions.action import Action
from utils import password_selector, ask_question


class Modify(Action):

    def __init__(self):
        super().__init__('modify')

    def execute(self, hpk_api, args):
        password = password_selector(hpk_api)
        new_password = Password(
            password['attributes']['name'],
            password['attributes']['login'],
            password['attributes']['password'],
            password['attributes']['domain'],
            private=False)
        fields = prompt({
            'type': 'checkbox',
            'name': 'fields',
            'message': 'Which fields to modify?',
            'choices': [{'name': 'Password name'}, {'name': 'Login'}, {'name': 'Password'}, {'name': 'Domain'}]
        }).get('fields')
        if len(fields) == 0:
            return
        if 'Password name' in fields:
            new_password['name'] = ask_question('New password name:')
        if 'Login' in fields:
            new_password['login'] = ask_question('New login:')
        if 'Password' in fields:
            new_password['password'] = ask_question(
                'New password:', 'password')
        if 'Domain' in fields:
            new_password['domain'] = ask_question('New domaine:')
        hpk_api.password_service.update(password['id'], new_password)
        print('Success!')
        return
