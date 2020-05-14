from flask import Flask, render_template, request
app = Flask(__name__)

import ari

# you use regular python functions with your flask app
# def count_words(text):
#     return len(text.split())


@app.route('/', methods=['POST', 'GET'])
def index(): # view
    
    if request.method == 'POST': # form submission
        print('index view - post')
        form_data = dict(request.form)
        print(form_data)
        text = form_data['input_text']
        result = ari.calculate_ari(text)
    else: # viewing the page
        print('index view - get')
        print(request.form) # empty - did not submit a form to get here
        result = ''
    return render_template('index.html', result=result)

@app.route('/about/')
def about():
    return render_template('about.html')