# imports and variables used 
import random
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']
kill_commands = ["quit", "q", "exit", "stop", "esc", "escape"]
user_guess = ""
computer_number = ""
num1 = 10
num2 = 78
total_guesses = 0
max_guesses = num2 - num1 + 1

# codes a few 'quit' options 
def endgame():
    print("Goodbye!")
    quit()

# checks to make sure the upper bound is larger than the lower bound
def range_check():
    if not int(num2) > int(num1) + 1:
        print("This will only work if the upper bound is greater than the lower bound.")
        print("Please fix your variable values. ")
        print("'num2' needs to be at least 2 greater than 'num1' ")
        endgame()

# Asks the user to input the number in a given range
# While loop repeats if user gives either of two invalid options
        # Any non-number, or any non-negative number overside the specified range
def validate_input_function():      
    user_guess = (input(f"Choose a number between {num1} and {num2}. "))
    while not user_guess.isnumeric() or not int(user_guess) in range(int(num1), int(num2)+1):
        if user_guess in kill_commands:
            endgame()
        elif not user_guess.isnumeric():
            print(f"That's not a valid input. Please enter a non-negative integer between {num1} and {num2}. ")
            user_guess = (input(f"Choose a number between {num1} and {num2}. "))
        elif not int(user_guess) in range(int(num1), int(num2)+1):
            print(f"{user_guess} is not within the upper and lower bounds.")
            if int(user_guess) < int(num1):
                print(f"{user_guess} is too Low.")
                print(f"Please enter a non-negative integer between {num1} and {num2}. ")
                user_guess = (input(f"Choose a number between {num1} and {num2}. "))
            else:
                print(f"{user_guess} is too High.")
                print(f"Please enter a non-negative integer between {num1} and {num2}. ")
                user_guess = (input(f"Choose a number between {num1} and {num2}. "))
    return user_guess

# Counts the total guesses, and how many are remaining in the game.    
# Can't find a way to get the guess counter to work
# Need to return an incremended guess count
# But I'm not passing one from mind_reader into guess_counter
def guess_counter():
    
    if total_guesses == 1:
        print(f"That's one guess, you have {int(max_guesses) - int(total_guesses)} guesses remaining. Try again. ")
        total_guesses += 1
        return total_guesses
    elif total_guesses < int(max_guesses) - 1:
        print(f"You've guessed {total_guesses} times, and have {int(max_guesses) - int(total_guesses)} guesses remaining. Try again. ")
        total_guesses += 1
        return total_guesses
    elif total_guesses == int(max_guesses) - 1:
        print(f"You've guessed {total_guesses} times, and have {int(max_guesses) - int(total_guesses)} guess remaining. ")
        print("Better make this one count. Try again. ")
        total_guesses += 1   
        return total_guesses
    elif total_guesses == int(max_guesses):
        print(f"You've guessed {total_guesses} times, out of {max_guesses} possible attempts.")
        print("You don't deserve to continue. Game Over. ")
        total_guesses += 1
        return total_guesses
    

# function runs the guessing game
def mind_reader():
    computer_number = random.randint(num1, num2)
    while True:
        total_guesses = 0
        while total_guesses <= max_guesses:
            user_guess = validate_input_function()
            user_guess = int(user_guess)
        # Once the user's input has cleared 
            # total_guesses += 1
            if user_guess > computer_number:
                print(f"The computer chose {computer_number}." )
                print("Too high. Try again. ")
                guess_counter()
            elif user_guess < computer_number:
                print(f"The computer chose {computer_number}." )
                print("Too low. Try again. ")
                guess_counter()
            elif user_guess == computer_number:
                print("Well done - you guessed correctly!")
                break

def mind_reader_no_guess():
    computer_number = random.randint(num1, num2)
    while True:
        user_guess = validate_input_function()
        user_guess = int(user_guess)
    # Once the user's input has cleared 
        if user_guess > computer_number:
            print(f"The computer chose {computer_number}." )
            print("Too high. Try again. ")
        elif user_guess < computer_number:
            print(f"The computer chose {computer_number}." )
            print("Too low. Try again. ")
        elif user_guess == computer_number:
            print("Well done - you guessed correctly!")
            break

# asks the user if they want to play again.
def play_again():
    while True:
        ask_again = input("Would you like to play again? ")
        if ask_again.lower() in affirmatives:
            mind_reader_no_guess()
        elif ask_again.lower() in negatives:
            print("Goodbye! ")
            break
        elif ask_again.lower() in kill_commands:
            endgame()
        else:
            print("I'm sorry, I don't understand that response. Please try again. ")


print(f"Welcome to Lab 14. Your computer is thinking of a number between {num1} and {num2}. What's your guess?")

range_check()
mind_reader_no_guess()

play_again()




