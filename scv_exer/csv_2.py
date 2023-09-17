import csv
import requests
from bs4 import BeautifulSoup

save_file_path = 'scv_exer/res_2.csv'
# 1 ------------------------------------------------------
with open(save_file_path, 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', 'Форм-фактор', 'Емкость', 'Объём буф. памяти', 'Цена'])
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
cards_url = 'https://parsinger.ru/html/index4_page_1.html'

response = requests.get(url=cards_url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
# 2 ------------------------------------------------------

# 3 ------------------------------------------------------
# 'Наименование', 'Бренд', 'Форм-фактор', 'Емкость', 'Объём буф. памяти', 'Цена'
name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
# brend = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
# form_factor = [x.text for x in soup.find_all('p', class_='price')]
# value = [x.text for x in soup.find_all('p', class_='price')]
# buffer = [x.text for x in soup.find_all('p', class_='price')]
description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
price = [x.text for x in soup.find_all('p', class_='price')]
# 3 ------------------------------------------------------

# 4------------------------------------------------------

for item, descr, price  in zip(name, description, price):
    flatten = item, *[x.split(':')[1].strip() for x in descr if x], price

    file = open(save_file_path, 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(file, delimiter=';')
    writer.writerow(flatten)
file.close()
print('Файл res.csv создан')