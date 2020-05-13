from flask import Flask, render_template, request
app = Flask(__name__)

import py.rot13 as rotn

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
    return render_template('unit-converter.html')