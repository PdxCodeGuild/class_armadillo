from flask import Flask, render_template, request, redirect
import json

app = Flask('increment_app')


# opens db.json, reads the text, turns the json into a python dictionary
def load_database():
    with open('db.json', 'r') as file: # open the file
        text = file.read() # read the text
    return json.loads(text) # turn the json string into a python dictionary

# opens db.json, turns the python dictionary into json, and saves it to the file
def save_database(data):
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)



# request/response cycle 1
# 1. user goes to http://localhost:5000/ and sends a GET request, which goes to the 'index' view
# 2. the server responds with the rendered template containing the form

# request/response cycle 2
# 3. the user submits the form, which goes to the 'submit_form'
# 4. the server responds with an instruction to redirect to the 'index' view

# request/response cycle 3 - the same as request/response cycle 1


# by default views can only receive GET requests
# @app.route('/', methods=['GET'])
@app.route('/')
def index():
    data = load_database()
    return render_template('index.html', value=data['value'], fav_nums=data['fav_nums'])


@app.route('/submit_form', methods=['POST'])
def submit_form():
    # load the database
    data = load_database()
    
    # get the data out of the form
    print(request.form) # ImmutableMultiDict([('inc_or_dec', 'increment')])
    inc_or_dec = request.form['inc_or_dec']
    print(inc_or_dec) # increment

    # modify the data from the database
    if inc_or_dec == 'increment':
        data['value'] += 1
    else:
        data['value'] -= 1

    # save the data to the database
    save_database(data)

    # redirect the user back to the home page
    # return 'you are at the submit form view'
    return redirect('/')


@app.route('/save_number', methods=['POST'])
def save_number():
    mynumber = request.form['mynumber']
    mynumber = int(mynumber) # the value form the form is a string by default
    data = load_database()
    data['fav_nums'].append(mynumber)
    data['fav_nums'].sort()
    save_database(data)

    return redirect('/')

