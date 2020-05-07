import requests
import json


keyword = input("enter a keyword to search for quotes: ")
# make formatted string to use lines 6 for category
url = f'https://favqs.com/api/quotes?page=1&filter={keyword}'

headers = {"Authorization": 'token token="855df50978dc9afd6bf86579913c9f8b"'}
response = request.get(url, headers=headers)
print(response.text)