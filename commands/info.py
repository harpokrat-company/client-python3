from commands.command import Command


# from HarpokratClientLibrary.models.domain.Password import Password
# from HarpokratClientLibrary.models.domain.User import User

class Info(Command):
    def __init__(self):
        super().__init__('info')

    def run(self, harpokrat_api, args):
        me = harpokrat_api.me_service.me()
        attributes = me.data.attributes
        print("Email: %s" % attributes.email)
        print("Prénom: %s" % attributes.firstName)
        print("Nom: %s" % attributes.lastName)
        print("Adresse email validée: %s" % ("oui" if attributes.emailAddressValidated else "non"))

