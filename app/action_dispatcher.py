
from actions import Add, Delete, Info, List, Modify


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

    def call_action(self, hpk_api, action_label, args):
        self._actions[action_label].execute(hpk_api, args)

    def debug_actions(self):
        print(self._actions.keys())
        print(self._actions.values())
