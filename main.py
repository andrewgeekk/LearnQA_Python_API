import requests

URL = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
method = {"method":"GET"}
response1 = requests.get(URL)
print(f'1. Без параметра method: {response1.text}')

response2 = requests.head(URL, data='HEAD')
print(f'2. Не из списка HEAD: {response2.text}')

response3 = requests.post(URL, data={"method":"POST"})
print(f'3. с правильным значением method: {response3.text}')

print('4.')
methods = ['POST', 'GET', 'PUT', 'DELETE', 'HEAD']
type = [[requests.get, 'requests.get'], [requests.post, 'requests.post'], [requests.put, 'requests.put'],
        [requests.delete, 'requests.delete'], [requests.head, 'requests.head']]

for i in type:
    for j in methods:
        if i[1] == 'requests.get':
            response = i[0](URL, params={"method":j})
            print(f'{i[1]}({URL}, parasms=["method"="{j}"]):  {response.text}')
        else:
            response = i[0](URL, data={"method": j})
            print(f'{i[1]}({URL}, data=["method"="{j}"]):  {response.text}')