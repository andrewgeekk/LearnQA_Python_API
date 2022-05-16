import pytest
import requests

class TestPhrase:
    def testPhrase(self):
        url = 'https://playground.learnqa.ru/api/homework_cookie'
        response = requests.get(url)
        print(response.cookies)
        assert response.status_code == 200, "Wrong response code"

