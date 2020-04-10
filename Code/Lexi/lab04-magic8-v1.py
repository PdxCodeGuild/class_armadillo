# https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/labs/lab04-magic_8_ball.md

# Lab 4: Magic 8-Ball
# Let's write a program to simulate the classic "Magic Eight Ball"

# Concepts Covered
# input, print
# import
# random.choice
# Instructions
# Print a welcome screen to the user.

import random

while True:


    greeting = input("Hello, welcome to the Magic of the 8 ball. want to play? y/n: ")
    # Use the random module's random.choice() to choose a prediction.
    question = (input("Type your question here: "))

    decisions = [  # this was a set - cannot do indexing since set is unordered

        "It is certain",
        "It is decidedly so",
        "Without a doubt",
        "Yes definitely",
        "You may rely on it",
        "As I see it, yes",
        "Most likely",
        "Outlook good",
        "Yes",
        "Signs point to yes",
        "Reply hazy try again",
        "Ask again later",
        "Better not tell you now",
        "Cannot predict now",
        "Concentrate and ask again",
        "Don't count on it",
        "My reply is no",
        "My sources say no",
        "Outlook not so good",
        "Very doubtful"
    ]

    choices = (random.choice(decisions))
    print(choices)
    ask_for_more = input('got more Qs?')
    if greeting != 'y':
        break


# while True:
#     question = input("want to play?")
#     if question == 'y':
#         decision = input("select a number 1 through 19")
#     else:
#         break
# Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
# Display the result of the 8-ball.
# Below are some example 'predictions':

# It is certain
# It is decidedly so
# Without a doubt
# Yes definitely
# You may rely on it
# As I see it, yes
# Most likely
# Outlook good
# Yes
# Signs point to yes
# Reply hazy try again
# Ask again later
# Better not tell you now
# Cannot predict now
# Concentrate and ask again
# Don't count on it
# My reply is no
# My sources say no
# Outlook not so good
# Very doubtful
# Version 2
# Using a while loop, keep asking the user for a question, if they enter 'done', exit