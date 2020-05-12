


from flask import Flask, request, render_template
app = Flask(__name__)
import string
import random

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        print(request.form["password_length"])

        output = ""
        
        for i in range(10):
            output += random.choice(alphabet)


    print(request.form)
    message = ''

    return render_template('index.html', password="Hello")
