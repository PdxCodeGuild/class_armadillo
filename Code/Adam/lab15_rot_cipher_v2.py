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



n = input('How many rotations in encryption? ')
n = int(n)

english = list(string.ascii_lowercase)
# print(english) # abcdefghijklmnopqrstuvwxyz
# print(english.index('a')) # a = 0

rot_n = english[n:] + english[:n]
print(rot_n) # nopqrstuvwxyzabcdefghijklm
# print(rot_n[0]) # 0 = n


# Start by asking the user for a string.
text_to_encode = input('Please enter text to encode. ').lower().strip()
# text_to_encode = 'hello' # test input
text_to_encode = list(text_to_encode)
# print(english.index('h'))  # the index of h is 7 in english list


# for char in text_to_encode:
indices = [english.index(char) for char in text_to_encode] # find index of that character in english
# print(indices) # test input prints [7, 4, 11, 11, 14] 

rot_13_encoded = [rot_n[i] for i in indices] # find the character with corresponding index in rot_n

output = ''.join(rot_13_encoded) # add the rot_n character to string

print(output) # print the string
