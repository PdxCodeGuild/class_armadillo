# Lab 02 Flask To Do
# Troy Fitzgerald

# imports the modules.
from flask import Flask, render_template, request
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


    # if request.method == 'POST':
    #     contact_name = request.form['input_text']
    #     print(contact_name)
    # return render_template('index.html')
    


# chore = '{"chore": "mow_the_lawn"}'
# data = json.loads(database) # json string -> python dictionary
# print(data['chore']) # bob

