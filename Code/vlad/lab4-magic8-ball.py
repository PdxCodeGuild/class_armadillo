#Lab 4: Magic 8-Ball Version 1 and Version 2!

""" Instructions
Print a welcome screen to the user!.

Use the random module's random.choice() to choose a prediction.

Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"

Display the result of the 8-ball."""

import random

predictions = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful',
    
]
print('Welcome to the Magic 8-Ball Game are you excited to play!! ')
while True:

    user = input("Ask a question to the 8 ball? ")



    prediction = random.choice(predictions)
    print(prediction)
    play_again = input("Would like to play again enter yes/no ")
    if play_again == "yes":
        continue
    elif play_again == "no":
        print("Have a nice day Bye!")
        break

