from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def generatePassword():
    if request.method == "POST":
        userEntry = request.form['length']
        char = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        passwordCharList = []
        while char in range(int(userEntry)):
            passwordCharList.append(random.choice(alphabet))
            char += 1
            password = ''.join(passwordCharList)
            
    else:
        password = "Something happened. Something bad. Blame $9.99 Udemy Flask Tutorials."
        
    return render_template('index.html', password=password)