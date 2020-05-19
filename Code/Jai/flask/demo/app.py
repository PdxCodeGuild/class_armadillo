from flask import Flask 
app = Flask(__name__)


#localhost:5000
@app.route("/")# decorator - path to the view 
def index():
    return "hello world"

@app.route()