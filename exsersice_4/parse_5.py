import requests
from bs4 import BeautifulSoup
import lxml

start_url = 'https://parsinger.ru/table/5/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.704 Yowser/2.5 Safari/537.36'}

response = requests.get(url=start_url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

list_keys =[tag.text for tag in soup.find_all('th')]
# print(list_keys)

# f'table tr td:nth-of-type({i+1})'
# soup.select('table tr td:nth-of-type(1)')
#  f'table tr td:nth-of-type({i+1})
# round(x, n) — данные х округляют до n знаков после точки.

list_values = []
for i in range(1, 15 + 1):
    values = [float(tag.text) for tag in soup.select(f"table tr td:nth-of-type({i})")]
    value = round(sum(values), 3)
    list_values.append(value)

result = dict(zip(list_keys, list_values))
print(result)