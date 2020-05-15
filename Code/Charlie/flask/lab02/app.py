import json
from flask import Flask, render_template, request

app = Flask(__name__)

# saving and loading the database
def load_database():
    with open('data.json', 'r') as file: # open the file
        text = file.read() # read the text
    return json.loads(text)

def save_database(data):
    with open('data.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)



@app.route('/')
def index():
    data = load_database()
    return render_template('index.html', value=data)


@app.route('/submit_form', methods=['POST'])
def submit_form():
    # load the database
    data = load_database()
    
    # get the data out of the form
    print(request.form) # 


    # save the data to the database
    save_database(data)

    # redirect the user back to the home page
    # return 'you are at the submit form view'
    return data



@app.route('/save_to_do', methods=['POST'])
def save_number():
    mytodo = request.form['mytodo']
    data = load_database()
    data['saved'].append(mytodo)
    data['saved'].sort()
    save_database(data)

    return data