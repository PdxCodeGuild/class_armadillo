import random

# set goal number
goal_number = random.randint(1, 11)
user_attempts = 0

# take user input
while user_attempts < 10:
    user_guess = int(input("What is your guess? "))
    # check if it's right
    if user_guess == goal_number:
        print(f"You win!! you guessed {user_attempts}")
        break
# give some sort of hint
    elif user_guess < goal_number:
        print("a little higher...")
        user_attempts += 1
# increment counter up
    elif user_guess > goal_number:
        print("a little too high.")
        user_attempts += 1
    else:
        print("please enter a valid response.")

if user_attempts == 10:
    print(f"Oh no! You've lost. the computer number was {goal_number}")
