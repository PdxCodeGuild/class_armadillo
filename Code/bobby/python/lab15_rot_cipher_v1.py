import string


def rot13(text, ceaser):
    
    alphabet = string.ascii_lowercase
    rot_alphabet = alphabet[13:] + alphabet[:13]
    cipher = ""
    for char in text:
        index = alphabet.index(char)
        cipher += rot_alphabet[index]
    return cipher
print(rot13("hello", 13))
