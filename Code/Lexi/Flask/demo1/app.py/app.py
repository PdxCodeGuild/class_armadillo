from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # decorator
def index():    # local home directory is typically 'index'
    # html = '<html><head></head></body>'
    # html += '<ul>'
    # for i in range(100):
    #     html += f'<li>{i}</li>'
    #     html+= '</ul>'
    #     html += '</body></html>'
    #     print(html)
    #     return html

name = 'bob'
return render_template('index.html', name='bob')

@app.route('/about') # this is called a 'view'
def about():
    return 'Welcome to the about page'