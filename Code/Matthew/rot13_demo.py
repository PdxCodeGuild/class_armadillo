


# v1

def rot13(text):
  ...

print(rot13('hello')) # uryyb

# v2

def rotn(text, n):
  ...

print(rotn('hello', 13)) # uryyb


# option 1
# use .find to look up the index of a character in the alphabet
# use that same index to look up the corresponding character in the rotated alphabet
# add the rotated character to the output
char = 'j'
#           0123456789
alphabet = 'abcdefghijklmnopqrstuvwxyz'
#           nopqrstuvwxyzabcdefghijklm
rot_alphabet = alphabet[13:] + alphabet[:13]
print(rot_alphabet)
index = alphabet.index(char)
print(index)
print(rot_alphabet[index])

# option 2
# use .find to look up the index of a character in the alphabet
# add 13 to the index, and mod it so it wraps back around
# e.g. the index of 'r' is 18
# (18 + 13)%26 == 5


# option 3
# use ord to find the ascii code of a character
# subtract 97 so the sequence starts at 0
# http://www.asciitable.com/
print(ord('a')) # 97
print(ord('b')) # 98



# option 4
# hard-code a dictionary, use it to look up the rotated character
{'a': 'n', 'b': 'o', 'c': 'p'}


# option 5
# generate a dictionary?


