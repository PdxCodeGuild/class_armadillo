from flask import Flask, render_template, request
import json

app = flask('increment_app')


def load_db():
    with open('db.son', 'r') as file: # open the file
        text = file.read() # read the text
    return json.loads(text) # turn the json string into a python dictionary


def save_db(data):
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)


@app.route('/', methods=['GET', 'POST'])

def index():
    data = load_db()
    print(data)
    return render_template("index.html", title= "todo list", todos=data)

@app.route('/newtask', methods=['POST'])
def savetask():
    print(request.form[
    ])
    if request.method =='POST':



