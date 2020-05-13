from flask import Flask, render_template, request
app = Flask (__name__)
import string
import random
import time

@app.route('/', methods = ['GET', 'POST'])
def index():
    password = ""


    
    if request.method == 'POST':
        # I am using letters is my string name to pull up the information within the moduals.
        # Password is my string name used in my for loop to call on the random modual to generate the password
        letters = string.ascii_letters + string.punctuation + string.digits
        password = ""
        # This section is where the program askes the user to input how long they would like their password to be.
        password_length = int (request.form["password_length"])
        # The for loop is the part of the progeram that takes what the user entered and generates the Random Pass word.
        for letter in range(0, password_length):
            password += random.choice(letters)
        print(request.form)
        
    return render_template('index.html', result=password)
