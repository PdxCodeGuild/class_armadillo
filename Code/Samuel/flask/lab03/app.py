from flask import Flask, render_template, request, redirect
import json
import requests
from secrets import authorization

app = Flask(__name__)

@app.route("/")
def index_start():
    address = "https://favqs.com/api/qotd"
    response = requests.get(address, headers = authorization).text
    data = json.loads(response)
    return render_template("index.html", message = data)