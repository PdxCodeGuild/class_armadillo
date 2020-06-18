from flask import Flask, request, render_template
import random
import string


app = Flask(__name__)

# path to the view
@app.route('/', methods=["GET", "POST"])
# defines our data
def index():

    output = ''

    if request.method == "POST":

        pw_length = int(request.form['num_select'])

        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

        i = 0

        while i < pw_length:
            output += random.choice(alphabet)
            i += 1
        
    # else:???


    return render_template('index.html', password = output)