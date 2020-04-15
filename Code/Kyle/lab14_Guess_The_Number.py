# imports and variables used 
import random
user_guess = ""
computer_number = ""

# def mind_reader():
#     pass

# computer_number = random.randint(0, 10)

# number_of_guesses = 0
# while True:

#     user_guess = (input("Choose a number between 0 and 10: "))

#     if user_guess > computer_number:
#         print("Too High!")
#     elif user_guess < computer_number:
#         print("Too Low!)")
#     elif user_guess == computer_number:


computer_number = random.randint(0, 10)
print("Welcome to Lab 14. Your computer is thinking of a number between 1 and 10. What's your guess?")

user_guess = (input("Choose a number between 1 and 10: "))
while not user_guess.isnumeric() or int(user_guess) > 10:
    if int(user_guess) > 10:
        print("Too high. Pick a lower number. ")
        user_guess = (input("Choose a number between 1 and 10: "))
    else:
        print("That's not a valid input. Please enter a non-negative integer between 1 and 10. ")
        user_guess = (input("Choose a number between 1 and 10: "))

user_guess = int(user_guess)
if user_guess > computer_number:
    print("Too high. Try again. ")
elif user_guess < computer_number:
    print("Too low. Try again. ")
elif user_guess == computer_number:
    print("Well done - you guessed correctly!")