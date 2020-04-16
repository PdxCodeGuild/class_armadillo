

# imports and variables used 
import random
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']
kill_commands = ["quit", "q", "exit", "stop", "esc", "escape"]


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
# Any non-number, or any non-negative number over num2
def validate_input_function():      
    total_pennies = input("Enter a how many pennies you have, and I'll convert it to dollars: ")
    while not total_pennies.isnumeric():
        if total_pennies in kill_commands:
            endgame()
        elif not total_pennies.isnumeric():
            print(f"'{total_pennies}'' is not a valid input. Please enter a non-negative integer. ")
            total_pennies = input("Enter a how many pennies you have, and I'll convert it to dollars: ")
        return total_pennies

def convert():
    while True:
        validate_input_function()
        print(f"The validate_input_function() returns: {validate_input_function}. ")
        total_pennies = int(total_pennies)
        dollars = total_pennies / 100
        print(f"You have ${dollars}.")


def pennies_to_dollars():
    total_pennies = input("Enter a how many pennies you have, and I'll convert it to dollars: ")
    while not total_pennies.isnumeric():
        if total_pennies in kill_commands:
            endgame()
        elif not total_pennies.isnumeric():
            print(f"'{total_pennies}'' is not a valid input. Please enter a non-negative integer. ")
            total_pennies = input("Enter a how many pennies you have, and I'll convert it to dollars: ")  
        break

    print(f"The first coded question returns: total_pennies = {total_pennies}. ")
    total_pennies = int(total_pennies)
    dollars = total_pennies / 100
    print(f"You have ${dollars}.")

def play_again():
    while True:
        ask_again = input("Would you like to play again? ")
        if ask_again.lower() in affirmatives:
            pennies_to_dollars()
        elif ask_again.lower() in negatives:
            print("Goodbye! ")
            break
        elif ask_again.lower() in kill_commands:
            endgame()
        else:
            print("I'm sorry, I don't understand that response. Please try again. ")

print("Welcome to Lab 08: Make Change." )

pennies_to_dollars()
play_again()

