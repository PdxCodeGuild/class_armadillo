import random

# set goal number
goal_number = random.randint(1, 11)
user_attempts = 0
valid = False
# take user input
while True:
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
            print(f"You win!! you guessed {user_attempts} time(s).")
        break
# give some sort of hint
    elif user_guess < goal_number:
        print("a little higher...")
        user_attempts += 1
        valid = False
# increment counter up
    elif user_guess > goal_number:
        print("a little too high.")
        user_attempts += 1
        valid = False
