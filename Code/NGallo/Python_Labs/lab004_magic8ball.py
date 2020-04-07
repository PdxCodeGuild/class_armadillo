# Nick Gallo
# Lab004 - Magical 8 Ball
# 4/07/2020

import random

print("\n\n--------Welcome to the MAGICAL 8 BALL--------\n")


def magic_ball():
    keep_it_going = True

    while keep_it_going:
        list_of_choices = ["it's for certain", "yes, definitely!", "without a single doubt!", "it might happen...", "it's 50/50", "it's possible", "not gonna happen, sorry", "Nope, sorry", "Negative, Nancy" , "SORRY DAVE I CAN'T DO THAT - try again"]

        user_input = input("Would you like to ask the Magic 8 Ball a question? y/n ")

        if user_input == "y":
            input("Alright, what would you like to ask? ")
            print(random.choice(list_of_choices))
        elif user_input == "n":
            print("Farewell, friend!")
            keep_it_going = False
        else:
            print("would you like to try again?")
magic_ball()

'''
Lab 4: Magic 8-Ball
Let's write a program to simulate the classic "Magic Eight Ball"

Concepts Covered
input, print
import
random.choice
Instructions
Print a welcome screen to the user.
Use the random module's random.choice() to choose a prediction.
Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
Display the result of the 8-ball.
Below are some example 'predictions':

It is certain
It is decidedly so
Without a doubt
Yes definitely
You may rely on it
As I see it, yes
Most likely
Outlook good
Yes
Signs point to yes
Reply hazy try again
Ask again later
Better not tell you now
Cannot predict now
Concentrate and ask again
Don't count on it
My reply is no
My sources say no
Outlook not so good
Very doubtful
Version 2
Using a while loop, keep asking the user for a question, if they enter 'done', exit
'''