import requests
import json

url = 'https://favqs.com/api/quotes?page=<page>&filter=<keyword>'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)

# data = json.loads(response.text)
# print(data)


keyword = input('enter a keyword to search for quotes: ') 
url = f'https://favqs.com/api/quotes?page=<page>&filter={keyword}'
response = requests.get(url)
data = response.json()
print(data)
