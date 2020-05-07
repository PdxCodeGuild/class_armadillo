# PDX Code Guild Fullstack Course
# Lab 15 ROT Cypher
# Samuel Purdy
# 4/16/2020

import string

# Used to define alphabet strings.
alphabet_upper = string.ascii_uppercase
alphabet_lower = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation

# Predifines rotated strings
rot_alphabet_upper = str()
rot_alphabet_lower = str()
rot_digits = str()
rot_punctuation = str()

def check_if_numeric(str1):
    # for each character in the string given, loop
    for char in str1:
        if not char.isnumeric():
            if char != "-":
                return False
    return True

# Initializing rotation as a string in order to check if it is numeric.
rotation = str()

# If the input is not a whole number, keep looping until a whole number is given.
while not len(rotation) > 0 or not check_if_numeric(rotation):
    rotation = input("What is the rotation? (Positive integer for left rotation, negative integer for right rotation.) ")

# Turns rotation from a string to an integer.
rotation = int(rotation)

# The rotated string is equal to the first slice of the rotation, plus the slice of rotation minus 
# the length of the string. This makes the string rotate around the number of times the user desired. 
# If the rotation is positive, it wrap around going left.
# If the rotation is negative, it will wrap going right instead. 
# Zero will do nothing.
if rotation > 0:
    rot_alphabet_upper = alphabet_upper[rotation:] + alphabet_upper[:rotation-len(alphabet_upper)]
    rot_alphabet_lower = alphabet_lower[rotation:] + alphabet_lower[:rotation-len(alphabet_lower)]
    rot_digits = digits[rotation:] + digits[:rotation-len(digits)]
    rot_punctuation = punctuation[rotation:] + punctuation[:rotation-len(punctuation)]
elif rotation < 0:
    rot_alphabet_upper = alphabet_upper[rotation:] + alphabet_upper[:rotation+len(alphabet_upper)]
    rot_alphabet_lower = alphabet_lower[rotation:] + alphabet_lower[:rotation+len(alphabet_lower)]
    rot_digits = digits[rotation:] + digits[:rotation+len(digits)]
    rot_punctuation = punctuation[rotation:] + punctuation[:rotation+len(punctuation)]
else:
    rot_alphabet_upper = alphabet_upper
    rot_alphabet_lower = alphabet_lower
    rot_digits = digits
    rot_punctuation = punctuation

# Gets the string the user wants to transform.
transform = input("What would you like to transform? ")

# This string will be equal to the string that is given though the characters will be rotated 
# depending on the rotation given.
new_string = str()

# For each index in string transform, loop.
for i in range(len(transform)):
    # If the character at transform[i] is found in alphabet_under, add a new rotated character 
    # from the index of alphabet_upper to rot_alphabet_upper.
    # This is the same for each of the following cases except the last, where if the character was 
    # not found in any of the parent strings, it is passed through to the new string.
    if alphabet_upper.find(transform[i]) > -1:
        new_string += rot_alphabet_upper[alphabet_upper.find(transform[i])]
    elif alphabet_lower.find(transform[i]) > -1:
        new_string += rot_alphabet_lower[alphabet_lower.find(transform[i])]
    elif digits.find(transform[i]) > -1:
        new_string += rot_digits[digits.find(transform[i])]
    elif punctuation.find(transform[i]) > -1:
        new_string += rot_punctuation[punctuation.find(transform[i])]
    else:
        new_string += transform[i]

# Prints the transformed string.
print(new_string)