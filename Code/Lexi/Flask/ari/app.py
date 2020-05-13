from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index(): #view
    if request.method == 'POST': # form submission
        print('index view - post')
        form_data = dict(request.form)
        print(form_data)
    else:
        print('index view -get')
        print(request.form) # empty - did not submit a form to get here
    return render_template('index.html', message1='hello', message2='ahoy')

@app.route('/about/')
def about():
    return render_template('about.html')