from flask import Flask, render_template, request
import json

app = Flask (__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        # saving and loading the database
        def save_database(data):
            with open('database.json', 'w') as file:
                file.write(json.dumps(data))

        def load_database():
            with open('database.json', 'r') as file:
                data = json.loads(file.read())
            return data
    data = save_database()

    # return"Hello World"

