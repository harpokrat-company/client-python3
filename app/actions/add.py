
from actions.action import Action
from utils import ask_question

from harpokrat_client_library.models.domain.password import Password


class Add(Action):
    '''Add Class

    This class represents the action of adding a new password to your harpokrat account.
    '''

    def __init__(self):
        super().__init__('add')

    def execute(self, hpk_api, args):
        max_confirm_error = 3
        name = ask_question('New password name:')
        login = ask_question('Login:')
        password = ask_question('Password:', 'password')
        while ask_question('Confirm password:', 'password') != password:
            if max_confirm_error == 0:
                print('Confirm password failed. Exit.')
                return
            print('Passwords do not match, please retry. ({} tries remaining)'.format(
                max_confirm_error))
            max_confirm_error -= 1
        domain = ask_question('Domain:')
        hpk_api.password_service.create(
            Password(name, login, password, domain, private=False))
        print("Success!")
        return
