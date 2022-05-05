import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
response_amount = len(response.history)
first_response = response.history[0].url
second_response = response.history[1].url
finally_response = response.url

print(f'Итоговый URL: {response.url}')
print(f'Количество редиректов: {response_amount}')

print(first_response, second_response, finally_response, sep='\n')
