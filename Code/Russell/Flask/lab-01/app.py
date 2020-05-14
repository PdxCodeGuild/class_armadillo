from flask import Flask, render_template, request
app = Flask(__name__)

import string
import random




@app.route('/', methods=['POST', 'GET'])
def index(): 
    
    if request.method == 'POST':
        
        password_length = int(request.form['Password Length'])
        letters = string.ascii_letters + string.punctuation + string.digits
        
        
        password = ""
        for letter in range(password_length):
            password += random.choice(letters)
   
    
    
    
    temp = 0
    return render_template('index.html', password_length=password_length, letter=letter, password=password, temp=temp )
    
    
    
 


# $env:FLASK_ENV = "development"
# $env:FLASK_APP = "app.py" 
# python -m flask run
