import requests
from random import choice
#  http://httpbin.org/
# Сайт http://httpbin.org/ создан специально для веб-разработчиков, чтобы они могли тестировать свой код, отправляя свои запросы.
"""
Если httpbin.org не доступен, используйте

http://ipwho.is/ 
https://api.ipify.org?format=json
"""

url = 'http://httpbin.org/'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.3.823 Yowser/2.5 Safari/537.36"}
response = requests.get(url)
print(type(response), response.text, response)

# Этот код последовательно подставляет user-agent из файла и делает запрос на наш url.
with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)
