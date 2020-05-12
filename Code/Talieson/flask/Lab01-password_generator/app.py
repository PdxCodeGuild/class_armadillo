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
    return render_template("index.html", context=context)
    


# # If the password is suppose to be randomized, randomize length and characters
# if full_rand == "Y":
#     length = random.randint(7, 16)
#     password = "".join(random.sample(rand_alphabet, length))
#     print(f"Here is your new password: {password}")

# # If not fully random, ask for # of each type of characters, join and randomize
# if full_rand == "N":
#     letters = int(input("How many characters should be letters? "))
#     password = "".join(random.sample(characters, letters))

#     numbers = int(input("How many characters should be numbers? "))
#     password += "".join(random.sample(digits, numbers))

#     punctuation = int(input("How many special characters should there be? "))
#     password += "".join(random.sample(specials, punctuation))

# # Password is still in order, need to shuffle, so convert to a list -> shuffle
#     password_list = list(password)
#     random.shuffle(password_list)
#     password = "".join(password_list)

#     print(f"Here is your new password: {password}")
