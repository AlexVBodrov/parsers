import requests
from fake_useragent import UserAgent

UA = UserAgent()
url = 'http://httpbin.org/user-agent'

for x in range(10):
    fake_ua = {'user-agent': UA.random}
    response = requests.get(url=url, headers=fake_ua)
    print(response.text)
    
    
"""
from fake_useragent import UserAgent as ua
import requests as r

print(*[r.get(url='http://httpbin.org/user-agent', headers={'user-agent': ua().random}).text for i in range(5)])
"""

