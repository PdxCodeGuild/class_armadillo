# PDX Code Guild Fullstack Course
# Lab 05 Random Emoticon Generator
# Samuel Purdy
# 4/8/2020

# Imports Random Module.
import random

# Custom Module used to verify inputs when using input().
import verify

correct_inputs = ["Yes", "No"]

# Set Face details.
eyes = [":", ";", "8", "="]
noses = ["^", "O", "*"]
mouths = [")", "(", "[", "]"]


# Returns a face string with randomly selected features.
def return_random_face():
    random_face = random.choice(eyes) + random.choice(noses) + random.choice(mouths)
    return random_face


# Prints a random face message.
def print_random_face_message():
    print("---------------------------------------")
    print(f"This program prints emoticons like: {return_random_face()}")
    print("---------------------------------------")


# Prints a number of random faces based on the integer given
# int1 : input integer
def print_random_faces_input(int1):
    for x in range(int1):
        print(return_random_face())


# Checks if an integer is within a specified range.
# int1 : input integer.
# int2 : lowest integer in the range to check against.
# int3 : highest integer in the range to check against.
def within_range(int1, int2, int3):
    return False if int1 < int2 or int1 > int3 else True


# Checks whether or not the integer given is positive or not.
# int1 : input integer
def within_positive(int1):
    return True if int1 > 0 else False


# Prints a face based on the users input
def print_specific_face():

    # Pre-specified inputs
    emoticon_input = None
    user_emoticon = ""

    # Prints the Eyes menu
    print("-----------------------")
    print("List of Eyes")
    print("0 - :")
    print("1 - ;")
    print("2 - 8")
    print("3 - =")
    print("4 - Random Eyes")

    # Checks whether the number is numeric or within the specified range, and
    # asking continuously until given a proper input to exit the loop.
    # Ranges are -1 and 5 to inclujde 0 and 4 within the check
    while not verify.valid_input(emoticon_input, against_range = True, range_low = -1, range_high = 5):
        emoticon_input = input("Please select a number based on what eyes you want (0-4): ")

    # Sets user_emoticon to the choice of eyes
    if int(emoticon_input) == 4:
        user_emoticon = random.choice(eyes)
    else:
        user_emoticon = eyes[int(emoticon_input)]

    # Prints the Nose Menu
    print("-----------------------")
    print("List of Nose")
    print("0 - ^")
    print("1 - O")
    print("2 - *")
    print("3 - Random Nose")

    # Resets emoticon_input to continue checking inputs.
    emoticon_input = None

    # Checks whether the number is numeric or within the specified range, and
    # asking continuously until given a proper input to exit the loop.
    # Ranges are -1 and 4 to inclujde 0 and 3 within the check
    while not verify.valid_input(emoticon_input, against_range = True, range_low = -1, range_high = 4):
        emoticon_input = input("Please select a number based on what nose you want (0-3): ")

    # Appends user_emoticon with the choice of nose.
    if int(emoticon_input) == 3:
        user_emoticon += random.choice(noses)
    else:
        user_emoticon += noses[int(emoticon_input)]

    # Prints the Mouths menu
    print("-----------------------")
    print("List of Mouths")
    print("0 - )")
    print("1 - (")
    print("2 - [")
    print("3 - ]")
    print("4 - Random Mouth")

    # Resets emoticon_input to continue checking inputs.
    emoticon_input = None

    # Checks whether the input is numeric or within the specified range, and
    # asking continuously until given a proper input to exit the loop.
    # Ranges are -1 and 5 to inclujde 0 and 4 within the check
    while not verify.valid_input(emoticon_input, against_range = True, range_low = -1, range_high = 5):
        emoticon_input = input("Please select a number based on what mouth you want (0-4): ")

    # Appends user_emoticon with the choice of mouth.
    if int(emoticon_input) == 4:
        user_emoticon += random.choice(mouths)
    else:
        user_emoticon += mouths[int(emoticon_input)]

    # Prints the emoticon
    print(user_emoticon)

user_input = None
# Prints the opening message
print_random_face_message()

# Checks whether the input is numeric and if the input is a positive integer,
# while asking continuously until given a proper input to exit the loop.
while not verify.valid_input(user_input, is_positive = True):
    user_input = str(round(float(input("How many faces would you like to print? "))))

# Prints the number of specified faces the user wished to see.
print_random_faces_input(int(user_input))
user_input = None
# Checks if the input is "Y" or "N" in order to continue. Both responses will
# exit the loop.
while not verify.valid_input(user_input, correct_inputs, against_list = True, against_string = True):
    user_input = input("Do you want another emoticon face? (Yes/No) ")

    # If the user input is "Y", it will print a random face.
    if user_input == "Yes":
        print(return_random_face())

# Resets the user input for further checks
user_input = None

# Checks if the input is "Y" or "N" in order to continue. Both responses will
# exit the loop.
while not verify.valid_input(user_input, correct_inputs, against_list = True, against_string = True):
    user_input = input("Would you like to create your own face? (Yes/No) ")

# While the users input is "Y", It will continue asking the user to make
# specific faces.
while user_input == "Yes":

    # If user_input is "Y", it will start print_specific_face().
    if user_input == "Yes":
        print_specific_face()
    user_input = None

    # Checks if the input is "Y" or "N" in order to continue. Both responses
    # will exit the loop.
    while not verify.valid_input(user_input, correct_inputs, against_list = True, against_string = True):
        user_input = input("Would you like to create another face? (Yes/No) ")
