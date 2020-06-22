from flask import Flask, request, render_template
import random
import string
import math


app = Flask(__name__)


# path to the view index
@app.route('/', methods=["GET", "POST"])
# defines our data; manipulates


def index():
    

    # master_pool = []
    master_pool = ''
    output = ''


    if request.method == "POST":

        num_select_uppers = int(request.form['num_select_uppers'])
        num_select_lowers = int(request.form['num_select_lowers'])
        num_select_chars = int(request.form['num_select_chars'])
        num_select_nums = int(request.form['num_select_nums'])

        uppers = string.ascii_uppercase
        lowers = string.ascii_lowercase
        numbers = '0123456789'
        specials = '!@#$%^&*()_+[]|:;",.<>?/'


        # password is the sum of all user inputs; it is the total number of characters in the password
        password_length = num_select_uppers + num_select_lowers + num_select_chars + num_select_nums

        # while i is less than the users input
        i = 0
        while i < num_select_uppers:
            # for each iteration a random letter from uppers is added to a master pool
            master_pool += random.choice(uppers)
            # master_pool.append(random.choice(uppers))
            # increment i
            i += 1
        
        j = 0
        while j < num_select_lowers:
            # repeat the same process for lowers
            master_pool += random.choice(lowers)
            # master_pool.append(random.choice(lowers))
            j += 1
        
        y = 0
        while y < num_select_chars:
            # repeat the same process for numbers
            master_pool += random.choice(numbers)
            # master_pool.append(random.choice(numbers))
            y += 1

        x = 0
        while x < num_select_nums:
            # repeat the same process for special characters
            master_pool += random.choice(specials)
            # master_pool.append(random.choice(specials))
            x += 1
        
        z = 0 
        while z <= password_length:
            # for each iteration a
            output += random.choice(master_pool)
            z += 1


    return render_template('index.html', password = output )


