import json
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def load_database():
    with open('db.json', 'r') as file:
        tasks = json.loads(file.read())
    return render_template("index.html", tasks=tasks["todos"])

# # saving and loading the database
# def save_database(data):
#     with open('database.json', 'w') as file:
#         file.write(json.dumps(data))

# def load_database():
#     with open('database.json', 'r') as file:
#         data = json.loads(file.read())
#     return data

# opens db.json, reads the text, turns the json into a python dictionary

# opens db.json, turns the python dictionary into json, and saves it to the file
def save_database(data):
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data) # turn the python dictionary into a json string
        file.write(text)


@app.route('/save_task', methods=['POST'])
def save_task():
    mynumber = request.form['mynumber']
    mynumber = int(mynumber) # the value form the form is a string by default
    data = load_database()
    data['fav_nums'].append(mynumber)
    data['fav_nums'].sort()
    save_database(data)

    return redirect('/')
