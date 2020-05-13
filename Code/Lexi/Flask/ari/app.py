from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

    @app.route('/about/')
def llama():
    return 'You are a llama'