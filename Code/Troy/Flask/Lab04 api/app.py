

from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)


# requests the url.
# requested_url = requests.get('https://favqs.com/api/qotd')
# creates the python dictionary.
# requested_data = json.loads(requested_url.text)
# prints the dictionary.
#print(requested_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    get_quote = requests.get('https://favqs.com/api/qotd')
    requested_data = json.loads(get_quote.text)
    author_response = requested_data['quote']['author']
    quote_response = requested_data['quote']['body']

    return render_template('index.html', author_response=author_response, quote_response=quote_response)

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

# # return render_template('index.html')