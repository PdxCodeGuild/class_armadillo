from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index(): # django's view
    if request.method == 'POST':

        animal = request.form['animal']
        texture = request.form['texture']
        noun = request.form['noun']
        madlib = f'Suzy had a little {animal} that was {texture} covered in {noun}'
        context = {
            'madlib': madlib
        }
        # return render_template('index.html', context=context)
    else:
        context = {

        }
    return render_template('index.html', context=context)
