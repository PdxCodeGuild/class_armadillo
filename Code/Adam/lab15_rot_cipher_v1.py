"""

Lab 15: ROT Cipher

Versopn 1 ==========================================================================
Write a program that prompts the user for a string, and encodes it with ROT13. For 
each character, find the corresponding character, add it to an output string. Notice 
that there are 26 letters in the English language, so encryption is the same as 
decryption.

Index:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
English: a b c d e f g h i j k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
ROT+13:  n o p q r s t u v w x  y  z  a  b  c  d  e  f  g  h  i  j  k  l  m 

"""


import string


#Version 1
def rot13(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot13_alphabet = alphabet[13:] + alphabet[:13]
    output = ''
    for char in text:
        index = alphabet.find(char) # use .find to look up the index of a character in the alphabet
        rot_char = rot13_alphabet[index] # use that same index to look up the corresponding character in the rotated alphabet
        output += rot_char # add the rotated character to the output
    return output


# print(rot13('hello')) #for testing


while True:
    encode = input('Would you like to encode a string of text? ')
    if encode == 'yes' or 'y':
        text = input("Please enter the text you'd like encoded. ") # prompt the user for a 'string'
        print(rot13(text))
    break

  