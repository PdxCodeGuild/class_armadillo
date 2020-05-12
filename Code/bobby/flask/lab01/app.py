from flask import Flask, render_template, request
app = Flask (__name__)
import string
import random
import time

@app.route('/', methods = ['Get', 'Post'])
def index():


    print(request.form)
    message = ''

# The for loop is the part of the progeram that takes what the user entered and generates the Random Pass word.
    # input= password_length = 'How Many Charecters Would You Like?:'

    if request.method == 'Post':
        letters = string.ascii_letters + string.punctuation + string.digits
        password_lenght = request.form['How many charecters Would You Like? ']
    
    else:
        password = ''

    # for letter in range (0, password_length):
    #  password += random.choice(letters)

# This is what the generated password
    return render_template('index.html', result=password)