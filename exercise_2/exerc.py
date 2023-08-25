# _ 1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя, сохранить JSON-вывод в файле *.json.
# https://api.github.com/users/USERNAME/repos

import requests
import time
import json
from pprint import pprint

USERNAME = 'AlexVBodrov'  # input('Введите username: ')


url = f'https://api.github.com/users/{USERNAME}/repos'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
response = requests.get(url)

data = response.json()

src = response.text


with open("exercise_2/index.html", "w") as file:
    file.write(src)

    
print('Получен результат:')
pprint(data)

repo = []
for item in data:
    repo.append(item['name'])
print(f'Список репозиториев пользователя {USERNAME}')
pprint(repo)

with open(f'exercise_2/{USERNAME}_repos.json', 'w') as f:
    json_repo = json.dump(repo, f)
