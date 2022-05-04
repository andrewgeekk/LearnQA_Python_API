import time
import requests
import json

URL = 'https://playground.learnqa.ru/ajax/api/longtime_job'
response = requests.get(URL)
print(f'Создаем задачу: {response.text}')
obj = json.loads(response.text)
token = obj['token']
seconds = obj['seconds']
response1 = requests.get(URL, params={'token':token})
print(f'Делаем запрос с token ДО того, как задача готова: {response1.text}')
print(f'Ждем {seconds} сек.')
time.sleep(seconds)
response2 = requests.get(URL, params={'token':token})
print(f'Делаем запрос с token ПОСЛЕ того, как задача готова: {response2.text}')
