
# db.json

# {
#     "user_score": 0,
#     "computer_score": 0
# }

from flask import Flask, render_template, request
import json, random
app = Flask(__name__)

def save_database(data):
    with open('db.json', 'w') as file:
        file.write(json.dumps(data))

def load_database():
    with open('db.json', 'r') as file:
        data = json.loads(file.read())
        return data

def computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

# Version 1
# Show the user a page with a form containing a dropdown list with "rock", "paper" and "scissors" and a submit button. When the user selects rock, paper, or scissors and hits submit, show the computer's choice and tell them whether they won or lost.

# Version 2
# Keep track of the score between the user and the computer, show the scores in the page and update the scores after a game is played.
@app.route('/', methods=['POST', 'GET'])
def index():
    data = load_database()
    user_choice = ''
    if request.method == 'POST':
        user_choice = request.form['choice'] # = value
        computer = computer_choice()


        if user_choice == computer:
            data['ties'] += 1
        elif user_choice == 'Rock' and computer == 'Scissors':
            data['user_score'] += 1
        elif user_choice == 'Scissors' and computer == 'Paper':
            data['user_score'] += 1
        elif user_choice == 'Paper' and computer == 'Rock':
            data['user_score'] += 1
        else:
            data['computer_score'] += 1

        save_database(data)

    return render_template('index.html', user_score=data['user_score'], computer_score=data['computer_score'], computer_choice=computer_choice(), ties=data['ties'], user_input=user_choice)
