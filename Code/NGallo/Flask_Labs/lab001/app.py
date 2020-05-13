from flask import Flask, render_template, request
from string import ascii_lowercase
import string
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    dict_of_distances = {'in':0.0254, 'ft':0.3048, 'ya':0.9144, 'm':1, 'mi':1609.34, 'k':1000}

    if request.method == 'POST':
        
        first_distance = request.form['first_distance']
        first_distance = round(first_distance)
        units = request.form['units']
        end_units = request.form['second_units']


        distance_meters = first_distance * dict_of_distances[units]

        distance_output = distance_meters / dict_of_distances[end_units]

        output = f"You are converting {first_distance}{units} to {end_units} and the answer is {distance_output} {end_units}."
    else:
        output = ''

    message = ''

    return render_template('index.html', output=output)

@app.route('/rot13', methods=['GET', 'POST'])
def rot13():

    if request.method == 'POST':
        user_input = str(request.form['word'])
        user_value = int(request.form['number'])
        list_userinput = []
        # going into ascii list and finding index of the letter
        for letter in user_input:
            list_userinput.append(ascii_lowercase.index(letter))
        # rotates the index in the list
        new_index = [i + user_value for i in list_userinput]
    
        # starts the index over once you hit the end of the list
        rotated_index = [i%26 for i in new_index]

        # appends to final list the ascii string
        final_list = []
        for i in rotated_index:
            final_list.append(ascii_lowercase[i])

        # takes chars out of list and creates a string
        output = "".join(final_list)
     
    else:
        output = ''

    message = ''

    return render_template('rot13.html', output=output)


@app.route('/random', methods=['GET', 'POST'])
def randompasswordgen():

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

    return render_template('random.html', output=output)