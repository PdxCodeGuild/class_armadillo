# Lab 15 ROT cipher takes a string and returns a string where each letter is
# replaced by a letter 13 spots ahead of it in the alphabet like below.
# Version 2, allowed the user to determine the amount of rotations rather
# then just 13.
# Version 3 allows for inclusion of numbers or special characters.

# | Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21
# |22|23|24|25|
# |---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--
# |--|--|--|--|
# | English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v
# | w| x| y| z|
# | ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i
# | j| k| l| m|


# The actual ROT function.
def rot(input_message, n):
    # we'll iterate through this alphabet to identify the character we need
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # This blank list is where we append the characters to form final message
    output = []
    # iterate through the input_message
    for letter in input_message:
        # if it's a space, just put it into the message
        if letter not in alphabet and letter not in upper_alphabet:
            output.append(letter)
        elif letter in upper_alphabet:
            # if it's a letter, grab the index of where it is in alphabet
            character_index = upper_alphabet.find(letter)
            # if it's below the ROT value, add the value, append that letter
            if character_index < n:
                output.append(upper_alphabet[character_index + n])
            # else, modulus by len(alphabet) and append letter at that index
            else:
                output.append(upper_alphabet[(character_index + n) % 26])
        # do what we just did, but this time for lowercase
        else:
            character_index = alphabet.find(letter)
            if character_index < n:
                output.append(alphabet[character_index + n])
            else:
                output.append(alphabet[(character_index + n) % 26])
    # combine the output list to a string and return it.
    return ''.join(output)


def number_check(string):
    return any(letter.isdigit() for letter in string)


# global variables
run = True
invalid = True

# Main run loop
while run:
    # input validation using the number_check function.

    rotation = int(input("How many rotations do you want? "))
    user_input = input(f'''
    Enter a string of letters to receive
    its ROT {rotation} equivalent:

''')
    # call the main ROT function.
    print(rot(user_input, rotation))

    # Check if user needs more ROT.
    run = False
    while not run:
        checkin = input("Do you have more ROT to do? (Y/N) ")
        if checkin == "Y":
            run = True
            invalid = True
        elif checkin == "N":
            print("goodbye!")
            exit()
        else:
            print("please enter a valid response.")
