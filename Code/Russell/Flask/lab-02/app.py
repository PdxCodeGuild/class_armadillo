import json

from flask import Flask, render_template, request

app = Flask(__name__)


def load_database():
    with open('db.json', 'r') as file:
        text = file.read()
    return json.loads(text)
        
def save_db(data):
    with open('db.json', 'w') as file:
        text = json.dumps(data)
        file.write(text)



@app.route('/', methods=['GET', 'POST'])
def index():


    data = load_database()
    if request.method == 'POST':
        print(data["todos"])
    return render_template('index.html', data=data)


# $env:FLASK_APP = "app.py" 
# $env:FLASK_ENV = "development"
# python -m flask run