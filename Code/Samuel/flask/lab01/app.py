from flask import Flask, render_template, request
import random
import string
app = Flask(__name__)

def check_if_numeric(str1):
    for char in str1:
        if not char.isnumeric():
            if char != "-":
                return False
    return True

@app.route("/", methods=['GET', 'POST'])
def index_start():
    return render_template("index.html")

@app.route("/rot13", methods=['GET', 'POST'])
def rot13():
    message = ''
    scrambled_word = ""
    if request.method == 'POST':
        rotation = request.form['rotation']
        transform = request.form['transform']
        if not check_if_numeric(rotation):
            message = "Please enter in a whole number either positive, negative, or zero."
        else:
            alphabet_upper = string.ascii_uppercase
            alphabet_lower = string.ascii_lowercase
            digits = string.digits
            punctuation = string.punctuation

            rot_alphabet_upper = str()
            rot_alphabet_lower = str()
            rot_digits = str()
            rot_punctuation = str()

            rotation = int(rotation)
            if rotation > 0:
                rot_alphabet_upper = alphabet_upper[rotation:] + alphabet_upper[:rotation-len(alphabet_upper)]
                rot_alphabet_lower = alphabet_lower[rotation:] + alphabet_lower[:rotation-len(alphabet_lower)]
                rot_digits = digits[rotation:] + digits[:rotation-len(digits)]
                rot_punctuation = punctuation[rotation:] + punctuation[:rotation-len(punctuation)]
            elif rotation < 0:
                rot_alphabet_upper = alphabet_upper[rotation:] + alphabet_upper[:rotation+len(alphabet_upper)]
                rot_alphabet_lower = alphabet_lower[rotation:] + alphabet_lower[:rotation+len(alphabet_lower)]
                rot_digits = digits[rotation:] + digits[:rotation+len(digits)]
                rot_punctuation = punctuation[rotation:] + punctuation[:rotation+len(punctuation)]
            else:
                rot_alphabet_upper = alphabet_upper
                rot_alphabet_lower = alphabet_lower
                rot_digits = digits
                rot_punctuation = punctuation

            for i in range(len(transform)):
                if alphabet_upper.find(transform[i]) > -1:
                    scrambled_word += rot_alphabet_upper[alphabet_upper.find(transform[i])]
                elif alphabet_lower.find(transform[i]) > -1:
                    scrambled_word += rot_alphabet_lower[alphabet_lower.find(transform[i])]
                elif digits.find(transform[i]) > -1:
                    scrambled_word += rot_digits[digits.find(transform[i])]
                elif punctuation.find(transform[i]) > -1:
                    scrambled_word += rot_punctuation[punctuation.find(transform[i])]
                else:
                    scrambled_word += transform[i]
    else:
        scrambled_word = str()
    return render_template("rot13.html", result=scrambled_word, message=message)

@app.route("/unit_converter", methods=['GET', 'POST'])
def unitconversions():
    unit_conversions = {
        "Feet": [0.3048],
        "Miles": [1609.34],
        "Meters": [1],
        "Kilometers": [1000],
        "Yards": [0.9144],
        "Inches": [0.0254]
    }
    input_units = str()
    output_units = str()
    measurement = str()
    message = str()
    converted_units = str()
    if request.method == 'POST':
        input_units = request.form['input_units']
        output_units = request.form['output_units']
        measurement = request.form['measurement']
        if not measurement.isnumeric():
            message = "Please enter a whole number greater than 0."
        elif int(measurement) <= 0:
            message = "Please enter a whole number greater than 0."
        else:
            converted_units = round((float((unit_conversions[input_units][0] * int(measurement))/ unit_conversions[output_units][0])), 2)
    
    return render_template("unit_converter.html", result=converted_units, message=message, input_units=input_units, output_units=output_units, measurement=measurement)

@app.route("/password_generator", methods=['GET', 'POST'])
def passwordgenerator():
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