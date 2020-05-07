#version two of this lab allows the user to encode a given word and choose how many letter they would like to rotate the encoding:

import string 

alphabet = string.ascii_lowercase #import lower case letters

def rotn(text, number):
    rotn_cipher = '' #blank string
    for letter in text:  #iterates over each letter in a word
        if letter in alphabet:  #this condition for input within ascii_lowercase
            rotn_cipher += alphabet[(alphabet.find(letter) + number) % 26]  #finds index of letter within alphabet, adds rotation, modulus 26
        else: #condition for characters not within ascii_lowercase
            rotn_cipher += letter #adds new encoded letter to string
    return rotn_cipher  #creates new rotated word

print(rotn('hello', 2)) #text is hello, rotates 2 places   