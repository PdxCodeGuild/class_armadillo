from flask import Flask, render_template, request, redirect
import json

app = Flask('do-it_app')

# opens database.json, reads the text, turns the json into a python dictionary
def load_database():
    with open('database.json', 'r') as file: # open the file
        text = file.read() # read the text
    return json.loads(text) # turn the json string into a python dictionary

# opens database.json, turns the python dictionary into json, and saves it to the file
def save_database(data):
    with open('database.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)

# by default views can only receive GET requests
@app.route('/')
def index():
    data = load_database()
    return render_template('index.html', doit=data['doit'])


@app.route('/enter_task', methods=['POST'])
def enter_task():
    # load the database
    data = load_database()
    new_text = request.form['new_text']
    new_pri = request.form['new_pri']
    task = {
        'text': new_text,
        'priority': new_pri,
    }
    data['doit'].append(task)

    save_database(data) # save the data to the database

    return redirect('/')









