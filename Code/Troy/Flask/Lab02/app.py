# Lab 02 Flask To Do
# Troy Fitzgerald

# imports the modules.
from flask import Flask, render_template, request, redirect
import json

#defines variable app and assigns it from Flask.
app = Flask(__name__)

# defines the function for chores.
def load_chores():
    # opens the file.
    with open('database.json', 'r') as file:
        # reads the text
        text = file.read()
    # turns the json string into a python dictionary.
    return json.loads(text)

# saving and loading the database.
def save_chores(data):
    # opens the file to be written.
    with open('database.json', 'w') as file:
        # python dictionary -> json string
        text = json.dumps(data, indent=4)
        # writes the file.
        file.write(text)
        # print(data)

# view is set to GET and POST.
@app.route('/', methods=['GET', 'POST'])
# assigns the function.
def index():
    # assigns variable to the function. 
    data = load_chores()
    # renders the template and runs the html file and accesses the value at the specified objects json key.
    return render_template('index.html', honey_do_list=data['honey_do_list'])    

@app.route('/save_honey_do_list/', methods=['POST'])

def save_honey_do_list():
    chore = request.form['chore']
    priority = request.form['priority']
    print(chore)
    data = load_chores()
    data['honey_do_list'].append({'chore':chore})
    data['honey_do_list'].append({'priority':priority})
    # data['honey_do_list'].sort()
    save_chores(data)

    return redirect('/')
