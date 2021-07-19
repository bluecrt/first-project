import requests
res = requests.get('https://www.google.com')
res_type = type(res)
print(res_type)