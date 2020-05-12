from flask import flask
app = Flask(_name_)

@app.route('/') # decorator
def index():    # local home directory is typically 'index'
    html = <html><head><head><body>'
    html += '<ul>'
    for i in range(100):
        html += f'<li>{i}</li>'
        html+= '</ul>'
        html += '</body></html>'
        print(html)

@app.route('/about')
def about():
    return 'Welcome to the about page'