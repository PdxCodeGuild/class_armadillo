import requests
import string
import json

page = "https://favqs.com/api/qotd"
response = requests.get(page)
# print(response.text)
info = json.loads(response.text)
print(info["quote"] ["body"])
print(info["quote"] ["author"])

