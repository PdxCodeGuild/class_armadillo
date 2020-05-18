import json

from flask import Flask, render_template, request, redirect

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
    counter = 0
    chores = []
    priority = []
    if request.method == 'GET':
        for _ in data['todos']:
            priority.append(data['todos'][counter]['priority'])
            chores.append(data['todos'][counter]['text'])
            counter += 1
        
    todo_dict = dict(zip(chores,priority))

        
    return render_template('index.html', data=data, todo_dict=todo_dict, chores=chores, priority=priority)



@app.route('/save_chore', methods=['POST']) 
def save_chore():

    data = load_database()
    print(data)
    print(request.form)
    data['todos'].append(request.form)
    print(data)
    save_db(data)
    return redirect('/')     
    
        



















# $env:FLASK_APP = "app.py" 
# $env:FLASK_ENV = "development"
# python -m flask run