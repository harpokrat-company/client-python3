
from actions.action import Action

from action_dispatcher import ActionDispatcher

class Shell(Action):
    '''Shell Class

    This class represents the shell mode.
    '''

    def __init__(self):
        super().__init__('shell')
        self.action_dispatcher = ActionDispatcher()

    def execute(self, hpk_api, args):
        while 1:
            print('> ', end="")
            s_in = input()
            action = False
            if s_in == "exit" or s_in == "quit":
                break
            exist = self.action_dispatcher.call_action(hpk_api, s_in, None)
            if exist == False:
                print("No action related to " + s)
        return
