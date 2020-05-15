from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_database():
    with open('db.json', 'r') as file:
        text = file.read()
    return json.loads(text)

def save_database(data):
    with open('db.json', 'w') as file:
        # This saves the 'data' to the file and json.dumps turns it back to json
        file.write(json.dumps(data, indent=4))

@app.route('/', methods=['GET', 'POST'])
def index():
    data = load_database()
    print(data)
    # print(data)
    # data['value'] += 1
    # save_database(data)
    if request.method == 'POST':
        inc_or_dec = request.form['inc_or_dec']
        if inc_or_dec == 'inc':
            data['value'] += 1
        else:
            data['value'] -= 1

        save_database(data)
        context = {
            "data": data
        }
    else:
        context = {
            "data": data
        }
    

    return render_template('index.html', context=context)
    # return redirect('/') if it were only post