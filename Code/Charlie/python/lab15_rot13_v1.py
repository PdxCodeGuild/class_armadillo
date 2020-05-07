#Lab 15 rot13 version one


def rotate_13_times(user_input):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    rotated_alphabet = alphabet[13:] + alphabet[:13]
    output = ''
    for char in user_input:
        index = alphabet.find(char)
        rotated_char = rotated_alphabet[index]
        output += rotated_char

    return output

user_input = input('what is your text? ')

print(rotate_13_times(user_input))






