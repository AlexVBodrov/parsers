import requests
from bs4 import BeautifulSoup
import lxml


start_url = 'https://parsinger.ru/table/5/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.7.5.704 Yowser/2.5 Safari/537.36'}

response = requests.get(url=start_url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
blue_list_tags = soup.select('td:last-child')

blue_list = []
for tag in blue_list_tags:

    blue_list.append(float(tag.text))




orange_list_tags = soup.select('.orange')

orange_list = []
for tag in orange_list_tags:
    orange_list.append(float(tag.text))

print(orange_list)
print()
print(blue_list)

print(len(orange_list))
total = 0
for i in range(len(orange_list)):
    num = orange_list[i] * blue_list[i]
    total += num
    
print(total)