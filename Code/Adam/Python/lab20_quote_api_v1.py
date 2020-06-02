"""
Lab 20 Quote API

For this lab we'll be using the Favqs Quotes API to first get a random quote, and then allow the user to find 
quotes by keyword. To accomplish this we'll be using the requests and json libraries. The example below uses a 
Chuck Norris joke API.

import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url) # send the request to the api
print(response.text) # look at the raw json
data = json.loads(response.text) # turn the json into a python dictionary
print(data['value']) # get a part of the response data out of the dictionary

Version 1: Get a Random Quote

The URL to get a random quote is https://favqs.com/api/qotd, send a request here, parse the JSON in the 
response into a python dictionary, and show the quote and the author.

"""


import requests
import json

url = 'https://favqs.com/api/qotd'
response = requests.get(url) # send the request to the api
# print(response.text) # look at the raw json
data = json.loads(response.text) # turn the json into a python dictionary
print(f" \"{data['quote']['body']}\" - {data['quote']['author']}") # get a part of the response data out of the dictionary
# print(data['quote']['author'])

