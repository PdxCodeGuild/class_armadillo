import random


# Guess the number is a simple game that allows the user to input guess
# at a random number generated randomly.
# Version 2 allows the user as many attempts as they'd like, and prints
# how many tries there were at the game end.
# Version 3 offers the user advice as they go.
# Version 4 monitors the previous guess and returns adviced based on if the
# guess was nearer or farther from the previous guess. Currently unfinished.


# This function compares the current guess, the previous guess, and returns
# advice based how those compare
def compare_guess(user_guess, last_guess, goal_number):
    # If it's their first guess, we have nothing to compare to.
    if not last_guess:
        if user_guess > goal_number:
            return print("too high!")
        else:
            return print("too low.")

    elif user_guess - goal_number > last_guess - goal_number:
        return print("You're getting colder!")
    elif user_guess - goal_number < last_guess - goal_number:
        return print("You're getting warmer!")
    elif user_guess - goal_number == last_guess - goal_number:
        return print(''' "The definition of insanity is doing the same thing over and over
    again and expecting a different result."
                    - Albert Einstein''')


# set goal number.
goal_number = random.randint(1, 11)

# establish global variables used for verifications.
user_attempts = 0
last_guess = False
valid = False
# take user input and validate that it is digits. if so, make an integer.
while user_attempts <= 10:
    while not valid:
        user_guess = input("What is your guess? ")
        valid = user_guess.isdigit()
        if valid:
            user_guess = int(user_guess)
            break
        else:
            print("please enter a valid response.")
    # check if they won. If they did it in 1, print a different message.
    if user_guess == goal_number:
        user_attempts += 1
        if user_attempts == 1:
            print(f"You win! You got in 1 try!!")
        else:
            print(f"You win!! you guessed {user_attempts} times.")
        break

    # Call our functions and increment the guess counter.
    else:
        compare_guess(user_guess, last_guess, goal_number)
        last_guess = user_guess
        user_attempts += 1
        valid = False

