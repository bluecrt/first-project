import requests
from bs4 import BeautifulSoup
url = 'https://wp.forchange.cn/psychology/11069/'
res = requests.get(url)
print(res.status_code)
res.encoding = 'utf-8'
bs = BeautifulSoup(res.text,'html.parser')
#print(bs)
print(res.text)
