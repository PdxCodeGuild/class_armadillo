

# imports the modules
from flask import Flask, request, render_template
import string
import random
app = Flask(__name__)

# flask application for the requests
@app.route('/', methods=["GET", "POST"])
# defines the view
def index():
    output = []
    if request.method == "POST":
        # Original Code
        # alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        # password_length = int(request.form["password_length"])

        # uppercase = [ABCDEFGHIJKLMNOPQRSTUVWXYZ]
        # lowercase = [abcdefghijklmnopqrstuvwxyz]
        # number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        # special_characters = [!@#$%^&*]

        # assigns the variable and the ouput for the uppercase letters
        uppercase = int(request.form["uppercase"])
        for i in range(uppercase):
            output += random.choice(string.ascii_uppercase)
        # assigns the variable and the ouput for the lowercase letters
        lowercase = int(request.form["lowercase"])
        for i in range(lowercase):
            output += random.choice(string.ascii_lowercase)
        # assigns the variable and the ouput for the numbers
        numbers = int(request.form["numbers"])
        for i in range(numbers):
            output += random.choice(string.digits)
        # assigns the variable and the ouput for the special characters
        special_characters = int(request.form["special_characters"])
        for i in range(special_characters):
            output += random.choice(string.punctuation)
        # converts strings into a list and shuffles the ouput
        password = list(output)
        random.shuffle(output)
        

        message = ''.join(output)

        print(request.form)

    return render_template('index.html', password= output)
# # Python program to convert a list 
# # to string using list comprehension 
   
# s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
  
# # using list comprehension 
# listToStr = ' '.join(map(str, s)) 
  
# print(listToStr)  