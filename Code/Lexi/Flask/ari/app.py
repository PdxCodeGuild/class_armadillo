from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index(): #view
    if request.method == 'POST':
        print('index view - post')
    else:
        print('index view -get')

    return render_template('index.html', message1='hello', message2='ahoy')

@app.route('/about/')
def about():
    return render_template('about.html')