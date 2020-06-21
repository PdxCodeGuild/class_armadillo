from flask import Flask
import json


app = Flask(__name__)


def load_database():
    with open('db.json', 'w') as file:
        data = json.loads(file.read())
    return data

def save_data(data):
    with open('db.json', 'w') as file:
        file.write(json.dumps(data))


@app.route('/')

def index():
    return 'Hello World!'