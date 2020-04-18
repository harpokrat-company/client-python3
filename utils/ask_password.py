from PyInquirer import prompt, print_json

from utils.exit_error import exit_error


def ask_password():
    questions = [
        {
            'type': 'password',
            'name': 'password',
            'message': 'Enter your HPK password:',
        }
    ]
    answers = prompt(questions)
    if not answers.get('password'):
        exit_error(-1, "Password needed.")
    return answers.get('password')
