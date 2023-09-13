import requests
from bs4 import BeautifulSoup
import lxml


start_url = 'https://parsinger.ru/table/3/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.704 Yowser/2.5 Safari/537.36'}

response = requests.get(url=start_url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
list_firsts_tr = soup.find_all('b')
print(list_firsts_tr)
# tag.attrs
tags_list = []
for tag in list_firsts_tr:
    tags_list.append(float(tag.text))

print(sum(tags_list))