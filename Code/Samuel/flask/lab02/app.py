from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_database():
    with open('db.json', 'r') as file:
        text = file.read()
    text = json.loads(text)
    
    return text

def save_database(data):
    with open('db.json', 'w') as file:
        text = json.dumps(data)
        file.write(text)

@app.route("/")
def index_start():
    text = load_database()
    tasks = list()
    for task in (text["todos"]):
        tasks.append(task["text"] + " (" + task["priority"] + ")")
    return render_template("index.html", tasks = tasks)

@app.route("/submit_task", methods=["POST"])
def submit_task():
    task = {"text": request.form["task"],
    "priority": request.form["priority"]}
    data = load_database()
    data["todos"].append(task)
    save_database(data)
    return redirect("/")