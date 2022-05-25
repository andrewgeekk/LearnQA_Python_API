import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRigister(BaseCase):
    # names['email'])
    names = [({
        'password': '123',
        'username': 'learnqa',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': 'vinkotov@example.com'}),
    ({	'password': '123',
        'username': '1',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': 'vinkotov@example.com'}),
    ({
        'password': 'X4PXG8RVFXLNN3OOO8BXRWKIYS47NKFK7KMH9KWCU2L2Q6NGV59CRHD4EZ24QOISKDHKI9AVRA0TU1EVF6SPX0E5LB777ZNBOUNK6QLGCKISSJKE0IFU262R18GTR9A29U6XEAQEMMBJ5ZCVKC66B0LQ9PZLVJS0JH27VI3BCMZ3EQKL8B9OFFS4HW021NUDTMYVCCTQX6NALB91LV8CM8RZXG155OH5R4T4LCDJPJRQ4CPG0WZKKLECB0J',
        'username': 'learnqa',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': 'vinkotov@example.com'}),
    ({
        'password': '123',
        'username': 'learnqa',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': 'vinkotovexample.com'}),
    ({
        'password': '123',
        'username': 'learnqa',
        'lastName': 'learnqa',
        'email': 'vinkotovexample.com'})
    ]
    @pytest.mark.parametrize('name', names)

    def test_create_user_with_existing_email(self, name):

        url = 'https://playground.learnqa.ru/api/user/'
        data = name

        response = requests.post(url, data=data)

        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{name['email']}' already exists", f"Unexpected response content {response.content}"


