

from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)


def read_database():
    with open('database.json') as file:
        data = json.loads(file.read())
    return data

def write_database(data):
    data = json.dumps(data, indent=2)
    with open('database.json', 'w') as file:
        file.write(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = read_database()

    # words = [('apple', 3), ('banana', 4), ('pineapple', 8)]
    # priorities = {'1': 'high', '2': 'medium', '3': 'low'}
    # data['todos'].sort(key=lambda x: x['priority'])

    return render_template('index.html', todos=data['todos'])


@app.route('/savetodo/', methods=['POST'])
def savetodo():
    text = request.form['todo_text']
    priority = request.form['todo_priority']
    todo = {
        'text': text,
        'priority': priority
    }
    data = read_database()
    data['todos'].append(todo)
    write_database(data)
    return redirect('/')


@app.route('/deletetodo/', methods=['POST'])
def deletetodo():
    todo_index = int(request.form['todo_index'])
    data = read_database()
    data['todos'].pop(todo_index)
    write_database(data)
    return redirect('/')



