from PyInquirer import prompt


def ask_question(question, qtype='input'):
    answer = prompt({
        'type': qtype,
        'name': 'result',
        'message': question
    })
    return answer.get('result')


def password_selector(hpk_api):
    '''Password_selector is a function that allows the user to pick a password
    The selected password is returned
    '''
    passwords = hpk_api.password_service.read_all()['data']
    formated_passwords = ["{}: {} - {}".format(id, password['attributes']['domain'],
                                               password['attributes']['login']) for id,
                          password in enumerate(passwords, start=1)]
    result = prompt({
        'type': 'list',
        'name': 'choice',
        'message': 'Select password:',
        'choices': formated_passwords
    })
    id = int(result.get('choice').split(':')[0]) - 1
    return passwords[id]
