import json
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def index():
    tasks = load_database()
    return render_template("index.html", tasks=tasks["todos"])

# # saving and loading the database
# def save_database(data):
#     with open('database.json', 'w') as file:
#         file.write(json.dumps(data))

def load_database():
     with open('db.json', 'r') as file:
         data = json.loads(file.read())
     return data

# opens db.json, reads the text, turns the json into a python dictionary

# opens db.json, turns the python dictionary into json, and saves it to the file
def save_database(data):
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data) # turn the python dictionary into a json string
        file.write(text)


@app.route('/save_task', methods=['POST'])
def save_task():
    print(request.form)
    task = request.form["task"]
    priority = request.form["priority"]
    data = load_database()
    data['todos'].append({
        "text": task,
        "priority": priority,
        })
    save_database(data)

    return redirect('/')
