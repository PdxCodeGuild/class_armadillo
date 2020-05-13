
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
        password_num = int(user_number)

        pass_length = []
        while i in range(password_num):
            pass_length.append(random.choice(alphabet))
            i += 1
            user_input = ''.join(pass_length)
            output = user_input

    else:
        output = ''
    
    return render_template('index.html', output=output)
