import urllib3
import certifi

http = urllib3.PoolManager(ca_certs=certifi.where())

url = 'https://httpbin.org/post'

req = http.request('POST', url, fields={'name': 'John Doe',
    'occupation': 'gardener'})
print(req.data.decode('utf-8'))


## Requests method POST

import requests as req

data = {'name': 'Peter'}

resp = req.post("https://httpbin.org/post", data)
print(resp.text)