
from actions.action import Action


class List(Action):

    def __init__(self):
        super().__init__('list')

    def execute(self, hpk_api, args):
        print("Executing {} action".format(self.label))
        print("TODO")
        return
