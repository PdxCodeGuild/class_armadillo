import requests
import json

# site we are using
url = 'https://api.chucknorris.io/jokes/random'
# send API request
response = requests.get(url)
# look at the text in raw JSON format
print(response.text)
# create a variable that represents a python dictionary
# https://www.w3schools.com/python/python_json.asp
joke = json.loads(response.text)

print(f'The joke is : "{joke["value"]}".')
