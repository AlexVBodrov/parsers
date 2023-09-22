import csv
import requests
from bs4 import BeautifulSoup

save_file_path = 'scv_exer/res_3.csv'
# 1 ------------------------------------------------------
with open(save_file_path, 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', ' Категория', 'инфо_1', 'инфо_2', 'Цена'])
# 1 ------------------------------------------------------

# 2 ------------------------------------------------------
for i in range(1, 4 + 1):
    cards_url = f'https://parsinger.ru/html/index4_page_{i}.html'

    response = requests.get(url=cards_url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    # 2 ------------------------------------------------------

    # 3 ------------------------------------------------------

    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
    price = [x.text for x in soup.find_all('p', class_='price')]
    # 3 ------------------------------------------------------

    # 4------------------------------------------------------

    for item, descr, price  in zip(name, description, price):
        # 'Наименование', 'Бренд', ' Категория', 'инфо_1', 'инфо_2', 'Цена'
        flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
        file = open(save_file_path, 'a', encoding='utf-8-sig', newline='')
        writer = csv.writer(file, delimiter=';')
        writer.writerow(flatten)
    file.close()

print(f'Файл {save_file_path} создан')