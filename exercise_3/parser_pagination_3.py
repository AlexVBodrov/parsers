import requests
from bs4 import BeautifulSoup
import lxml


TOTAL_COST = 0

# получим стартовую страницу

# Проходимся по всем категориям,
# страницам 
# и карточкам с товарами(всего 160шт)

index_labels = {1: "watch", 2: "mobile", 3: "mouse", 4: "hdd", 5: "headphones"}
for i in range(5):
    for j in range(32):
        card_url = f"https://parsinger.ru/html/{index_labels[i+1]}/{i+1}/{i+1}_{j+1}.html"
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.4.971 Yowser/2.5 Safari/537.36'}
        response = requests.get(url=card_url, headers=headers)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')
        # price
        price = int(soup.find(id="price").text.split()[0])
        # in_stock
        soup = BeautifulSoup(response.text, 'lxml')
        in_stock = int(soup.find(id="in_stock").text.split()[2])
        card_cost = price * in_stock
        TOTAL_COST += card_cost

print(TOTAL_COST)