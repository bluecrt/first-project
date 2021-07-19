import requests
res = requests.get('https://google.com')
print(res)
print(res.status_code)