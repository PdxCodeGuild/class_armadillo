#Lab 08: Make Change 
#Kyle Harasimowicz

# imports and variables used 
import random
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']
kill_commands = ["quit", "q", "exit", "stop", "esc", "escape"]


def endgame():
    print("Goodbye!")
    quit()

# Asks the user to input the number in a given condition
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


# function to check if a string is a float
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

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

## Converts a dollar amount in float notation to pennies
## will break if the user input is not in float form
def dollars_to_pennies():
    dollar_amount = input("Enter your dollar amount (i.e. 1.36) and I'll convert to it to pennies. ")
    while not dollars_to_pennies is int or not dollars_to_pennies is float:
        dollar_amount = input("Enter your dollar amount (i.e. 1.36) and I'll convert to it to pennies. ")
        if dollar_amount in kill_commands:
            endgame()
        elif not dollar_amount in kill_commands:
            dollar_amount = float(dollar_amount)
        break
    
    print(f"The first coded question returns: dollar_amount = {dollar_amount}. ")
    pennies = int(dollar_amount * 100)
    print(f"You had ${dollar_amount}. That's {pennies} pennies, or ¢{pennies}. ")

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

dollars_to_pennies()
play_again()

# program to turn a dollar amount into change of quarters, dimes, nickels, and pennies
# while true:
#     dollars_to_change = float(input("Please enter your dollar amount in X.XX format. You have: $"))
#     dollars_to_change = dollars_to_change * 100

