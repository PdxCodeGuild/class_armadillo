from flask import Flask, request, render_template
import random
import string
import math


app = Flask(__name__)


# path to the view index
@app.route('/', methods=["GET", "POST"])
# defines our data; manipulates


def index():
    

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
        # numbers = ['0','1','2','3','4','5','6','7','8','9']
        specials = '!@#$%^&*()_+[]|:;",.<>?/'
        # specials = ['!','@','#','$','%','^','&','*','(',')','-','=','+','{','}','|',':',';','?','<','>']
        password_length = num_select_uppers + num_select_lowers + num_select_chars + num_select_nums


        i = 0
        while i < num_select_uppers:
            master_pool += random.choice(uppers)
            i += 1
        
        j = 0
        while j < num_select_lowers:
            master_pool += random.choice(lowers)
            j += 1
        
        y = 0
        while y < num_select_chars:
            master_pool += random.choice(numbers)
            y += 1

        x = 0
        while x < num_select_nums:
            master_pool += random.choice(specials)
            x += 1

        z = 0
        while z <= password_length:
            output += random.choice(master_pool)
            z += 1

    return render_template('index.html', password = output )




