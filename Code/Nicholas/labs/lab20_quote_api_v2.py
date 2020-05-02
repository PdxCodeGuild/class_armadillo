import requests
import json


page = 1
keyword = input('enter a keyword to search for quotes: ') 
url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
data = json.loads(response.text)


for quotes in data['quotes']: 
    print({quotes['body']})
    print({quotes['author']})

