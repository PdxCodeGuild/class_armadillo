'''Let's play 'Guess the Number'. The computer will guess a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Concepts Covered
random.randint
REPL: read-evaluate-print loop
input, print
Version 1
Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost. If the user guesses the number, the user is told they've won and the game exits. You can get a random number using random.randint:

import random
x = random.randint(1,10)
print(x)
Below is an example run of the game:

guess the number: 5
try again!
guess the number: 2
try again!
guess the number: 3
correct! you guessed 3 times'''

import random  # get that random module

def mind_reader():
    pass

# generate a random integer between 1 and 10
secret = random.randint(1, 10)  

number_of_guesses = 0
while number_of_guesses < 10:
    # print(f"{number_of_guesses = }") # brand new syntax in Python 3.8 to print a label with a variable in an f-string

    print(f"Guesses remaining: {10 - number_of_guesses}")

    # prompt the user for a guess
    guess = input("Please enter a number between 1 and 10: ")

    # convert the guess string into an integer
    guess = int(guess)

    # test the guess against the secret
    if guess > secret:
        print("Too high!")

    elif guess < secret:
        print("Too low!")

    elif guess == secret:
        if number_of_guesses <= 1:
            message = f"You're a wizard, Harry!"
        elif number_of_guesses <= 4:
            message = f"You're above average!"
        elif number_of_guesses <= 8:
            message = f"You're below average!"
        else:
            message = f"You statistically suck, kid!"
        
        print(message)    
        print(f"You guessed the secret in {number_of_guesses + 1} guess(es)!")
        break

    number_of_guesses += 1
    