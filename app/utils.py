from PyInquirer import prompt


def ask_question(question, qtype='input'):
    answer = prompt({
        'type': qtype,
        'name': 'result',
        'message': question
    })
    return answer.get('result')
