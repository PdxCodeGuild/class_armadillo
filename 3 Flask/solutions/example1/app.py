from flask import Flask, render_template, request

app = Flask(__name__)


def add(a, b):
    return a + b

@app.route('/')
def index():
    total = add(5, 2)
    return 'you are at the index page ' + str(total)

@app.route('/example1/')
def example1():
    html = '<ul>'
    for i in range(10, 100):
        html += f'<li>{i}</li>'
    html += '</ul>'
    return html

@app.route('/example2/')
def example2():
    return render_template('example2.html')

@app.route('/example3/')
def example3():
    name = 'bill'
    temperature = 100
    return render_template('example3.html', name=name, temperature=temperature, text_color="green")

@app.route('/example4/<int:temperature>/')
def example4(temperature):
    return render_template('example4.html', temperature=temperature)


@app.route('/example5/')
def example5():
    nums = list(range(0, 100))
    return render_template('example5.html', nums=nums)


@app.route('/example6/')
def example6():
    contacts = [{
        'name': 'jim',
        'age': 23,
        'email': 'jim@jim.org',
        'fav_color': 'red'
    },{
        'name': 'jill',
        'age': 234,
        'email': 'jim@jim.org',
        'fav_color': 'blue'
    },{
        'name': 'jane',
        'age': 2345,
        'email': 'jim@jim.org',
        'fav_color': 'green'
    }]
    return render_template('example6.html', contacts=contacts)


@app.route('/example7/', methods=['GET', 'POST'])
def example7():
    response = ''
    temperature = ''
    if request.method == 'POST':
        temperature = request.form['temperature']
        temperature = int(temperature)
        if temperature < 50:
            response = 'cold'
        elif temperature < 80:
            response = 'warm'
        else:
            response = 'hot'
    return render_template('example7.html', temperature=temperature, response=response)


@app.route('/example8/', methods=['GET', 'POST'])
def example8():
    if request.method == 'POST':
        print(request.form)
        mypassword = request.form['mypassword']
        mycheckbox1 = 'mycheckbox1' in response.form

    return render_template('example8.html')





