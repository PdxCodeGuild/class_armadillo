from flask import Flask, render_template, request
import json

app = Flask(__name__)

#Part 1 

# loads data from db.json, returns a dictionary
def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

# save data to the db.json
def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

@app.route('/', methods=['GET', 'POST'])
def index():
        list = load_database()
        return render_template('index.html', list=list['todos'])

#Part 2

@app.route('/save', methods=['GET', 'POST'])
def save():
    list = load_database()
    list["todos"].append(request.form)
    save_database(list)
    return "saved!"