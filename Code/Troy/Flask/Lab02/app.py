# Lab 02 Flask To Do
# Troy Fitzgerald

# imports the modules.
from flask import Flask, render_template, request
import json

#defines variable app and assigns it from Flask.
app = Flask("honey_do_list_app")



chore = '{"chore": "mow_the_lawn"}'
data = json.loads(database) # json string -> python dictionary
print(data['chore']) # bob
data = json.puts(database) # python dictionary -> json string
print(database)

def load_database():
    with open('database.json', 'r') as file:
        data = json.loads(file.read())
    return data
# saving and loading the database
def save_database(data):
    with open('database.json', 'w') as file:
        file.write(json.dumps(data))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        contact_name = request.form['input_text']
        print(contact_name)
    return render_template('index.html')