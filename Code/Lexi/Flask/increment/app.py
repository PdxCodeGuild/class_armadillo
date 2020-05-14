from flask import Flask, render_template, request
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







@app.route('/', methods=['GET', 'POST'])
def index():

    #json.loads turns a string of JSON into a dictionary
    # data = json.loads({"name" : "joe", "age" : 456})
    # print(data)
    # print(data['name']) #joe
    # data['name'] = 'jane'
    # # json.dumps turns
    # json_string = json.dumps(data)

    # data = load_database()
    # print(data)
    # data['value'] += 1
    # save_database(data)

    data = load_database()
    if request.method =='POST':
        print(request.form) #immutableMultiDict
        inc_or_dec = request.form['inc_or_dec'] # increment
        print(inc_or_dec)
        if inc_or_dec == 'increment':
            data['value'] += 1
        else:
            data['value'] -= 1
            save_database(data)


    return render_template('index.html' , value=data['value'], fruits=data['fruits'])