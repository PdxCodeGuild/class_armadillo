

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    animal = 'armadillo'
    texture = 'scales'
    noun = 'dirt'
    madlib = f"Suzy had a little {animal}, its {texture} was white as {noun}"

    return render_template('index.html', result=madlib)





