import json
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    tasks = load_database()  # Call load database to open the file on GET request
    return render_template("index.html", tasks=tasks["todos"])


# opens db.json, turns the python dictionary into json, and saves it to the file
def load_database():
     with open('db.json', 'r') as file:
         data = json.loads(file.read())
     return data


# opens db.json, turns the python dictionary into json, and saves it to the file
def save_database(data):
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)


@app.route('/save_task', methods=['POST'])
def save_task():
    task = request.form["task"]
    priority = request.form["priority"]
    data = load_database()
    data['todos'].append({
        "text": task,
        "priority": priority,
        })
    save_database(data)

    return redirect('/')


@app.route('/delete_task', methods=['post'])
def delete_task():
    task_index = request.form["task_index"]
    data = load_database()
    data['todos'].pop(int(task_index))
    save_database(data)

    return redirect('/')