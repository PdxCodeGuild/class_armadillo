# PDX Code Guild Fullstack Course
# Lab 06 Password Generator
# Samuel Purdy
# 4/8/2020

# Imports Random Module
import random
import string

# Custom Module used to verify inputs when using input().
import verify

# Initilizing characters
valid_inputs = ["Yes", "No"]
set_password_length = None
character_counter = 0
character_types = ""
character_password = ""
user_input = None

# verify.valid_input(set_password_length, is_positive = True, is_numeric = True)

# Checks to see if the users input is valid and then sets the number
# while not set_password_length.isnumeric() or int(set_password_length) < 1:
#     set_password_length = input("Please input a number that will define how long the password will be: ")

while not verify.valid_input(set_password_length, is_positive = True, is_numeric = True):
    set_password_length = input("Please input a number that will define how long the password will be: ")

# Runs while there are not items in list character_types
while len(character_types) == 0:
    # Checks whether or not the user entered a valid choice for if they wanted
    # capital characters.
    while not verify.valid_input(user_input, valid_inputs, against_list = True, against_string = True):
        user_input = input("Would you like capital characters in your password? (Yes/No) ")
        # Appends the character types list to add capital characters.
        if user_input == "Yes":
            character_types += string.ascii_uppercase
    user_input = None

    # Checks whether or not the user entered a valid choice for if they wanted
    # lowercase characters.
    while not verify.valid_input(user_input, valid_inputs, against_list = True, against_string = True):
        user_input = input("Would you like lowercase characters in your password? (Yes/No) ")
        # Appends the character types list to add lowercase characters.
        if user_input == "Yes":
            character_types += string.ascii_lowercase
    user_input = None

    # Checks whether or not the user entered a valid choice for if they wanted
    # number characters.
    while not verify.valid_input(user_input, valid_inputs, against_list = True, against_string = True):
        user_input = input("Would you like number characters in your password? (Yes/No) ")
        # Appends the character types list to add number characters.
        if user_input == "Yes":
            character_types += string.digits
    user_input = None

    # Checks whether or not the user entered a valid choice for if they wanted
    # symbol characters.
    while not verify.valid_input(user_input, valid_inputs, against_list = True, against_string = True):
        user_input = input("Would you like symbol characters in your password? (Yes/No) ")
        # Appends the character types list to add symbol characters.
        if user_input == "Yes":
            character_types += string.punctuation
    user_input = None

    # Checks to see if the user made any choices by checking the length of the
    # string of characters to choose from. If not, it will go back and make
    # them choose at least one.
    if len(character_types) == 0:
        print("You have selected no character types, please select at least one to proceed.")
        break


# Adds a random character to the password until the password is at the chosen
# length.
while character_counter != int(set_password_length):
    # Chooses a random index from list character_types, then chooses a random
    # character from that index and adds it to the password.
    character_password += random.choice(random.choice(character_types))
    character_counter += 1

# Prints the password back to the user
print(f"This is the password that was generated: {character_password}")
