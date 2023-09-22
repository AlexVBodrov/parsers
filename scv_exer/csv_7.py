import requests
from bs4 import BeautifulSoup
import lxml
import csv


def get_soup(link):
    # get soup
    response_card = requests.get(url=link)
    response_card.encoding = 'utf8'
    card_soup = BeautifulSoup(response_card.text, 'lxml')
    return card_soup


# Обязательные Заголовки :  Наименование, Артикул, Бренд, Модель, Наличие, Цена, Старая цена, Ссылка на карточку с товаром,

save_file_path = 'csv_4.9.7.csv'

with open(save_file_path, 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена',  'Ссылка на карточку с товаром'])


index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
for i in range(5):
    for j in range(32):
        card_url = f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html"
        card_soup = get_soup(card_url)

        # заполняем поля
        name = card_soup.find('p', {'id': 'p_header'}).text
        article = card_soup.find('p', {'class': 'article'}).text.split()[1]
        brand = card_soup.find('li', {'id': 'brand'}).text.split()[1]
        model = card_soup.find('li', {'id': 'model'}).text.split()[1]
        in_stock = card_soup.find('span', {'id': 'in_stock'}).text.split(': ')[1]
        price = card_soup.find('span', {'id': 'price'}).text
        old_price = card_soup.find('span', {'id': 'old_price'}).text
        card_link = card_url

        # 4------------------------------------------------------
        # save info
        list_row = (name, article, brand, model, in_stock, price, old_price, card_link)
        with open(save_file_path, 'a', encoding='utf-8-sig', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(list_row)
