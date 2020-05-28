#LAB 01- **random password generator**
#   - Simple version: the user just enters in the number of characters in the password

from flask import Flask, request, render_template
from string import ascii_lowercase, punctuation, digits
import string
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        user_value = request.form['number']
        i = 0
        keep_it_going = True
        possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password_length = int(user_value)

        rando = []
        while i in range(password_length):
            rando.append(random.choice(possible_chars))
            i += 1
            rando_string = ''.join(rando)    
            output = rando_string
     
    else:
        output = ''

    message = ''

    return render_template('index.html', output=output)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     output = ""
#     if request.method == 'POST':
#         alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
#         password_length = int(request.form["password_length"])

#         for i in range(password_length):
#             output += random.choice(alphabet)

#     print(request.form)
   

#     return render_template('index.html', password = output)