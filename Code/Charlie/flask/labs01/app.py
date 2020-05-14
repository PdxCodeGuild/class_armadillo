
# john helped with lab
from flask import Flask, request, render_template
import random
import string

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/rotate', methods=["GET", "POST"])
def rotate():
    if request.method == "POST":
        user_text = str(request.form['text'])
        alphabet ='abcdefghijklmnopqrstuvwxyz'
        rotated_alphabet = alphabet[13:] + alphabet[:13]
        text_length = (user_text)

        length_of_text = ''
        for char in text_length:
            index = alphabet.find(char)
            rotated_char = rotated_alphabet[index]
            length_of_text += rotated_char
            output = length_of_text
    else:
        output = ''

    

    return render_template('rotate.html', output=output)
    





@app.route('/password', methods=["GET", "POST"])
def password():
    if request.method == "POST":
        user_number = request.form['number']
        i = 0
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password_num = int(user_number)

        pass_length = []
        while i in range(password_num):
            pass_length.append(random.choice(alphabet))
            i += 1
            user_input = ''.join(pass_length)
            output = user_input

    else:
        output = ''
    
    return render_template('index.html', output=output)
