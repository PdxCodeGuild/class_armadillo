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


char = 0


english = string.ascii_lowercase 
# print(english)

rot_13 = english[13:] + english[:13] 
# print(rot_13)

output = ''


# Start by asking the user for a string.
text_to_encode = input('Please enter text to encode. ')
text_to_encode = text_to_encode.lower()
# print(text_to_encode)
# print(rot_13[index])


#2. for each character, find the corresponding character 
for char in text_to_encode:
  index = char.index()
  print(index)


# print(index)
  #3. add it to an output string. (ill add it to a dictionary)







# End with output of encoded message
print(output)