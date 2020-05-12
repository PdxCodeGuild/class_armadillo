


from flask import Flask, request, render_template
app = Flask(__name__)
import string
import random

@app.route('/', methods=["GET", "POST"])
def index():
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    # print('Please make a password.  It should be 10 characters long. ')

    # input('I will make a password using random choices. Press enter to get your password... ')

    # for i in range(10):
    #     print(random.choice(alphabet), end= '')

    print(request.form)
    message = ''

    return render_template('index.html')
