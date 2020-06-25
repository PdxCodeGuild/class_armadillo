from flask import Flask, render_template, request
import json

app = Flask('increment_app')


# JSON can only contain
# null (None in Python), booleans, ints, floats, strings, arrays (list in python), objects (dictionary in python)


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


# if we used classes
# db = Database()
# db.load()
# db.save()

@app.route('/', methods=['GET', 'POST'])
def index():

    # # json.loads turns a string of json into a dictionary
    # data = json.loads('{"name":"joe","age":456}')
    # print(data)
    # print(data['name']) # joe
    # data['name'] = 'jane'
    # # json.dumps turns a dictionary into a string of json
    # json_string = json.dumps(data)
    # print(json_string)


    # data = load_database()
    # print(data)
    # data['value'] += 1
    # save_database(data)

    # load data from the database
    data = load_database()
    if request.method == 'POST':

        # get form data
        # print(request.form) # ImmutableMultiDict([('inc_or_dec', 'increment')])
        inc_or_dec = request.form['inc_or_dec']
        # print(inc_or_dec) # increment

        # modify the data from the database using our form data
        if inc_or_dec == 'increment':
            data['value'] += 1
        else:
            data['value'] -= 1

        # saving our data back to the database
        save_database(data)
    
    return render_template('index.html', value=data['value'], fruits=data['fruits'])
