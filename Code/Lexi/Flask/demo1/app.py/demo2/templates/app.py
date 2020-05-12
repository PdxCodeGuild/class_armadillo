from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
   
   # passing KWARGS below
   return render_template('index.html', result="testing result")

