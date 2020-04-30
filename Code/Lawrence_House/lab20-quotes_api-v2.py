import requests
import json

keyword = input('Enter a keyword to search for quotes: ')

url = f"https://favqs.com/api/quotes?page=1&filter={keyword}"
print(url)
headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}
response = requests.get(url, headers=headers)
data = json.loads(response.text)
data1 = data['quotes']

print(data1[0]['body'])


input(f"Enter 'next page' or 'done': ")




# data = {'page': 1, 'last_page': False, 'quotes': [{'id': 0, 'favorites_count': 0, 'favorite': False, 'dialogue': False, 'body': 'No quotes found', 'tags': []}]}
# if data['quotes'][0]['body'] == 'No quotes found':

# data['quotes'][0]['body']

