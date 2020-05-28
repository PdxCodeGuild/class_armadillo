# Lab 20 Quote API
# For this lab we'll be using the Favqs Quotes API to first get a 
# random quote, and then allow the user to find quotes by keyword.
#  To accomplish this we'll be using the requests and json libraries.
#   The example below uses a Chuck Norris joke API.

import requests
import json



url = requests.get('https://favqs.com/api/qotd')
data = json.loads(url.text)

# defines function to get quote
def quotes():
    # send a request to the api
    get_quote = requests.get('https://favqs.com/api/qotd')
     # turn json string into a python dictionary
    return json.loads(get_quote.text)
print(quotes()['quote']['body'])

def response():
    response = requests.get('https://favqs.com/api/qotd')
    # turn json string into a python dictionary
    return json.loads(response.text)
print(response()['quote']['author'])





# from secrets 
# import chuck_norris_api_key



# url = 'https://api.chucknorris.io/jokes/random'
# # send the request to the api
# response = requests.get(url) 
# # look at the raw json
# print(response.text) 
# # turn the json into a python dictionary
# data = json.loads(response.text) 
# #  # get a part of the response data out of the dictionary
# print(data['value'])

# site to pull from
# url = "https://favqs.com/api/qotd"
# # send API request
# response = requests.get(url)
# # looks at the text in JSON 
# print(response.text)
# # create a variable that represents a python dictionary
# silly = json.loads(response.text)

# print(silly['value'])


# "I'd just as soon play tennis with the net down." - "Robert Frost"


# Version 1: Get a Random Quote
# The URL to get a random quote is https://favqs.com/api/qotd, send 
#   a request here, parse the JSON in the response into a python 
#   dictionary, and show the quote and the author.