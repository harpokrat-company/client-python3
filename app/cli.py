
from parser import Parser
from action_dispatcher import ActionDispatcher
from PyInquirer import prompt

from harpokrat_client_library.harpokrat import Harpokrat

hpk_api_url = 'https://api.dev.harpokrat.com:443/v1'


class CLI:

    def __init__(self):
        self._parser = Parser()
        self.arguments = self.__parse_arg()
        # TODO Change the value of hpk_api using the library
        self.action_dispatcher = ActionDispatcher()
        self.hpk_api = Harpokrat(hpk_api_url)

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
        # TODO ADD EXCEPTION SYSTEM ABOVE THE HPK_API (MAYBE IMPLEMENT DECORATOR ?)
        self.hpk_api.token_endpoint.login(
            self.arguments.username, self.retrieve_password())
        for action in self.arguments.actions:
            self.action_dispatcher.call_action(self.hpk_api, action, None)
            # self.action_dispatcher.debug_actions()
