

from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/password', methods=["GET", "POST"])
def password():
    if request.method == "POST":
        user_number = request.form['number']
        i = 0
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = int(user_number)

        rando = []
        while i in range(password):
            rando.append(random.choice(alphabet))
            i += 1
            rando_string = ''.join(rando)
            output = rando_string

    else:
        output = ''
    
    return render_template('index.html', output=output)
