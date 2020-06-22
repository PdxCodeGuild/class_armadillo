from flask import Flask, render_template, request
import json

def load_database():
    with open('db.json', 'r') as file:
        text = file.read()
    return json.loads(text)


def save_database(data):
    with open('db.json', 'r') as file:
        text = json.dumps(data, indent=4)
        file.write(text)


@app.route('/', methods=['GET', 'POST'])
def index():
    