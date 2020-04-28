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

Version 2 ==========================================================================
Allow the user to input the amount of rotation used in the encryption. (ROTN)

"""


import string


# Version 2
def rot_n(text, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rot_alphabet = alphabet[n:] + alphabet[:n]
    output = ''
    for char in text:
        index = alphabet.find(char) # use .find to look up the index of a character in the alphabet
        rot_char = rot_alphabet[index] # use that same index to look up the corresponding character in the rotated alphabet
        output += rot_char # add the rotated character to the output
    return output


print(rot_n('hello', 13)) #for testing

while True:
    encode = input('Would you like to encode a string of text? ')
    if encode == 'yes' or 'y':
        text = input("Please enter the text you'd like encoded. ") # prompt the user for a 'string'
        n = input('Please specify the number of rotations in the encryption. ') # allow the user to input the amount of rotation used in the encryption.
        n = int(n)
        # print(text)
        # print(n)
        print(rot_n(text, n))
    break
