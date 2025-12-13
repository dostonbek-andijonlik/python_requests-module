import requests
import json

url_delete = "https://jsonplaceholder.typicode.com/posts/1"

body_json = {
    "id": "1",
    "title": "foo",
    "body": "bar",
    "userId": 1
}

headers_data = {'Content-type': 'application/json; charset=UTF-8'}

resp = requests.delete(url=url_delete, headers=headers_data, json=body_json)

code_status = resp.status_code
assert code_status == 200
print(code_status)

resp_json = resp.json()

print(resp_json)