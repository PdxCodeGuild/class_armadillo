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

# source : https://docs.python.org/3/library/json.html
        #   https://www.w3schools.com/python/python_json.asp
    



@app.route('/')
def index():
    chores = load_form() # CULPRIT
    chore_list = request.form['chores']
    return render_template('index.html', chores=chores)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    # load database
    data = load_form()

    #get data from form
    print(request.form) 

     # ImmutableMultiDict([('inc_or_dec', 'increment')])
    chore_list = request.form['chores']
    print(chore_list)

    # save data to the database
    save_form(data)

    #redirect the user back to the home page
    return redirect('/')

