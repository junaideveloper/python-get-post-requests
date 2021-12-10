import Urllib3

import urllib3

http = urllib3.PoolManager()

url = 'http://google.com'

resp = http.request('GET', url)
print(resp.data.decode('utf-8'))

print(resp)

## Requests method GET

import requests as req

resp = req.get("http://webcode.me")

print(resp.text)
