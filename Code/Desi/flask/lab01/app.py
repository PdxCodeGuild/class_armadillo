from flask import Flask, request, render_template
app = Flask(__name__)
import string
import random

@app.route ('/', methods=["GET", "POST"])
def hello_world():
    return 'Hello World!'