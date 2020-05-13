from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    units_dict = {
    "ft" : 0.3048,
    "mi" :1609.34,
    "m" : 1,            #various unit's equivalent to 1 meter
    "km" : 1000,
    "yd" : 0.9144,
    "in" : 0.0254
    }
    print(request.form)
    if request.method == 'POST':
        user_input = request.form['user_input']
        units = request.form['units']
        user_input = float(user_input)
        conversion = round(user_input * units_dict[units],3)
        result = f'{user_input} {units} equals {conversion}'
    else: 
        print(request.form)    
        result = ''
    return render_template('index.html', units=units, result=result)




    
    
    
