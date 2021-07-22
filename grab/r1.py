import requests
url = 'https://wp.forchange.cn/psychology/11069/'
res = requests.get(url)
print(res.status_code)
res.encoding ='utf-8'
print(res.text)
#print(res.__attrs__)
#print(res.cookies)
#print(res.elapsed)
#print(res.encoding)
#print(res.headers)
#print(res.history)
#print(res.raw)
#print(res.reason)
#print(res.request)
#print(res.url)

