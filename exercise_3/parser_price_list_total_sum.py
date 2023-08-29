import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url, timeout=3)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
price_list = soup.find('div', {'class': 'item_card'}).find_all('p', {'class': 'price'})
total_price_sum = 0

for price in price_list:
    total_price_sum += int(price.text.strip(' руб'))

print(total_price_sum)