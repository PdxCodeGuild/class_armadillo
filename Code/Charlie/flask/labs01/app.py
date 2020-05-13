from flask import Flask, render_template, request
import random
import string
from string import ascii_lowercase


app = Flask(__name__)

@app.route('/random', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        user_value = request.form['number']
        i = 0
        
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        
        length_of_password = input("enter the length of password you want: ")
        length_of_password = int(user_value)

        while not characters.isdigit():

            output = "You must enter a number: "
        else:
            characters = int(characters)

        password = []
        while i in range(length_of_password):
            password.append(random.choice(characters))
            i += 1
            password_string = ''.join(password)
            output = password_string
    else:
        output = ''
    


    return render_template('index.html', output=output)