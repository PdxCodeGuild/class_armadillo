import random


def compare_guess(user_guess, last_guess, goal_number):
    if not last_guess:
        if user_guess > goal_number:
            return print("too high!")
        else:
            return print("too low.")

    elif user_guess - goal_number > last_guess - goal_number:
        return print("colder")
    elif user_guess - goal_number < last_guess - goal_number:
        return print("warmer")


# set goal number
goal_number = random.randint(1, 11)
user_attempts = 0
last_guess = False
valid = False
# take user input
while user_attempts <= 10:
    while not valid:
        user_guess = input("What is your guess? ")
        valid = user_guess.isdigit()
        if valid:
            user_guess = int(user_guess)
            break
        else:
            print("please enter a valid response.")
    # check if it's right
    if user_guess == goal_number:
        user_attempts += 1
        if user_attempts == 1:
            print(f"You win! You got in 1 try!!")
        else:
            print(f"You win!! you guessed {user_attempts} times.")
        break

    elif user_guess < goal_number:
        compare_guess(user_guess, last_guess, goal_number)
        last_guess = user_guess
        user_attempts += 1
        valid = False

    elif user_guess > goal_number:
        compare_guess(user_guess, last_guess, goal_number)
        last_guess = user_guess
        user_attempts += 1
        valid = False
