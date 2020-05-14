from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    output = ""
    meter_output = ""
    if request.method == 'POST':
        user_unit = request.form['user_unit']
        user_distance = int(request.form['user_distance'])
        if user_unit == "mi" or user_unit == "mile":
            output = (user_distance * 1609.34)
        elif user_unit == 'ft' or user_unit == 'feet':
            output = (user_distance * 0.3048)
        elif user_unit == 'km' or user_unit == 'kilometer':
            output = (user_distance * 1000)
        elif user_unit == 'm' or user_unit == 'meter':
            output = (user_distance * 1)
        elif user_unit == 'yd' or user_unit == 'yard':
            output = (user_distance * 0.9144)
        elif user_unit == 'in' or user_unit == 'inch':
            output = (user_distance * 0.0254)
    

    return render_template('index.html', result = output)
