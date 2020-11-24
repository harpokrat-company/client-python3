
class Action:
    '''Action Class is an abstract class inherited by all actions
    '''

    def __init__(self, label):
        self.label = label

    def execute(self, hpk_api, args):
        print("Executing {} action".format(self.label))
        return
