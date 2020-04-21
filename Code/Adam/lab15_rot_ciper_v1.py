"""

Lab 15: ROT Cipher
Versopn 1
Write a program that prompts the user for a string, and encodes it with ROT13. For each 
character, find the corresponding character, add it to an output string. Notice that there 
are 26 letters in the English language, so encryption is the same as decryption.

Index:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
English: a b c d e f g h i j k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
ROT+13:  n o p q r s t u v w x  y  z  a  b  c  d  e  f  g  h  i  j  k  l  m 

Version 2
Allow the user to input the amount of rotation used in the encryption. (ROTN)

"""
#starter code provided in class
# v1
import string

# prompt the user for a 'string'
# use .find to look up the index of a character in the alphabet
# use that same index to look up the corresponding character in the rotated alphabet
# add the rotated character to the output
# encode 'string' with ROT13
# For each character, .find the corresponding character
# add it to an 'output string'.

def rot13(text):
    for char in text:
        i = text.find(char)
        print(i)
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        rot13 = "nopqrstuvwxyzabcdefghijklm"

        # print(char)

print(rot13('hello')) # uryyb

# def rot13(text):
#     for i in range(len()):
#         user_string = input("Enter a message to be encoded.")
#         print(f"You entered: {user_string}") # for testing

         
#         print(string.ascii_lowercase) # for testing

#         rot_alphabet = alphabet[13:] + alphabet[:13]    #   nopqrstuvwxyzabcdefghijklm
#         print(rot_alphabet)
#         index = alphabet.index(char)
#         print(index) # for testing                    
    
#         char = 'j'
#         print(char) # for testing
#         #output_string =

# print(rot13('hello')) # uryyb
# print(index)
# print(rot_alphabet[index])
