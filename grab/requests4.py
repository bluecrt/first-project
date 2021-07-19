import requests
res = requests.get('https://www.baidu.com')
res.encoding = 'utf-8'
#text = res.text

#print(text)
print(res.status_code)