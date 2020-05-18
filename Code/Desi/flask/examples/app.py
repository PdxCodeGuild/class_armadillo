from flask import Flask, request, render_template
app = Flask(__name__)
import string
import random

@app.route ('/', methods=["GET", "POST"])
def hello_word():
    return "Hello World!"

