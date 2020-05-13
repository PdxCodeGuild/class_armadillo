# THIS IS MY VIEW
# completed with Pete Jones

from flask import Flask, render_template, request
# always remember 2nd 'flask' is Capitalized
app = Flask(__name__)

#decorator
@app.route('/', methods=['GET', 'POST']) # this is the path, and it calls whatever is below it

def index(): #  Simple version: the user could just input the word to encode.
    

    return render_template('index.html')

@app.route('/test/', methods=['GET', 'POST'])
def test():

    if request.method == 'POST':
        print(request.form['box1'])
        # bunny
        # 127.0.0.1 - - [12/May/2020 17:38:40] "POST /test/ HTTP/1.1" 200 -
        # 127.0.0.1 - - [12/May/2020 17:38:45] "POST / HTTP/1.1" 200 -
        # 127.0.0.1 - - [12/May/2020 17:38:45] "GET /static/style.css HTTP/1.1" 304 -
        # 127.0.0.1 - - [12/May/2020 17:38:45] "GET /static/rot13%20logo.png HTTP/1.1" 304 -
        # Hi Pete

    return "Test 1 was run!"