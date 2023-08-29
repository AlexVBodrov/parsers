from bs4 import BeautifulSoup
import requests

url = 'http://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
div = soup.find('div', 'item').find_all('li')
for txt in div:
    print(txt.text)