# 4.9 - 6
from bs4 import BeautifulSoup
import requests
import csv

# открываем файл и записываем туда заголовки таблицы
with open('496res.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        'Наименование', 'Артикул', 'Бренд', 
        'Модель', 'Тип', 'Технология экрана', 
        'Материал корпуса', 'Материал браслета', 
        'Размеры', 'Сайт производителя', 'Цена', 
        'Старая цена', 'Ссылка на карточку с товаром'])

# открываем сайт 
url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')

# составляем список ссылок навигационного меню
pagen = [link['href'] for link in soup.find('div', class_='pagen').find_all('a')]

# идём по каждой ссылке в списке пагинации и составляем список ссылок на все товары
items_all = []
schema = 'https://parsinger.ru/html/'

for page in pagen:
    response = requests.get(url=schema + page)
    response.encoding = 'utf-8'
    page_soup = BeautifulSoup(response.text, 'lxml')
    items_all += [link.find('a')['href'] for link in page_soup.find_all(class_ = 'sale_button')]    

# проходим по списку товаров и переписываем оттуда в файл все значения атрибутов
for item in items_all:
    response = requests.get(url=schema + item)
    response.encoding = 'utf-8'
    item_soup = BeautifulSoup(response.text, 'lxml')
    
    # переписываем в переменные все характеристики
    name = item_soup.find(id = 'p_header').text.strip()
    article = item_soup.find(class_ = 'article').text.strip().split(':')[1].strip()
    brand = item_soup.find(id = 'brand').text.strip().split(':')[1].strip()
    model = item_soup.find(id = 'model').text.strip().split(':')[1].strip()
    type_ = item_soup.find(id = 'type').text.strip().split(':')[1].strip()
    display = item_soup.find(id = 'display').text.strip().split(':')[1].strip()
    material_frame = item_soup.find(id = 'material_frame').text.strip().split(':')[1].strip()
    material_bracer = item_soup.find(id = 'material_bracer').text.strip().split(':')[1].strip()
    size = item_soup.find(id = 'size').text.strip().split(':')[1].strip()
    site = item_soup.find(id = 'site').text.strip().split(':')[1].strip()   
    price = item_soup.find(id = 'price').text.strip()
    old_price = item_soup.find(id = 'old_price').text.strip()
    
    # записываем в файл построчно
    with open('496res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            name, article, brand, model, type_,
            display, material_frame, material_bracer,
            size, site, price, old_price, schema + item])