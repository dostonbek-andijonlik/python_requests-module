import requests
import json

url_dest = "https://jsonplaceholder.typicode.com/posts/1"

json_body = {
    "id": "1",
    "title": "foo",
    "body": "bar",
    "userId": 1
}

headers = {'Content-type': 'application/json; charset=UTF-8'}

resp = requests.put(url=url_dest, headers=headers, json=json_body)
code_status = resp.status_code
print(code_status)
assert code_status == 200
resp_json = resp.json()
print(resp_json['id'])