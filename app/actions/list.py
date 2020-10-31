
from actions.action import Action


class List(Action):
    '''List Class

    This class represents the action of listing all the passwords of your harpokrat account.
    '''

    def __init__(self):
        super().__init__('list')

    def execute(self, hpk_api, args):
        passwords = hpk_api.password_service.read_all()['data']
        print("{} password(s) found.".format(len(passwords)))
        for password in passwords:
            print("===================================")
            print("Name: {}".format(password['attributes']['name']))
            print("Login: {}".format(password['attributes']['login']))
            print("Password: {}".format(password['attributes']['password']))
            print("Domain: {}".format(password['attributes']['domain']))
        return
