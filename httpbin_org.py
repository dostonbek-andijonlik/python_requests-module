import requests
import json

url1 = "https://httpbingo.org/get"
resp = requests.get(url=url1)
# if  resp.status_code == 200:
#     print("Service is working")
# else:
#     print("Service is not available")
#     print(resp.status_code)

resp_json = resp.json()
# print(resp_json['origin'])

# beautified_json = json.dumps(resp_json, indent=4, sort_keys=True)
# print(beautified_json)
print(resp_json['headers']['Host'])