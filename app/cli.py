
from parser import Parser
from action_dispatcher import ActionDispatcher
from PyInquirer import prompt


class CLI:

    def __init__(self):
        self._parser = Parser()
        self.arguments = self.__parse_arg()
        # TODO Change the value of hpk_api using the library
        self.action_dispatcher = ActionDispatcher()
        self.hpk_api = None

    def __parse_arg(self):
        return self._parser.parse_arg()

    def print_usage(self):
        self._parser.print_usage()

    def retrieve_password(self) -> str:
        answer = str()
        while len(answer) == 0:
            answer = prompt({
                'type': 'password',
                'name': 'password',
                'message': 'Enter your HPK password:',
            })['password']
        return answer

    def run(self):
        if len(self.arguments.actions) == 0:
            self.print_usage()
            return
        # TODO CONNEXION USING THE PYTHON LIBRARY AND THE USERNAME
        self.retrieve_password()

        for action in self.arguments.actions:
            self.action_dispatcher.call_action(self.hpk_api, action, None)
            # self.action_dispatcher.debug_actions()
