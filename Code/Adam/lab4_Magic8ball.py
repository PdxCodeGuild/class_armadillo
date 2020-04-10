"""

Lab 4: Magic 8-Ball

Let's write a program to simulate the classic "Magic Eight Ball"

Concepts Covered

-input, print
-import
-random.choice

Instructions

1. Print a welcome screen to the user.
2. Use the random module's random.choice() to choose a prediction.
3. Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
4. Display the result of the 8-ball.

"""
import random

#lists
eight_ball = ["all knowing", "brilliant", "magnificent", "infallable"]

predictions = ["It is certain. ", "It is decidedly so. ", "Without a doubt. ", "Don't count on it. ", "Don't hold your breathe. ", "The outlook is grim. ", "50/50"]

#random_choices
title = random.choice(eight_ball)

prediction = random.choice(predictions)

#welcome_screen
print("Welcome to the Magic 8-Ball! ")

#prompt_user
question = input("what is your question? ")

print(f"The {title}8-Ball says...{prediction}")
