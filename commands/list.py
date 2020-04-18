from commands.command import Command


# from HarpokratClientLibrary.models.domain.Password import Password
# from HarpokratClientLibrary.models.domain.User import User

class List(Command):
    def __init__(self):
        super().__init__('list')

    def run(self, harpokrat_api, args):
        secrets = harpokrat_api.user_password_service.read_all()
        me = harpokrat_api.me_service.me()
        for s in secrets.data:
            owner_id = s.relationships.get('owner').data.id
            attributes = s.attributes
            if attributes == None or s.relationships.get('owner').data.id != me.data.id:
                continue
            print("===================================")
            print("Login: " + s.attributes.login)
            print("Password: " + s.attributes.password)
            print("Domain: " + s.attributes.domain)
