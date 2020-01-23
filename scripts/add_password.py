#!/usr/bin/env python3

from HarpokratClientLibrary.HarpokratAPI import HarpokratAPI
from HarpokratClientLibrary.models.domain.Password import Password
from HarpokratClientLibrary.models.domain.User import User

harpokrat_api = HarpokratAPI('https://api.harpokrat.com/v1')

test_user = User('test-eip@gmail.com', '123456789azerty', 'jpp', 'flantier')

response2 = harpokrat_api.token_service.login(test_user.email, test_user.password)
#print(response2)

response3 = harpokrat_api.me_service.me()
#print(response3)

pw = Password('MDPajouté', '12345', 'http://random.com')
response4 = harpokrat_api.user_password_service.create(pw)
print(response4)
