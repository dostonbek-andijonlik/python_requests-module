import requests
# import json

url1 = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url=url1)
# print(type(response.json()))

code = response.status_code
assert code == 200

list = response.json()
for i in range(0, len(list)):
    id = list[i]['id']
    if(id == 11):
        title = list[i]['title']
assert title == "et ea vero quia laudantium autem", f"title actual and title expected do not matches. Expected title is: {title}"