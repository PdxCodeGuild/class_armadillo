import requests
import json

url = 'https://favqs.com/api/qotd'
response = requests.get(url) # send the request to the api
data = json.loads(response.text) # turn the json into a python dictionary
data1 = data['quote'] # get a part of the response data out of the dictionary

print(f"{data1['body']}  - {data1['author']}") # Concatenates the quote and author.