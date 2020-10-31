
from actions.action import Action


class Info(Action):

    def __init__(self):
        super().__init__('info')

    def execute(self, hpk_api, args):
        me = hpk_api.me_service.read()
        attributes = me['data']['attributes']
        print("Email: {}".format(attributes['email']))
        print("Prénom: {}".format(attributes['firstName']))
        print("Nom: {}".format(attributes['lastName']))
        print("Adresse email validée: {}".format(
              ("oui" if attributes['emailAddressValidated'] else "non")))
        return
