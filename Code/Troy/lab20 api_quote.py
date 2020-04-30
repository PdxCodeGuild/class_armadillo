# Lab 20 API Quote
# Troy Fitzgerald


'''Version 1: Get a Random Quote
The URL to get a random quote is https://favqs.com/api/qotd, send a request here, 
parse the JSON in the response into a python dictionary, and show the quote and 
the author.'''


# imports the functions.
import json
import requests


# requests the url.
requested_url = requests.get('https://favqs.com/api/qotd')
# creates the python dictionary.
requested_data = json.loads(requested_url.text)
# prints the dictionary.
#print(requested_data)


# defines the function to get the quote.
def get_quote():
    quote_response = requests.get('https://favqs.com/api/qotd')
    return json.loads(quote_response.text)
#print(get_quote().keys()) - tested for the keys in the dictionary.
print(get_quote()['quote']['body'])


# defines the function to get the author of the quote.    
def author_response():
    author_response = requests.get('https://favqs.com/api/qotd')
    return json.loads(author_response.text)
print(author_response()['quote']['author'])

    