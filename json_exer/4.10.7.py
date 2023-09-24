import requests
from bs4 import BeautifulSoup
import lxml
import json
# Import time module
import time
# record start time
start = time.time()

def get_soup(link):
    # get soup
    response_card = requests.get(url=link)
    response_card.encoding = 'utf8'
    card_soup = BeautifulSoup(response_card.text, 'lxml')
    return card_soup


# Обязательные Заголовки :  Наименование, Артикул, Бренд, Модель, Наличие, Цена, Старая цена, Ссылка на карточку с товаром,

save_file_path = 'res_4.10.7.json'
result_json = []


index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
for i in range(5):
    for j in range(32):
        card_url = f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html"
        card_soup = get_soup(card_url)

        # заполняем поля
        name = card_soup.find('p', {'id': 'p_header'}).text
        article = card_soup.find('p', {'class': 'article'}).text.split()[1]
        
        # ----------------------
        description_soup = card_soup.find('ul', id='description').find_all('li')
        li_id = [li.get('id') for li in description_soup]
        # description
        description = {}
        for item in li_id:
            description[item] = card_soup.find('li', {'id': f'{item}'}).text.split(': ')[1]

        # ----------------------
        in_stock = card_soup.find('span', {'id': 'in_stock'}).text.split(': ')[1]
        price = card_soup.find('span', {'id': 'price'}).text
        old_price = card_soup.find('span', {'id': 'old_price'}).text
        link = card_url
        
        # save result  ---------------------------------------------------
        result_json.append({
                'categories': 'watch',
                'name': name,
                'article': article,
                'description': description,
                'count': in_stock,
                'price': price,
                'old_price': old_price,
                'link': link,

            })
        
# 4 ------------------------------------------------------
with open(save_file_path, 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
# 4 ------------------------------------------------------

# record end time
end = time.time()
# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :",
      (end-start))
print(f'Файл {save_file_path} создан')