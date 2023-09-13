import requests
from bs4 import BeautifulSoup
import lxml


start_url = 'https://parsinger.ru/table/1/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.704 Yowser/2.5 Safari/537.36'}

response = requests.get(url=start_url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
table_data = soup.find('div', {'class': 'main'}).find_all('td')

print(table_data)

item_list = []
for item in table_data:
    item_list.append(float(item.text))

item_set = sum(set(item_list))
print(item_set)