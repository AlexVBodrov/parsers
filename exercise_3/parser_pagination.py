import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
string = 'https://parsinger.ru/html/'
pagen = [f"{string}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
res = []
for i in range(len(pagen)):
    url = pagen[i]
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    b = soup.find_all('a', class_='name_item')
    names = []
    for name in b:
        names.append(name.text)
    res.append(names)
print(res)