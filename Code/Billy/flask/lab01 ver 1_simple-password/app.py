from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = '' # empty string for establishing word
    length = '' 
    if request.method == 'POST':

        all_characters = string.ascii_letters + string.digits + string.punctuation 

        length = int(request.form['length'])

        for _ in range(length): # user input for password length
            password += random.choice(all_characters) # builds word

        # random.shuffle can't accept string arguments, must convert to list
        password = list(password) # convert string into a list of characters
        random.shuffle(password) # shuffle the list of characters
        password = ''.join(password) # convert the list of characters back into a string

    return render_template('index.html', password=password)

