from flask import Flask, request, render_template
app = Flask(__name__)
import string
import random


# flask app for requests
@app.route ('/', methods=["GET", "POST"])
# defines the view
def index():
    output = ''
    if request.method == "POST":
        # assigns variable and output for uppercase, lowercase, numbers, and special characters.
        uppercase = int(request.form['uppercase'])
        for i in range(uppercase):
            output += random.choice(string.ascii_uppercase)

        lowercase = int(request.form['lowercase'])
        for i in range(lowercase):
            output +=random.choice(string.ascii_lowercase)

        numbers = int(request.form['numbers'])
        for i in range(numbers):
             output += random.choice(string.digits)

        characters = int(request.form['characters'])
        for i in range(characters):
            output += random.choice(string.punctuation)
        # converts string into list and shuffles the ouput
        output = list(output)
        random.shuffle(output)
        # converts list back to string
        output = ''.join(output)   
    


        print(request.form)
    return render_template("Lab01-pswd_gen.html", password=password)