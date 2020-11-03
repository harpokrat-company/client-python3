
from actions.action import Action


class Info(Action):
    '''Info Class

    This class represents the action of getting all the available informations of your harpokrat account.
    '''

    def __init__(self):
        super().__init__('info')

    def execute(self, hpk_api, args):
        me = hpk_api.me_service.read()
        attributes = me['data']['attributes']
        print("Email: {}".format(attributes['email']))
        print("Surname: {}".format(attributes['firstName']))
        print("Name: {}".format(attributes['lastName']))
        print("Validated email address: {}".format(
              ("yes" if attributes['emailAddressValidated'] else "no")))
        return
