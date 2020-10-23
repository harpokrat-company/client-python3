
from actions.action import Action


class Delete(Action):

    def __init__(self):
        super().__init__('delete')

    def execute(self, hpk_api, args):
        print("Executing {} action".format(self.label))
        print("TODO")
        return
