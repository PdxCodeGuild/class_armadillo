from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    units_dict = {
    "ft" : 0.3048,
    "mi" :1609.34,
    "m" : 1,          
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
    }
    print(request.form)
    if request.method == 'POST':
        user_input = request.form['user_input']
        user_input = float(user_input)
        units = request.form['start_units']
        end_units = request.form['end_units']
        
        conversion_meters = user_input * units_dict[units]
        final_conversion = round(conversion_meters / units_dict[end_units],3)
        result = f'{user_input} {units} equals {final_conversion} {end_units}'
    else: 
        print(request.form)    
        result = ''
    return render_template('index.html', result=result)
   




