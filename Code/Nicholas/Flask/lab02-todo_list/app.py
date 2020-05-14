import json
from flask import Flask, render_template, request


def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

def save_database(todos):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))    

app = Flask(__name__)
@app.route('/', method = ['GET','POST'])

def index():
    data = load_database()

    return render_template('index.html', todos = data["todos"])