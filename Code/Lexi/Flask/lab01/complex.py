import string, random
# Complex version: the user enters the number of uppercase letters, lowercase letters, numbers, and special characters

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    output = ""
    if request.method == 'POST':

        upper = int(request.form["upper"])
        lower = int(request.form["lower"])
        punct = int(request.form["punct"])
        digit = int(request.form["digit"])


        for i in range(upper):
            output += random.choice(string.ascii_uppercase)
        for i in range(lower):
            output += random.choice(string.ascii_lowercase)
        for i in range(punct):
            output += random.choice(string.punctuation)
        for i in range(digit):
            output += random.choice(string.digits)


    print(output)

    return render_template('index.html', password = output)