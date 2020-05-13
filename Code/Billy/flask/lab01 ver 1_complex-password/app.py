from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = '' # empty string for establishing word
    if request.method == 'POST':

        # all_characters = string.ascii_letters + string.digits + string.punctuation 

        # length = int(request.form['length'])

        # for _ in range(length): # user input for password length
        #     password += random.choice(all_characters) # builds word

        # # random.shuffle can't accept string arguments, must convert to list
        # password = list(password) # convert string into a list of characters
        # random.shuffle(password) # shuffle the list of characters
        # password = ''.join(password) # convert the list of characters back into a string

        # ascii letters, digits, special char
        upper = int(request.form['upper'])
        lower = int(request.form['lower'])
        number = int(request.form['number'])
        character = int(request.form['character'])

        for _ in range(upper): # uses input parameters to build password
            password += random.choice(string.ascii_uppercase)

        for _ in range(lower):
            password += random.choice(string.ascii_lowercase)

        for _ in range(number):
            password += random.choice(string.digits)

        for _ in range(character):
            password += random.choice(string.punctuation)
        
        # random.shuffle can't accept string arguments, must convert to list
        password = list(password)     # convert string into a list of characters
        random.shuffle(password)  # shuffle the list of characters
        password = ''.join(password)  # convert the list of characters back into a string    

    return render_template('index.html', password=password)

