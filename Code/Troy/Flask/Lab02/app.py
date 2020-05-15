# Lab 02 Flask To Do
# Troy Fitzgerald

# imports the modules.
from flask import Flask, render_template, request
import json

#defines variable app and assigns it from Flask.
app = Flask("honey_do_list_app")

# defines the function for chores.
def load_chores():
    # opens the file.
    with open('database.json', 'r') as file:
        # reads the text
        text = file.read()
    # turns the json string into a python dictionary.
    return json.loads(text)

# saving and loading the database
def save_chores(data):
    # opens the file to be written.
    with open('database.json', 'w') as file:
         # python dictionary -> json string
        text = json.dumps(data, indent=4)
        # writes the file.
        file.write(text)
        print(data)


@app.route('/')

def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
    return render_template('index.html')
    


# chore = '{"chore": "mow_the_lawn"}'
# data = json.loads(database) # json string -> python dictionary
# print(data['chore']) # bob

