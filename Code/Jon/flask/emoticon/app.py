from flask import Flask, render_template, request 
app = Flask(__name__)

import random

# EXAMPLE
@app.route('/', methods=['GET', 'POST'])
def hello_world():

    if request.method == 'POST':
        user_input = request.form['user_input']

        eyes = ['8', '0', ':']
        nose = ['D', '>', '.']
        mouth = [')', 'D', ']']
        for i in range(user_input):
            
        context = {
            'faces': faces
        }

    else:
        context = {

        }

    return render_template('index.html', context=context)

