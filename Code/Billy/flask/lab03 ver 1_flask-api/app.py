from flask import Flask, render_template, request, redirect
import json
import requests

app = Flask('kool_kwotes_api')

# by default views can only receive GET requests
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kotd/') # decorator - path to the view
def qotd(): # view - function that receives the request and returns the response
    response = requests.get('https://favqs.com/api/qotd')
    data = response.json()
    print(data)
    return render_template('kotd.html', kwote=data['quote']['body'], author=data['quote']['author']) # the response we're returning












