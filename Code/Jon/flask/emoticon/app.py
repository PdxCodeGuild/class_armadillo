from flask import Flask, render_template, request 
app = Flask(__name__)

import random

# EXAMPLE
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        user_input = int(user_input)
        faces = []
        eyes = ['8', '0', ':']
        noses = ['D', '>', '.']
        mouths = [')', 'D', ']']

        for i in range(user_input):
            eye = random.choice(eyes)
            nose = random.choice(noses)
            mouth = random.choice(mouths)
            face = f'{eye}{nose}{mouth}'
            faces.append(face)
        print(faces)
        context = {
            'faces': faces
        }
    else:
        context = {

        }

    return render_template('index.html', context=context)

