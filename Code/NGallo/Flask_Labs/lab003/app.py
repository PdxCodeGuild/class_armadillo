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
    return render_template('index.html', data = data)

@app.route('/save_to_json', methods=['POST'])
def save_to_json():
    task = request.form['task']
    priority = request.form['priority']
    data = load_database()
    data['todos'].append({"text": task, "priority": priority})
    save_database(data)
    return redirect('/')

# @app.route('/delete_from_json', methods=['post'])
# def delete_from_json():
#   request.form[""]

#   return redirect('/')
    '''Lab 2 Flask TODO
Part 1
Create a folder called lab02 to hold all the files for your lab. Inside that create database.json and add the following content. You can add additional fields if you'd like to.

{
  "todos":[
    {
      "text": "walk the dog",
      "priority": "high"
    },{
      "text":"butter the cat",
      "priority":"medium"
    },{
      "text":"wash dishes",
      "priority":"low"
    }
  ]
}
Create a flask app to load this data with open..., parse it using the json library, and render a template to display the data. Below is an example of parsing and encoding json:

import json

# demonstrating how to go between json and a python dictionary
data = '{"name": "bob"}'
data = json.loads(data) # json string -> python dictionary
print(data['name']) # bob
data = json.puts(data) # python dictionary -> json string
print(data)

# saving and loading the database
def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data
The resulting HTML should look something like this, but feel free to use a table or divs instead.

<ul>
  <li>walk the dog (high)</li>
  <li>butter the cat (medium)</li>
  <li>wash dishes (low)</li>
</ul>
Part 2
Using a form, allow the user to save a new todo item to the database. This should include a input for text, a select for the priority, and a button for submitting the form.
'''