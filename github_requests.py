import requests 
import json

url_github_timeline = 'https://api.github.com/events'
r = requests.get(url=url_github_timeline)
resp_json = r.json()
beautified_json = json.dumps(resp_json, indent=4, sort_keys=True)
# print(beautified_json)

payload = {'1': '1', '2': '2'}
r2 = requests.get('https://httpbin.org/get', params=payload)
resp_json2 = r.json()
# print(r2.url)

url3 = 'https://httpbin.org/get'
payload3 = {"key1": "value1", "key2": ["value2", "value3"]}
r3 = requests.get(url=url3, params=payload3)
resp_json3 = r3.json()
print(resp_json3)

