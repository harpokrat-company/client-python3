
from actions.action import Action


class Info(Action):

    def __init__(self):
        super().__init__('info')

    def execute(self, hpk_api, args):
        print("Executing {} action".format(self.label))
        print("TODO")
        return
