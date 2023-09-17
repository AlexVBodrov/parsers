import csv
import requests
from bs4 import BeautifulSoup

save_file_path = 'scv_exer/res.csv'
# 1 ------------------------------------------------------
with open(save_file_path, 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Цена', 'Бренд', 'Тип', 'Подключение', 'Игровая'])
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
url = 'http://parsinger.ru/html/index3_page_2.html'

response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
price = [x.text for x in soup.find_all('p', class_='price')]
# 3 ------------------------------------------------------

# 4------------------------------------------------------

for item, price, descr in zip(name, price, description):
    flatten = item, price, *[x.split(':')[1].strip() for x in descr if x]

    file = open(save_file_path, 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(file, delimiter=';')
    writer.writerow(flatten)
file.close()
print('Файл res.csv создан')