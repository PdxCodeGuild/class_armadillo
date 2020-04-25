# Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

# VERSION 1

import random

computer_num = random.randint(1,11)

guesses = 0

while guesses <= 10:
    user_guess = int(input(f'Guess a number [{guesses}]: '))
    if user_guess != computer_num:
        print('Try again!')
    elif user_guess == computer_num:
        print(f'You got it! {computer_num}')
        break
    guesses += 1


# VERSION 2
# Allow the user to make an unlimited number of guesses using a while True and break. Keep track of how many guesses the user has made, and tell them at the end.
import random

computer_num = random.randint(1,10)

guesses = 0

while True:
    user_guess = int(input(f'Guess a number [{guesses}]: '))
    if user_guess != computer_num:
        print('Try again!')
    elif user_guess == computer_num:
        print(f'You got it! Secret Num was {computer_num}. Your guesses {guesses}')
        break

    guesses += 1

# Version 3
# Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

import random

computer_num = random.randint(1,10)

guesses = 0

while guesses <= 10:
    user_guess = int(input(f'Guess a number [{guesses}]: '))

    if user_guess > computer_num:
        print('Too high!')
    elif user_guess < computer_num:
        print('Too low!')

    if user_guess != computer_num:
        print('Try again!')
    elif user_guess == computer_num:
        print(f'You got it! Secret Num was {computer_num}. Your guesses {guesses}')
        break
    
    guesses += 1

# Version 4 (optional)
# Tell the user whether their current guess is closer than their last. This can be done by maintaining a variable containing the last guess outside the loop, then comparing the last guess to the current guess, and check if it's closer. Hint: you're interested in comparing the two absolute differences: abs(current_guess-target) and abs(last_guess-target).

import random

computer_num = 9

guesses = 0

last_guess = ''

while guesses <= 10:
    user_guess = int(input(f'Guess a number [{guesses}]: '))

    if user_guess > computer_num:
        print('Too high!')
    elif user_guess < computer_num:
        print('Too low!')

    if guesses >= 1:
        if abs(user_guess - computer_num) > abs(last_guess - computer_num):
            print('COLD!')
        
        elif abs(user_guess - computer_num) < abs(last_guess - computer_num):
            print('HOT!')

    if user_guess != computer_num:
        print('Try again!')
    elif user_guess == computer_num:
        print(f'You got it! Secret Num was {computer_num}. Your guesses {guesses}')
        break

    last_guess = user_guess
    guesses += 1

# VERSION 5
# Swap the user with the computer: the user will pick a number, and the computer will make random guesses until they get it right.

import random

guesses = 0
secret_number = int(input(f'Pick a secret number the computer will try to guess it: '))

last_guess = ''

while guesses <= 10:
    computer_num = random.randint(1,10)
    print(f'Computer guessed: {computer_num}')
    if computer_num > secret_number:
        print('Too high!')
    elif computer_num < secret_number:
        print('Too low!')

    if guesses >= 1:
        if abs(computer_num - secret_number) > abs(last_guess - secret_number):
            print('COLD!')
        
        elif abs(computer_num - secret_number) < abs(last_guess - secret_number):
            print('HOT!')

    if computer_num != secret_number:
        print('Try again!')
    elif computer_num == secret_number:
        print(f'You got it! Secret Num was {secret_number}. Your guesses {guesses}')
        break

    last_guess = secret_number
    guesses += 1