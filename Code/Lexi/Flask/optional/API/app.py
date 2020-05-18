import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('weather.html')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:test123@localhost/flaskmovie'
# db= SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         super().__init__()
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username


# # Version 1: display text/graphics from the API.
# # Version 2: allow the user to search the API.
# # Version 3: allow the user to save "favorites" to a db.json database.
# def load_database():
#     with open('r'):


@app.route('/')
def index():
    return "<h1 style='color:red'>hello Flask</h1>"

if __name__ == "__main__":
    app.run()

# @app.route('/submit_form', methods=['POST'])
# def submit_form():
#     pass
#     data = load_database()

# @app.route('/favorite', methods=['POST'])
# def favorite():
#     pass


# resources:

# checkin increment-multi/db_demo.py

import config

from twython import Twython, TwythonError

# create a Twython object by passing the necessary secret passwords
twitter = Twython(config.api_key, config.api_secret, config.access_token, config.token_secret)
