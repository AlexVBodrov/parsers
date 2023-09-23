import requests
from bs4 import BeautifulSoup
import json
import lxml

# 1 ------------------------------------------------------
for category in range(1, 5 + 1):
    for page in range(1, 4 + 1):
        url = f"https://parsinger.ru/html/index{category}_page_{page}.html"
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
    # 1 ------------------------------------------------------

        # 2 ------------------------------------------------------
        name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
        description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
        price = [x.text for x in soup.find_all('p', class_='price')]
        # 2 ------------------------------------------------------

        result_json = []
        # 3 ------------------------------------------------------
        for list_item, price_item, name in zip(description, price, name):
            result_json.append({
                'name': name,
                str([x.split(':')[0] for x in list_item][0]) : [x.split(':')[1] for x in list_item][0],
                str([x.split(':')[0] for x in list_item][1]): [x.split(':')[1] for x in list_item][1],
                str([x.split(':')[0] for x in list_item][2]): [x.split(':')[1] for x in list_item][2],
                str([x.split(':')[0] for x in list_item][3]): [x.split(':')[1] for x in list_item][3],
               'price': price_item

            })

        # 3 ------------------------------------------------------

        # 4 ------------------------------------------------------
        with open('res_4.10.5.json', 'a', encoding='utf-8') as file:
            json.dump(result_json, file, indent=4, ensure_ascii=False)
        # 4 ------------------------------------------------------