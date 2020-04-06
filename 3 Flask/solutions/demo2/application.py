
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature/', methods=['POST'])
def temperature():
    print(request.form)
    # write it to the database
    return redirect('/')


@app.route('/clothing/', methods=['POST'])
def clothing():
    print(request.form)
    return render_template('index.html')

