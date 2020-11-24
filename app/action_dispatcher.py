
from actions import Add, Delete, Info, List, Modify, Shell


class ActionDispatcher:

    def __init__(self):
        self._actions = dict()
        # Register all actions
        self.__register_all()

    def __register(self, action):
        self._actions[action.label] = action

    def __register_all(self):
        self.__register(Add())
        self.__register(Delete())
        self.__register(Info())
        self.__register(List())
        self.__register(Modify())
        self.__register(Shell())

    def call_action(self, hpk_api, action_label, args):
        if (self._actions.get(action_label) == None):
            return False
        self._actions[action_label].execute(hpk_api, args)
        return True

    def debug_actions(self):
        print(self._actions.keys())
        print(self._actions.values())
