

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(): # view

    print(request.form)
    message = ''
    if request.method == 'POST': # we received a form submission

        # the keys of the dictionary request.form
        # are the *name* attributes of the input fields inside the form
        animal = request.form['animal']
        texture = request.form['texture']
        noun = request.form['noun']
        if noun.isdigit(): # if the user entered a number for the noun
            message = 'noun cannot be a number'
            madlib = ''
        else:
            madlib = f"Suzy had a little {animal}, its {texture} was white as {noun}"
    else: # we received a get request
        madlib = ''
    animals = ['armadillo', 'sloth', 'baby elephant', 'honeybadger', 'llama', 'raven']
    animals.sort()
    return render_template('index.html', result=madlib, animals=animals, message=message)





