import csv
import requests
from bs4 import BeautifulSoup as BS


#Если у вас в файле иероглифы, не спишите снижать балл!
# Возможно, стоит заменить encoding='utf-8-sig' на encoding='cp1251'

url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BS(response.text, 'lxml')
pagen = [int(link.text) for link in soup.find('div', class_='pagen').find_all('a')][-1]
print(pagen)
menu = [f"https://parsinger.ru/html/'{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]


for i in range(1, len(menu) + 1):
    for j in range(1, pagen + 1):
        url = f'https://parsinger.ru/html/index{i}_page_{j}.html'
        res = requests.get(url=url)
        res.encoding = 'utf-8'
        soup = BS(res.text, 'lxml')
        names = soup.find_all('div', class_='item')
        for i_name in names:
            name_every = i_name.find('a', class_='name_item').text.strip()
            price = i_name.find('p', class_='price').text.strip()
            list_li = i_name.find('div', class_='description').text.split('\n')
            first = list_li[1].split(':')[1]
            second = list_li[2].split(':')[1]
            third = list_li[3].split(':')[1]
            fourth = list_li[4].split(':')[1]

            data = {'Наименование': name_every,  'Бренд': first, 'Тип': second, 'Подключение': third, 'Игровая': fourth,'Цена': price}

            with open('items_all.csv', 'a', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow((name_every, first, second, third, fourth, price))