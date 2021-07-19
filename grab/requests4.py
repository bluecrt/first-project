import requests
res = requests.get('https://www.taobao.com')
res.encoding = 'utf-8'
text = res.text

print(text)