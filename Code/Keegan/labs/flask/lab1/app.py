from flask import Flask, render_template, request
app = Flask(__name__)

import py.rot13 as rotn
import py.unit_converter as uc

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rotate', methods=['GET', 'POST'])
def rotate():
    if request.method == 'POST':
        user_string = request.form['user_string'].strip()
        r_factor = request.form['r_factor']

        if user_string != '' and r_factor != '':
            rotated_string = rotn.rotate_string(user_string, r_factor)
            
            context = {
                'user_string'   : user_string,
                'r_factor'      : r_factor,
                'rotated_string': rotated_string
            }
        else:
            error = 'Fields cannot be blank!'
            return render_template('rotate-string.html', error=error)

        return render_template('rotate-string.html', context=context)

    # return plain template if method is GET
    return render_template('rotate-string.html')

@app.route('/unit-converter', methods=['GET', 'POST'])
def unit_converter():
    context = {
        'units': uc.UNIT_OPTIONS,
    }
    if request.method == 'POST':
        distance = request.form['distance']
        unit_in = request.form['unit-in']
        unit_out = request.form['unit-out']

        error = ''
        if distance == '':
            error = 'Distance cannot be blank!'
        elif not uc.is_float(distance):
            error = 'Distance must contain only numbers.'

        if error:
            return render_template('unit-converter.html', context=context, error=error)

        result = uc.convert_unit(float(distance), unit_in, unit_out)    
        
        context['distance'] = distance
        context['unit_in'] = unit_in
        context['unit_out'] = unit_out
        context['result'] = result

    return render_template('unit-converter.html', context=context)