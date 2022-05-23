import pytest
import requests

class TestPhrase:
    names = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")
    ]

    @pytest.mark.parametrize('name', names)
    def testPhrase(self, name):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        data = {'User-Agent': name}

        response = requests.get(url, headers=data)

        assert response.status_code == 200, "Wrong response code"

        expected_platform = response.json()['platform']
        expected_browser = response.json()['browser']
        expected_device = response.json()['device']

        if name == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
            actual_platform = 'Mobile'
            actual_browser = 'No'
            actual_device = 'Android'
        elif name == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
            actual_platform = 'Mobile'
            actual_browser = 'Chrome'
            actual_device = 'iOS'
        elif name == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
            actual_platform = 'Googlebot'
            actual_browser = 'Unknown'
            actual_device = 'Unknown'
        elif name == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
            actual_platform = 'Web'
            actual_browser = 'Chrome'
            actual_device = 'No'
        else:
            actual_platform = 'Mobile'
            actual_browser = 'No'
            actual_device = 'iPhone'

        assert actual_platform == expected_platform, "actual_platform in the response is no correct"
        assert actual_browser == expected_browser, "actual_browser in the response is no correct"
        assert actual_device == expected_device, "actual_device in the response is no correct"
