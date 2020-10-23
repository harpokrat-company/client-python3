
from actions.action import Action


class Add(Action):

    def __init__(self):
        super().__init__('add')

    def execute(self, hpk_api, args):
        print("Executing {} action".format(self.label))
        print("TODO")
        return
