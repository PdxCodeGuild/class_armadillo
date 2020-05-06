import requests
import json

url = 'https://favqs.com/api/qotd'
response = requests.get(url)

# print(response.text)

data = json.loads(response.text)

print(data['quote']['body'])
print(data['quote']['author'])
