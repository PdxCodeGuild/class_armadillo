from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

@app.route('/', methods=['GET', 'POST'])
def index():
    data = load_database()
    todos = data['todos']
    return render_template('index.html', todos = todos)

@app.route('/save_to_json', methods=['POST'])
def save_to_json():
    task = request.form['task']
    priority = request.form['priority']
    data = load_database()
    data['todos'].append({"text": task, "priority": priority})
    save_database(data)
    return redirect('/')

@app.route('/delete_from_json', methods=['post'])
def delete_from_json():

    data = load_database()
    data['todos'].pop(-1)
    save_database(data)
    return redirect('/')