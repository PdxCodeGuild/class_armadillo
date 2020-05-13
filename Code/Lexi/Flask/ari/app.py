from flask import Flask, render_template, request
app = Flask(__name__)

import ari

def count_words(text):
    return len(text.split())


@app.route('/', methods=['POST', 'GET'])
def index(): #view
    if request.method == 'POST': # form submission
        print('index view - post')
        form_data = dict(request.form)
        print(form_data)
        text = form_data['input_text']
        words = count_words(text)
        result = ari.calculate_ari(text)


    else:
        print('index view -get')
        print(request.form) # empty - did not submit a form to get here
        result = ''
    return render_template('index.html', message1='hello', message2='ahoy', result=result)

@app.route('/about/')
def about():
    return render_template('about.html')