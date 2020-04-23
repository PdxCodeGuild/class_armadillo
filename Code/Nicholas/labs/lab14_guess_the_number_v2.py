#this allows user to guesses computer generated value between 1-10 until they guess it correctly.

import random

#have the computer randomly choose a number
computer_choice = random.randint(1, 10)
i = 1
while True:
    #ask the user for their guess
    user_input = int(input('Guess a number between 1 and 10: '))
    #check if user guessed the correct answer
    if user_input == computer_choice:
        print(f'You got it right! You guessed {i} times') #tells user how many guesses it took them
        break
    #avoid printing 'try again' if the user runs out of guesses
    print('try again')
    i += 1  #adds up user guesses
