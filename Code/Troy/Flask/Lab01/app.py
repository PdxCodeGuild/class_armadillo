


from flask import Flask, request, render_template
app = Flask(__name__)
import string
import random

@app.route('/', methods=["GET", "POST"])
def index():
    output = []
    if request.method == "POST":
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password_length = int(request.form["password_length"])
        # uppercase = [ABCDEFGHIJKLMNOPQRSTUVWXYZ]
        # lowercase = [abcdefghijklmnopqrstuvwxyz]
        for i in range(password_length):
            output += random.choice(alphabet)


    print(request.form)
    message = ''

    return render_template('index.html', password= output)
