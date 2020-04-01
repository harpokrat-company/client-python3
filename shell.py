from commands.list import List
from commands.add import Add
from commands.delete import Delete

commands = [
    List(),
    Add(),
    Delete()
]


def shell_mode(harpokrat_api, username, password):
    connexion_result = harpokrat_api.token_service.login(username, password)
    s = None
    action = False
    while 1:
        print('> ', end="")
        s = input()
        action = False
        if s == "exit":
            break
        for command in commands:
            if command.get_label() == s:
                command.run(harpokrat_api,'qaa')
                action = True
        if action == False:
            print("No action related to " + s)
                
