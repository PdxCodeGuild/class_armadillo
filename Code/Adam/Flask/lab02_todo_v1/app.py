from flask import Flask, render_template
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

# receive request at localhost:5000/
@app.route('/', methods=['GET', 'POST'])

def index():
    # declaring the variable data 
    # and assigning it the dictionary returned by the function
    data = load_database()
    # render the the template index.html and pass it the variable agenda 
    return render_template('index.html', agenda = data['agenda'] )