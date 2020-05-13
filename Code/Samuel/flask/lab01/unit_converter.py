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
def index():
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