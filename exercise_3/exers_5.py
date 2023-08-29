import requests


for _ in range(0, 500 + 1):
    response = requests.get(url=f'https://parsinger.ru/task/1/{_}.html', timeout=1)
    if response.status_code == 200:
        data = response.text
        print(f'https://parsinger.ru/task/1/{_}.html')
        print()
        print(data)