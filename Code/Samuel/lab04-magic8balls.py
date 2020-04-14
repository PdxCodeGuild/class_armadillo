# PDX Code Guild Fullstack Course
# Lab 04 Magic 8 Ball
# Samuel Purdy
# 4/7/2020

# Imports the random Module.
import random

# Custom Module used to verify inputs when using input().
import verify

# Correct inputs
correct_input = "done"

# List of Magic 8-ball responses.
magic8ball = ["As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again", "Don't count on it", "It is certain.", "It is decidedly so.", "Most likely", "My Reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes - Definitely.", "You may rely on it."]

# Initialized user_input.
user_input = None

# Welcomes the user to the magic 8 ball.
print("----------------------------")
print("Welcome to the Magic 8-ball!")
print("----------------------------")

# While the user is not done asking questions, keep looping responses for each question except for "done".
while not verify.valid_input(user_input, correct_input, against_string = True):

    # Asks what you desire to know.
    user_input = input("What do you wish to know about your future? (enter \"done\" when you are done.)")

    # Checks to see if the user is is done or not.
    if user_input == "done":
        print("Goodbye")
    else:
        # Produces a random response
        print(random.choice(magic8ball))
        user_input = None
