#    Print a welcome screen to the user.
#    Use the random module's random.choice() to choose a prediction.
#    Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
#    Display the result of the 8-ball.

#   Version 1  Greets the player and asks for question

print("You enter the palace of the Mystical 8 Ball\n")

input("Welcome to the Magic 8 Ball, owner of the valley of jehoshaphat. . . Please ask your question: ")

import random
decisions = ['It is certain', 'Dont count on it', 'Ask again later']
answer = random.choice(decisions)

print('\n' + answer)

#   Version 2  Asks player if they want to ask another

while True:
    go_again = input("\nWould you like to ask again? ")

    if go_again == ('done'):
        print('\nOk no more answers. . .')
        break
    else:
        input("\nOk, what's your Question? ")
        answer = random.choice(decisions)
        print('\n' + answer)