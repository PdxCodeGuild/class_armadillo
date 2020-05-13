
# john helped with lab
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

        pass_lenght = []
        while i in range(password):
            pass_lenght.append(random.choice(alphabet))
            i += 1
            user_input = ''.join(pass_lenght)
            output = user_input

    else:
        output = ''
    
    return render_template('index.html', output=output)
