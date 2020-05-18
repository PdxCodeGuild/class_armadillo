from flask import Flask, render_template, request
import json

app = Flask('do-it_app')

# opens database.json, reads the text, turns the json into a python dictionary
def load_database():
    with open('database.json', 'r') as file: # open the file
        text = file.read() # read the text
    return json.loads(text) # turn the json string into a python dictionary

# by default views can only receive GET requests
@app.route('/')
def index():
    data = load_database()
    return render_template('index.html', doit=data['doit'])
    







