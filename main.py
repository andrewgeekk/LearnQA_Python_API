import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
response_amount = response.history[-1]
print(f'Итоговый URL: {response_amount.url}')
print(f'Количество редиректов: {len(response.history)}')
for i in range(len(response.history)):
    print(f'{i+1}) {response.history[i].url}')