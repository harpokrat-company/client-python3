
from actions.action import Action
from utils import password_selector


class Delete(Action):

    def __init__(self):
        super().__init__('delete')

    def execute(self, hpk_api, args):
        password = password_selector(hpk_api)
        hpk_api.password_service.delete(password['id'])
        print("Success!")
        return
