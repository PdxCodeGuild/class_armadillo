from flask import Flask, render_template, request, redirect
import json

app = Flask('increment_app')

# JSON can only contain: null (None in python), booleans, ints, floats, strings, arrays(list in python), objects

def load_database():
    with open('db.json', 'r') as file:# open the file
        text = file.read() # read the file
    return json.loads(text) # convert JSON string into a python dict

#opens db.json, turns the python dictionary into json, and saves it into the file
def save_database():
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) #turn the python dictionary into a json string
        file.write(text)

# request/response cycle 1
# 1. user goes to localhost: 5000 and sends a GET request, which goes to the 'index' view
# 2. server responds with the rendered template containing the form

# request/response cycle 2
# 3. user submits the form, which goes to 'submit_form'
# 4. user responds with a redirect - the same as request/response cycle 1

# by default views can only receive GET requests

@app.route('/')
def index():
    data = load_database()
    return render_template('index.html' , value=data['value'], fav_nums=data['fav_nums'])


@app.route('/submit_form', methods=['POST'])
def submit_form():

    data = load_database()

    print(request.form) #immutableMultiDict
    inc_or_dec = request.form['inc_or_dec'] # increment
    print(inc_or_dec)


    if inc_or_dec == 'increment':
        data['value'] += 1
    else:
        data['value'] -= 1

        # save the data to a database
        save_database(data)

    # redirect brings you to a separate URL
    return redirect('/')

@app.route('/save_number', methods=['POST'])
def save_number():
    mynumber = request.form['mynumber']
    print(mynumber)
    print(type(mynumber))
    mynumber = int(mynumber) # the value from the form is a string by default
    data = load_database()
    data['fav_nums'].append(mynumber)
    data['fav_nums'].sort()
    save_database(data)