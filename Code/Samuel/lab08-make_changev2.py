# PDX Code Guild Fullstack Course
# Lab 08 Make Change
# Samuel Purdy
# 4/8/2020

import string

# Coins and their respective values
coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

# Helps record the number of coins
number_of_quarters = 0
number_of_dimes = 0
number_of_nickels = 0
number_of_pennies = 0

# Records the remainder when doing division
current_remainder = 0

# Initilized for inputs
user_input = "f"


# Checks to see if the input is a float.
# str1 = string input, usually gotten from input()
def check_if_float(str1):
    # for each character in the string given, loop
    for char in str1:
        if not char.isnumeric():
            if char != ".":
                return False
    return True


# While user_input is not a valid input, it will keep looping until a
# valid input is given.
while not check_if_float(user_input) or float(user_input) < 0:
    user_input = input("Please enter in an amount of money you wish to get change for: (e.g. 210.25)")

# multiplies the input by 100 for easier calculations
user_input = float(user_input) * 100

# If the user_input has a remainder after being divided by coins[0][1], it
# will process code inside the statement.
# It will do it for Quarters, then Dimes, then Nickels and Pennies.
# As long as there is a remainder, it will go deeper into the nested if
# statement.
if(user_input % coins[0][1]):
    number_of_quarters = user_input // coins[0][1]
    current_remainder = user_input % coins[0][1]

    if(current_remainder % coins[1][1]):
        number_of_dimes = current_remainder // coins[1][1]
        current_remainder %= coins[1][1]

        if(current_remainder % coins[2][1]):
            number_of_nickels = current_remainder // coins[2][1]
            number_of_pennies = current_remainder % coins[2][1]
    else:
        number_of_dimes = current_remainder // coins[1][1]
else:
    number_of_quarters = user_input // coins[0][1]

# Prints the amount given by the user, and how the change works into it.
print(f"Here is the change for {user_input/100}")
print(f"Number of {coins[0][0]} = {int(number_of_quarters)}")
print(f"Number of {coins[1][0]} = {int(number_of_dimes)}")
print(f"Number of {coins[2][0]} = {int(number_of_nickels)}")
print(f"Number of {coins[3][0]} = {int(number_of_pennies)}")
