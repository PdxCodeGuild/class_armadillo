import string 

alphabet = string.ascii_lowercase #import lower case letters

def rotn(text, number):
    rotn_cipher = '' #blank string
    for letter in text:  #scans over each letter in a word
        if letter in alphabet:  #this condition for input within ascii_lowercase
            rotn_cipher += alphabet[(alphabet.find(letter) + number) % 26]  #finds index of letter within alphabet, adds rotation, modulus 26
        else: #condition for characters not within ascii_lowercase
            rotn_cipher += letter
    return rotn_cipher  #creates new rotated word

print(rotn('hello', 2))    