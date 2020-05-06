
import random

choices = ['yes', 'no', 'maybe so']

while True:
    question = input('what is your question? ')
    choice = random.choice(choices)
    print(choice)

    ask_another = input('would you like to ask another question? ').lower().strip()
    if ask_another != 'yes':
        break
