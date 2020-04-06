from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://favqs.com/api/qotd')
    data = json.loads(response.text)
    quote_author = data['quote']['author']
    quote_text = data['quote']['body']
    return render_template('index.html', quote_author=quote_author, quote_text=quote_text)

