from random import choice
import time
import requests

url = 'http://httpbin.org/ip'
filename = 'proxy.txt'
filter_proxy = r"filter_proxy_3.txt"
my_ip_file = 'my_ip.txt'

with open(my_ip_file) as f:
    for ip in f.readlines():
        my_ip = ip.strip()

with open(filename) as file, open(filter_proxy, 'w') as fpr:
    for ip in file.readlines():
        ip = ip.strip()
        try:
            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }
            response = requests.get(url=url, proxies=proxy, timeout=5)

            print(response.json(), 'Success connection')
            if my_ip in response.json().get('origin'):
                print('!!!! Содержит мой IP')
            else:
                fpr.write(f'{ip}\n')

        except Exception as _ex:
            print()
            print(_ex)
            print()
            print(f'status {ip}: False')
            print()
            print('-' * 50)
            print()
            time.sleep(1)
            continue

#--------------------------------------
#Для socks4
proxy_socks4 = {
    'http':'socks4://103.177.45.3:80',
    'https':'socks4://103.177.45.3:80',

}
#--------------------------------------
#Для socks5
proxy_socks5 = {
    'http':'socks5://103.177.45.3:80',
    'https':'socks5://103.177.45.3:80',
}


#--------------------------------------
#Для всех, с авторизацией
proxy_all_auth = {
    'http':'socks5://login:password@103.177.45.3:80',
    'https':'socks5://login:password@103.177.45.3:80',
}