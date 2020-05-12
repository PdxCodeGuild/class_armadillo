from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/' methods=['GET', 'POST']) # decorator
def index():    # local home directory is typically 'index'
    # html = '<html><head></head></body>'
    # html += '<ul>'
    # for i in range(100):
    #     html += f'<li>{i}</li>'
    #     html+= '</ul>'
    #     html += '</body></html>'
    #     print(html)
    #     return html

    if request.method == 'POST':
        print(request.form['user_name'])
        print(request.form['birthday'])



    temperature = 65
    nums = [1, 2, 3]

    return render_template('index.html', name='bob', temperature=temperature, nums=nums)

@app.route('/about') # this is called a 'view'
def about():
    return 'Welcome to the about page'