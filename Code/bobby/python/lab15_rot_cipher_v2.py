# I imported string so I wouldn't have to hard code the alphabet into the program
import string

# I am using the def function to list my paramaters to pull from later in the program
def rot13(text, ceaser):

    # For the alphabet I pulled ascii letters from string in order to use both upper and lowercase letters in the cipher
    alphabet = string.ascii_letters

    # This line is just the shifting alphabet string starting at the 14th letter (n) and ending at the 13th letter (m)
    rot_alphabet = alphabet[13:] + alphabet[:13]

    # This is the output string and loop
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
    # User inerface input ouput
text = input("Enter your phrase or password to encript: ")
ceaser = int(input('what is the rotation amount? '))
print(rot13(text, ceaser))

