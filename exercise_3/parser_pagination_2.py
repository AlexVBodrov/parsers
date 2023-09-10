import requests
from bs4 import BeautifulSoup
import lxml

start_url = 'https://parsinger.ru/html/index3_page_4.html'

start_response = requests.get(start_url)
start_response.encoding = 'utf-8'


start_soup = BeautifulSoup(start_response.text, 'lxml')

string_pagen = 'https://parsinger.ru/html/'

list_pagens= [f"{string_pagen}{link['href']}" for link in start_soup.find('div', class_='pagen').find_all('a')]
link_in_cards = []
total = 0
# print(list_pagens)
print('---' * 10)

for link in list_pagens:
    
    link_in_cards_response = requests.get(link)
    link_in_cards_response.encoding = 'utf-8'


    soup = BeautifulSoup(link_in_cards_response.text, 'lxml')

    soup_in_cards = [link for link in soup.find_all('div', class_='sale_button')]

# print(soup_in_cards)


    for link in soup_in_cards:
        for a in link.find_all('a', href=True):
            # print(f"{string_pagen}{a['href']}")
            link_in_cards.append(f"{string_pagen}{a['href']}")


# print(link_in_cards, len(link_in_cards))
for card_url in link_in_cards:
    # card_url = 'https://parsinger.ru/html/mouse/3/3_1.html'

    card_response = requests.get(card_url)
    card_response.encoding = 'utf-8'
    card_soup = BeautifulSoup(card_response.text, 'lxml')

    article = int(card_soup.find('p', class_='article').text.split()[1])
    total += article

print(total)
    
    
