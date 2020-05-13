from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(length, is_upper, is_special, numbers):
    possible_characters = list(string.ascii_lowercase)
    length = int(length)
    if is_upper:
        uppers = string.ascii_uppercase
        for upper in uppers:
            possible_characters.append(upper)
    if is_special:
        specs = ["!", "#", "$", "%", "&", "+", ".", "?", "@", "~"]
        for spec in specs:
            possible_characters.append(spec)
    if numbers:
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for num in nums:
            possible_characters.append(num)
    password = []
    for i in range(length):
        password.append(random.choice(possible_characters))
    password = "".join(password)
    return password


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    context = {}
    if request.method == "POST":
        length, is_upper, is_special, numbers = request.form["length"], request.form["upper"], request.form["special"], request.form["numbers"], 
        password = generate_password(length, is_upper, is_special, numbers)
        print(password)
        context={
            "password":password,
        }
    return render_template("index.html", context=context)
