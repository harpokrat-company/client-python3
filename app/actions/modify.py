
from actions.action import Action


class Modify(Action):

    def __init__(self):
        super().__init__('modify')

    def execute(self, hpk_api, args):
        print("Executing {} action".format(self.label))
        print("TODO")
        return
