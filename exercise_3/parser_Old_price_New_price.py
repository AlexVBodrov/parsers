import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://parsinger.ru/html/hdd/4/4_1.html'

response = requests.get(url, timeout=3)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
price = int(soup.find('span', {'id': 'price'}).text.strip(' руб'))
old_price = int(soup.find('span', {'id': 'old_price'}).text.strip(' руб'))

# Формула (старая цена - новая цена) * 100 / старая цена)

result = (old_price - price) * 100 / old_price
print(result)





