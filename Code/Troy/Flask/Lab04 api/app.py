

from flask import Flask request render_templates
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello World"


# # requests the url.
# requested_url = requests.get('https://favqs.com/api/qotd')
# # creates the python dictionary.
# requested_data = json.loads(requested_url.text)
# # prints the dictionary.
# #print(requested_data)


# # defines the function to get the quote.
# def get_quote():
#     quote_response = requests.get('https://favqs.com/api/qotd')
#     return json.loads(quote_response.text)
# #print(get_quote().keys()) - tested for the keys in the dictionary.
# print(get_quote()['quote']['body'])


# # defines the function to get the author of the quote.    
# def author_response():
#     author_response = requests.get('https://favqs.com/api/qotd')
#     return json.loads(author_response.text)
# print(author_response()['quote']['author'])