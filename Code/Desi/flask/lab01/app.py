from flask import Flask, request, render_template
app = Flask(__name__)
import string
import random

@app.route ('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route ('/password_gen', methods=["GET", "POST"])
def generator():
    password=""
    return render_template("Lab01-pswd_gen.html", password=password)