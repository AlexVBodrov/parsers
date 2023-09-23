import requests
from bs4 import BeautifulSoup
import json
import lxml

result_json = []

# 1 ------------------------------------------------------
for i in range(1, 32 + 1):
    url = f"https://parsinger.ru/html/mouse/3/3_{i}.html"
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    card_soup = BeautifulSoup(response.text, 'lxml')
# 1 ------------------------------------------------------

    # 2 ------------------------------------------------------
    name = card_soup.find('p', {'id': 'p_header'}).text
    article = card_soup.find('p', {'class': 'article'}).text.split()[1]
    
    # description --------------------------------
    brand = card_soup.find('li', {'id': 'brand'}).text.split()[1]
    model = card_soup.find('li', {'id': 'model'}).text.split()[1]
    type_device = card_soup.find('li', {'id': 'type'}).text.split()[1]
    purpose = card_soup.find('li', {'id': 'purpose'}).text.split()[1]
    light = card_soup.find('li', {'id': 'light'}).text.split()[1]
    size = card_soup.find('li', {'id': 'size'}).text.split()[1]
    dpi = card_soup.find('li', {'id': 'dpi'}).text.split(': ')[1]
    site = card_soup.find('li', {'id': 'site'}).text.split()[1]
    # --------------------------------------------
    
    in_stock = card_soup.find('span', {'id': 'in_stock'}).text.split(': ')[1]
    price = card_soup.find('span', {'id': 'price'}).text
    old_price = card_soup.find('span', {'id': 'old_price'}).text
    card_link = url
    # ___________
    description = card_soup.find('ul', id='description').find_all('li')
    li_id = [li.get('id') for li in description]


    # 2 ------------------------------------------------------
    
    # 3 ------------------------------------------------------
    result_json.append({
            'categories': 'watch',
            'name': name,
            'article': article,
            'description': {
                li_id[0]: brand,
                li_id[1]: model,
                li_id[2]: type_device,
                li_id[3]: purpose,
                li_id[4]: light,
                li_id[5]: size,
                li_id[6]: dpi,
                li_id[7]: site,
                },
            'count': in_stock,
            'price': price,
            'old_price': old_price,
            'link': url,

        })
        
# 4 ------------------------------------------------------
with open('res_4.10.6.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
# 4 ------------------------------------------------------