from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        print('index view - post')
        print(request.form)
    else:
        print('index view - get')
    return render_template('index.html', message='hello')

@app.route('/about/')
def about():
    return render_template('about.html')





    
# $env:FLASK_APP = "app.py" 
# $env:FLASK_ENV = "development"
# python -m flask run