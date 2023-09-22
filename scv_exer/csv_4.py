import csv
import requests
from bs4 import BeautifulSoup
# Import time module
import time
# record start time
start = time.time()

save_file_path = 'scv_exer/res_4.csv'
url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
count = 0
# 1 ------------------------------------------------------
# Делаем заголовки (Знаю что: Заголовки Указывать не нужно)
with open(save_file_path, 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Бренд', ' Категория', 'инфо_1', 'инфо_2', 'Цена'])
# 1 ------------------------------------------------------
# get all cards urls
pagen = [int(link.text) for link in soup.find('div', class_='pagen').find_all('a')][-1]

menu = [f"https://parsinger.ru/html/'{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]


for i in range(1, len(menu) + 1):
    for j in range(1, pagen + 1):
        card_url = f'https://parsinger.ru/html/index{i}_page_{j}.html'
        
        # 2 ------------------------------------------------------
        # get card soup
        print(f'get info in card:{card_url}')
        
        
        response = requests.get(url=card_url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        # 2 ------------------------------------------------------

        # 3 ------------------------------------------------------
        # get info
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text for x in soup.find_all('p', class_='price')]
        # print(name, description, price)
        # 3 ------------------------------------------------------

        # 4------------------------------------------------------
        # save info
        for item, descr, price  in zip(name, description, price):
            # 'Наименование', 'Бренд', ' Категория', 'инфо_1', 'инфо_2', 'Цена'
            flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
            file = open(save_file_path, 'a', encoding='utf-8-sig', newline='')
            writer = csv.writer(file, delimiter=';')
            writer.writerow(flatten)
        file.close()
        count += 1
        print(f'прогресс :{count}')

    
# record end time
end = time.time()
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start))
print(f'Файл {save_file_path} создан')