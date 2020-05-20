from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)
@app.route('/', methods=["POST", "GET"])
def index():
    score = load_database()
    if request.method == "POST":
        weapons = ["paper", "rock", "scissors"]
        user_choice = request.form["user_choice"]
        computer = random.choice(weapons)
        print(score)
        if user_choice == "rock" and computer == "paper":
            result = "✋ covers ✊ Boom! You lose Sucka! "
            score["computer_score"] += 1
        elif user_choice == "scissors" and computer == "rock":
            result = "✊ smashes ✌ Boom! You lose Sucka!"
            score["computer_score"] += 1
        elif user_choice == "paper" and computer == "rock":
            result = "✋ covers ✊ Boom! You lose Sucka!"
            score["computer_score"] += 1
        elif user_choice == "paper" and computer == "scissors":
            result = "✌ cut ✋ Damn you win!"
            score["user_score"] += 1
        elif user_choice == "rock" and computer == "scissors":
            result = "✊ smashes ✌ Damn you win!"
            score["user_score"] += 1
        elif user_choice == "scissors" and computer == "paper":
            result = "✌ cut ✋ Damn you win!"
            score["user_score"] += 1
        elif user_choice == computer:
            result = "Crapsticks! It is a tie!"
        save_database(score)
        return render_template("index.html", score=score, result=result, user_choice=f"You chose: {user_choice}", computer=f"The computer chose: {computer}")
    return render_template("index.html", result="", computer="", score=score)


# # opens db.json, turns the python dictionary into json, and saves it to the file
def load_database():
     with open('db.json', 'r') as file:
         data = json.loads(file.read())
     return data


# # opens db.json, turns the python dictionary into json, and saves it to the file
def save_database(data):
    with open('db.json', 'w') as file: # open the file
        text = json.dumps(data, indent=4) # turn the python dictionary into a json string
        file.write(text)