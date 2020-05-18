from flask import Flask, render_template, request, redirect
import json


app = Flask(__name__)

#opens db.json, reads the text, turns the json into a python dictionary
def load_database():
    with open('db.json', 'r') as file: #open the file
        text = file.read() # read the text
        return json.loads(text) # turn the json string into a python dictionary

# opens db.json, turns the python dictionary into json, and saves it to the file
def save_database(data):
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)



@app.route('/', methods=['GET', 'POST'])
def index():

    data = load_database()


    return render_template('index.html', value=data['value'], fruits=data['fruits'])

@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = load_database()

    # get the data out of the form
    print(request.form)
    inc_or_dec = request.form['inc_or_dec'] # ImmutableMultiDict([('inc_or_dec', 'increment')])
    print(inc_or_dec)

    # modify the data from the database
    if inc_or_dec == 'increment':
        data['value'] += 1
    else:
        data['value'] -= 1

    # save the database again
    save_database(data)

    # redirect the user back to the homepage
    return redirect('/')
    
    



# $env:FLASK_APP = "app.py" 
# $env:FLASK_ENV = "development"
# python -m flask run