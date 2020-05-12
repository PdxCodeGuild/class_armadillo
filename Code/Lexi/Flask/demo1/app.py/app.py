from flask import flask
app = Flask(_name_)

@app.route('/') # decorator
def index():    # local home directory is typically 'index'
    return 'Hello World!'

@app.route('/')
def about():
    return 'Hello World!'