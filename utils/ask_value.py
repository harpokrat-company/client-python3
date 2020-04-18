from PyInquirer import prompt


def ask_value(question):
    questions = [
        {
            'type': 'input',
            'name': 'text',
            'message': question,
        },
        {
            'type': 'confirm',
            'name': 'confirm',
            'message': 'Confirmez:'
        }
    ]
    answers = prompt(questions)
    if not len(answers.get('text')) > 0 or not answers.get('confirm'):
        return None
    return answers.get('text')
