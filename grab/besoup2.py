import requests
res = requests.get('https://wp.forchange.cn/psychology/11069/')
res.encoding = 'utf-8'
print(res.status_code)