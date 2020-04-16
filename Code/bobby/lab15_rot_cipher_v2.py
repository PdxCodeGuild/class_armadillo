import string


def rot13(text, ceaser):
    
    alphabet = string.ascii_letters
    rot_alphabet = alphabet[13:] + alphabet[:13]
    cipher = ""
    for char in text:
        index = alphabet.index(char)
        cipher += rot_alphabet[index]
        if index == -1:
            cipher += char
        else:
            index += ceaser
            index %= len(alphabet)
            cipher += alphabet[index]
    return cipher
text = input("Enter your phrase or password to encript: ")
ceaser = int(input('what is the rotation amount? '))
print(rot13(text, ceaser))

