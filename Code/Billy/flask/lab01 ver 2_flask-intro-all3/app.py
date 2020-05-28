from flask import Flask, render_template, request
import string
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def password():
    output = ''
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
    output = ''.join(password)  # convert the list of characters back into a string   

    return render_template('password.html', output=output)


@app.route('/', methods=['POST'])
def converter():
    conv_rate = {"ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, "yd": .9144, "in": .0254} # conv rate dictionary

    user_dist = float(request.form['distance'])   
    user_unit_orig = request.form['units_1'].lower # user input
    distance_meters = user_dist * (conv_rate.get(f"{user_unit_orig}"))
    
    user_unit_desired = request.form['units_2'].lower # user input
    distance_new = distance_meters / (conv_rate.get(f"{user_unit_desired}"))

    output = f"{user_dist} {user_unit_orig} equals {distance_new} {user_unit_desired}" # results                      

    return render_template('coverter.html', output=output)


@app.route('/', methods=['POST'])
def rot():
    output = '' # makes empty output list
    text = request.form['rot_text']
    num = request.form['rot_num']
    for x in text: # iterates through input one character(chr)(char) at a time
        ascii_code = ord(x) # changes char to ascii
        if 97 <= ascii_code <= 122: # lower case
            ascii_code -= 97 # starts sequence at 0
            output += chr((ascii_code + num)%26 + 97) 
            # rotates, shifts, changes ascii to chr, adds to ouput variable 
        elif 65 <= ascii_code <= 90: # upper case
            ascii_code -= 65
            output += chr((ascii_code + num)%26 + 65)
        elif 32 <= ascii_code <= 64 or 91 <= ascii_code <= 96 or 123 <= ascii_code <= 126: 
            # space, numbers, special char groups (ascii special char are separated into four groups)
            output += chr(ascii_code) # no rotation required for these characters 
        else:
            # output += chr(ascii_code)
            output = f'Invalid character(s)...cannot encrypt that entry.' # input validation  

    return render_template('rot.html', output=output)

