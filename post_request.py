import requests
import json

url_post = "https://jsonplaceholder.typicode.com/posts/"
body_post = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

header_post = {'Content-type': 'application/json; charset=UTF-8'}

resp = requests.post(url=url_post, headers=header_post, json=body_post)

code_status = resp.status_code

print(code_status)
assert code_status == 201

resp_json = resp.json()
print(resp_json['id'])