from flask import Flask, render_template, request
import string 



app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        alphabet= string.ascii_lowercase
        rot_alphabet = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
        output = ''
        text = request.form["word"]
        for char in text:
            index = alphabet.find(char)
            rot = rot_alphabet[index]
            output += rot
        print(text)
    else:
        output = ""
    print(request.form)



    return render_template('index.html', output = output)


