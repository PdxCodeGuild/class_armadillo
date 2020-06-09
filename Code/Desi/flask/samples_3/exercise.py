from flask import flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the home page'

@app.route('/about')
def about():
    return "weclome to the about page"

    