#!/usr/bin/env python3

from HarpokratClientLibrary.HarpokratAPI import HarpokratAPI
from HarpokratClientLibrary.models.domain.Password import Password
from HarpokratClientLibrary.models.domain.User import User

harpokrat_api = HarpokratAPI('https://api.harpokrat.com/v1')

test_user = User('test-eip@gmail.com', '123456789azerty', 'Test', 'EIP')

response1 = harpokrat_api.user_service.create(test_user)
print(response1)

response2 = harpokrat_api.token_service.login(test_user.email, test_user.password)
print(response2)

response3 = harpokrat_api.me_service.me()
#print(response3)

pw = Password('test-eip@gmail.com', '12345', 'http://facebook.com')
response4 = harpokrat_api.user_password_service.create(pw)
print(response4)

pw = Password('d4rk-S4sukE@gmail.com', 'narutox', 'http://naruto.com')
response4 = harpokrat_api.user_password_service.create(pw)
print(response4)

pw = Password('lmbr@kent.ac.uk', 'lZdIIjf2k;', 'http://kent.ac.uk')
response4 = harpokrat_api.user_password_service.create(pw)
print(response4)

pw = Password('tanguyGeromz@hpk.com', 'AzERtY', 'http://hpk.asia')
response4 = harpokrat_api.user_password_service.create(pw)
print(response4)
