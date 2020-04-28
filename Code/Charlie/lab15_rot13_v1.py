#Lab 15 rot13 version one


def rot13(text):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    rot_alphabet = alphabet[13:] + alphabet[:13]
    output = ''
    for char in text:
        index = alphabet.find(char)
        rot_char = rot_alphabet[index]
        output += rot_char

    return output

text = input('what is your text? ')

print(rot13(text))






