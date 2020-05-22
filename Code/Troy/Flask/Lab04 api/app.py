
# imports the module
from flask import Flask, request, render_template
import requests
import json

# class
app = Flask(__name__)

# decorator with a path to the view
@app.route('/', methods=['GET', 'POST'])
# defines the view 
def index():
    # assigns variables to request data from the json database from the url
    get_quote = requests.get('https://favqs.com/api/qotd')
    requested_data = json.loads(get_quote.text)
    author_response = requested_data['quote']['author']
    quote_response = requested_data['quote']['body']
    # returns the author and quote
    return render_template('index.html', author_response=author_response, quote_response=quote_response)

