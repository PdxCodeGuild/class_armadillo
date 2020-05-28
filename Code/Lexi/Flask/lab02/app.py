# PART UN: Create a folder called lab02 to hold all the files for your lab. Inside that create database.json and add the following content. You can add additional fields if you'd like to.

# PART DEUX: Using a form, allow the user to save a new todo item to the database. This should include a input for text, a select for the priority, and a button for submitting the form.

from flask import Flask, render_template, redirect, request
import json

app = Flask(__name__)

def load_form():
    with open('db.json', 'r') as file:
        data = json.loads(file.read())
    return data

def save_form(data):
    with open('db.json', 'w') as file:
        file.write((json.dumps(data, indent=4))) #sending it to the form to be converted to JSON from python

# source : https://docs.python.org/3/library/json.html, N.Kalinin's code
        #   https://www.w3schools.com/python/python_json.asp
    
@app.route('/', methods = ['GET','POST'])
def index():
    chore = ''
    priority = ''
    result= ''
    data = load_form()
    if request.method == "POST": 
        task = request.form['task']
        priority = request.form['priority']
        chores = {'chore': task,
                 'priority': priority}
        data["chores"].append(chores)        
        save_form(data) 
        result = data["chores"]
        
    return render_template('index.html', chores=data['chores'])
