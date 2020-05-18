import json
from flask import Flask, render_template, request

app = Flask(__name__)

def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data

def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data, indent=4))    

@app.route('/', methods = ['GET','POST'])
def index():
    text= ''
    priority = ''
    result= ''
    data = load_database()
    if request.method == "POST": 
        task = request.form['task']
        priority = request.form['priority']
        todos = {'text': task,
                 'priority': priority}
        data["todos"].append(todos)        
        save_database(data) 
        result = data["todos"]
        
    return render_template('index.html', todos=data['todos'])

