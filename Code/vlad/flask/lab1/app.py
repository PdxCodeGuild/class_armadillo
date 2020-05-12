# to run flask I need to enter the following in the terminal each time:  python3 -m flask run


from flask import Flask, render_template # I need to enter after the coma render_template to be able 
#connect index html to the browser
app = Flask(__name__)

@app.route('/') # localhost:5000/
def hello_world():
    return render_template('index.html')
