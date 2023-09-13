from bs4 import BeautifulSoup
import requests
import lxml

path_file = 'ex_22\index.html'
path_file_out = 'ex_22/1.txt'


with open(path_file, 'r', encoding='utf-8') as file:
    soup2 = BeautifulSoup(file, 'lxml')
    soup2.encode('utf-8')
    print(soup2)
    with open(path_file_out, 'wb', encoding='utf-8') as f:
        f.write(soup2)
