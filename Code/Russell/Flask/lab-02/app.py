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
    counter = 0
    chores = []
    priority = []
    if request.method == 'GET':
        for _ in data['todos']:
            priority.append(data['todos'][counter]['priority'])
            chores.append(data['todos'][counter]['text'])
            counter += 1
        
        todo_dict = dict(zip(chores,priority))
        print(todo_dict)
           

        return render_template('index.html', data=data, priority=priority, chores=chores, todo_dict=todo_dict)
        
    # return 'hello world'
        


# $env:FLASK_APP = "app.py" 
# $env:FLASK_ENV = "development"
# python -m flask run