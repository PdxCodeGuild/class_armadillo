from flask import Flask, render_template, request
import json
# Create a string object from flask; acts as a central registry for the
# view functions, the URL rules, template configuration.
app = Flask(__name__)


def load_database():
    # read data from json file
    with open('db.json', 'r') as file:
        # convert the json file to python dictonary
        # and assign it to the variable data
        data = json.loads(file.read())
        # function returns that dictinary
    return data


def save_database(data):
    # open and write to the json file
    with open('db.json', 'w') as file:
        #converting the python dict to a json string
        file.write(json.dumps(data))

# receive request at localhost:5000/
@app.route('/', methods=['GET', 'POST'])
def index():
    # declaring the variable data
    # and assigning it the dictionary returned by the function
    data = load_database()

    if request.method == "POST":
        # request input from the forms and assign those values to the declared variables
        text_input = request.form['text_input']
        priority_input = request.form['priority_input']
        # decalare todo and assign it a dictionary containing the forms input
        todo = {
            'todo': text_input,
            'priority': priority_input
        }
        # add todo to the list of dictionaries
        data['agenda'].append(todo)

        # call function
        save_database(data)

    # render the the template index.html and pass it the variable agenda
    return render_template('index.html', agenda=data['agenda'])
