from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    character_password = str()
    message = ''
    if request.method == 'POST':
        upper = "upper" in request.form
        lower = "lower" in request.form
        digit = "digit" in request.form
        symbol = "symbol" in request.form
        number_of_characters = request.form['number_of_characters']
        if not number_of_characters.isnumeric():
            message = "Please enter a whole number greater than 0."
        elif int(number_of_characters) <= 0:
            message = "Please enter a whole number greater than 0."
        else:
            print(upper)
            print(lower)
            print(digit)
            print(symbol)
            print(number_of_characters)
            character_counter = 0
            character_types = str()
            character_password = str()
            
            if upper:
                character_types += string.ascii_uppercase
            if lower:
                character_types += string.ascii_lowercase
            if digit:
                character_types += string.digits
            if symbol:
                character_types += string.punctuation

            for i in range(int(number_of_characters)):
                character_password += random.choice(character_types)
            
            print(character_password)
    else:
        character_password = str()
    return render_template("password_generator.html", result=character_password, message=message)