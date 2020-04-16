# Lab 15 ROT cipher takes a string and returns a string where each letter is
# replaced by a letter 13 spots ahead of it in the alphabet like below.
# Version 2, allowed the user to determine the amount of rotations rather
# then just 13.

# | Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21
# |22|23|24|25|
# |---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--
# |--|--|--|--|
# | English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v
# | w| x| y| z|
# | ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i
# | j| k| l| m|


def rot13(input_message, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    out_message = []
    for letter in input_message:
        if letter == ' ':
            out_message.append(letter)
        else:
            character_index = alphabet.find(letter)
            if character_index < n:
                out_message.append(alphabet[character_index + n])
            else:
                out_message.append(alphabet[(character_index + n) % 26])
    return ''.join(out_message)


run = True
invalid = True

while run:
    while invalid:
        rotation = int(input("How many rotations do you want? "))
        user_input = input(f'''
    Enter a letter to receive
    its ROT {rotation} equivalent:

''')
        if user_input:
            print(user_input)
            invalid = False
        else:
            print("Please enter only letters.")

    print(rot13(user_input, rotation))

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
