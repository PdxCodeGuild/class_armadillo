from flask import Flask, request, render_template
app = Flask(__name__)
import string
import random







dictionary = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 
                'h':'u', 'i':'v','j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 
                'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 
                'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 
}


def rot(text):
    rot13 = ''
    for character in text:
        if character.islower():
            rot13 += dictionary.get(character)
        if character.isupper():
            character = letter.lower()
            rpt13 += dictionary.get(character).capitalize()
        if character not in dictionary:
            rot13 += character

    return rot13


#  with url localhost:5000 include /rot13 to access web page
@app.route('/rot13', methods=['GET','POST'])
def index():
    text = request.form.get('message')
    translated_text = text
    if text:
        translated_text = rot(text)

    return render_template('rot13.html', text = translated_text)














# # flask app for requests
# @app.route ('/', methods=["GET", "POST"])
# # defines the view
# def index():
#     output = ''
#     if request.method == "POST":
#         # assigns variable and output for uppercase, lowercase, numbers, and special characters.
#         uppercase = int(request.form['uppercase'])
#         for i in range(uppercase):
#             output += random.choice(string.ascii_uppercase)

#         lowercase = int(request.form['lowercase'])
#         for i in range(lowercase):
#             output +=random.choice(string.ascii_lowercase)

#         numbers = int(request.form['numbers'])
#         for i in range(numbers):
#              output += random.choice(string.digits)

#         characters = int(request.form['characters'])
#         for i in range(characters):
#             output += random.choice(string.punctuation)
#         # converts string into list and shuffles the ouput
#         output = list(output)
#         random.shuffle(output)
#         # converts list back to string
#         output = ''.join(output)   
    


#         print(request.form)
#     return render_template("pswd_gen.html", password=password)