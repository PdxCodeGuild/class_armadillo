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
import time

#pychalk

#lists
eight_ball = ['all knowing ', 'brilliant ', 'magnificent ', 'infallable ', 'amazing ', 'incredible ', 'inscrutable ']

predictions = ['It is certain. ', 'It is decidedly so. ', 'Without a doubt. ', 'Don\'t count on it. ', 'Don\'t hold your breathe. ', 'The outlook is grim. ', '50/50']

#random_choices
title = random.choice(eight_ball) # pick a random title from eight_ball list

prediction = random.choice(predictions) # pick a random prediction from predictions list


#welcome_screen
print(f"\nWelcome to the Magic 8-Ball!\n")
time.sleep(.5)

# Version 2 - Allow the user to replay until they enter done
loop = True
while loop == True:
    response = input(f'Do you have a question for the {title}8-Ball? ').lower()
    time.sleep(.5)
    if response == 'yes':
        question = input('what is your question? ') # prompt_user
        time.sleep(.5)
        print(f'The {title}8-Ball says...{prediction} ') # display the result

    elif response == 'no':
        time.sleep(.5)
        print('Goodbye. ')
        loop = False
