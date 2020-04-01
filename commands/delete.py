from PyInquirer import prompt, print_json
from commands.command import Command

# from HarpokratClientLibrary.models.domain.Password import Password
# from HarpokratClientLibrary.models.domain.User import User

question = {
        'type': 'list',
        'name': 'choice',
        'message': 'Quel mot de passe souhaitez vous supprimer ?',
        'choices': []
}

choice = []

class Delete(Command):
    def __init__(self):
        super().__init__('delete')

    def run(self, harpokrat_api, args):
        secrets = harpokrat_api.user_password_service.read_all()
        me = harpokrat_api.me_service.me()
        filtered_secret = []
        separation = ' - ' 
        for s in secrets.data:
            owner_id = s.relationships.get('owner').data.id
            attributes = s.attributes
            if attributes == None or s.relationships.get('owner').data.id != me.data.id:
                continue
            choice.append(attributes.domain + separation + attributes.login)
            filtered_secret.append(s)
            # print("===================================")
            # print("Login: " + s.attributes.login)
            # print("Password: " + s.attributes.password)
            # print("Domain: " + s.attributes.domain)
        question['choices'] = choice
        answers = prompt([question])
        [domain, login] = answers.get('choice').split(separation)
        print(domain)
        print(login)
        for s in filtered_secret:
            if s.attributes.


