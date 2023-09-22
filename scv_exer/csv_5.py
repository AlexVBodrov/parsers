import requests
from bs4 import BeautifulSoup
import lxml
import csv

# получим кол-во страниц ссылок
start_url = 'https://parsinger.ru/html/index1_page_1.html'
start_response = requests.get(start_url)
pagen_len = len(BeautifulSoup(start_response.text, 'lxml').find(
    'div', {'class': 'pagen'}).find_all('a'))

# ----------------------------------------------------------------
# Схема урл
main_part_link = 'https://parsinger.ru/html/'

# Получим Ссылки на карточку с товаром
list_links_in_cards = []

for i in range(1, pagen_len + 1):
    # ссылки страниц
    page_url = f'https://parsinger.ru/html/index1_page_{i}.html'
    response_page = requests.get(url=page_url)
    response_page.encoding = 'utf8'
    page_soup = BeautifulSoup(response_page.text, 'lxml').find(
        'div', {'class': 'item_card'}).find_all('div', {'class': 'sale_button'})
    for link in page_soup:
        for a in link.find_all('a', href=True):
            list_links_in_cards.append(f"{main_part_link}{a['href']}")

# ----------------------------------------------------------------

# Создаем Обязательные Заголовки :
# Наименование, Артикул, Бренд, Модель, Тип, Технология экрана, Материал корпуса, Материал браслета, Размер, Сайт производителя, Наличие, Цена, Старая цена,  Ссылка на карточку с товаром.

save_file_path = 'csv_5.csv'

with open(save_file_path, 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана', 'Материал корпуса',
                    'Материал браслета', 'Размер', 'Сайт производителя', 'Наличие', 'Цена', 'Старая цена',  'Ссылка на карточку с товаром'])

for link in list_links_in_cards:
    response_card = requests.get(url=link)
    response_card.encoding = 'utf8'
    card_soup = BeautifulSoup(response_card.text, 'lxml')
    # заполняем поля
    name = card_soup.find('p', {'id': 'p_header'}).text
    article = card_soup.find('p', {'class': 'article'}).text.split()[1]
    brand = card_soup.find('li', {'id': 'brand'}).text.split()[1]
    model = card_soup.find('li', {'id': 'model'}).text.split()[1]
    type_model = card_soup.find('li', {'id': 'type'}).text.split(': ')[1]
    display = card_soup.find('li', {'id': 'display'}).text.split(': ')[1]
    material_frame = card_soup.find('li', {'id': 'material_frame'}).text.split(': ')[1]
    material_bracer = card_soup.find('li', {'id': 'material_bracer'}).text.split(': ')[1]
    size = card_soup.find('li', {'id': 'material_bracer'}).text.split(': ')[1]
    site = card_soup.find('li', {'id': 'site'}).text.split(': ')[1]
    in_stock = card_soup.find('span', {'id': 'in_stock'}).text.split(': ')[1]
    price = card_soup.find('span', {'id': 'price'}).text
    old_price = card_soup.find('span', {'id': 'old_price'}).text
    card_link = link

    # 4------------------------------------------------------
    # save info
    list_row = (name, article, brand, model, type_model, display, material_frame, material_bracer, size, site, in_stock, price, old_price, card_link)
    file = open(save_file_path, 'a', encoding='utf-8-sig', newline='')
    writer = csv.writer(file, delimiter=';')
    writer.writerow(list_row)
    file.close()
