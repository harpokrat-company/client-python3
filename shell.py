from commands.list import List
from commands.add import Add
from commands.delete import Delete
from commands.info import Info
from commands.modify import Modify

commands = [
    List(),
    Add(),
    Delete(),
    Info(),
    Modify()
]


def shell_mode(harpokrat_api, username, password):
    connexion_result = harpokrat_api.token_service.login(username, password)
    s = None
    action = False
    while 1:
        print('> ', end="")
        s = input()
        action = False
        if s == "exit" or s == "quit":
            break
        for command in commands:
            if command.get_label() == s:
                command.run(harpokrat_api, None)
                action = True
        if not action:
            print("No action related to " + s)
