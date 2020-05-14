from flask import Flask, render_template, request
app = Flask(__name__)

import string
import random




@app.route('/', methods=['POST', 'GET'])
def index(): 
    
    
    password = ""
    if request.method == 'POST':
        
        password_length = int(request.form['Password Length'])
        letters = string.ascii_letters + string.punctuation + string.digits
        
        
        for _ in range(password_length):
            password += random.choice(letters)
   
    
    
    
   
    return render_template('index.html', password=password )
    
    
    
 


# $env:FLASK_APP = "app.py" 
# $env:FLASK_ENV = "development"
# python -m flask run
