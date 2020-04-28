#Lab 15: ROT Cipher Version 1




alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#index =    ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
#rot13 =    ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
rot13 = alphabet[13:] + alphabet[:13] # this is call slice  - this line is doing the same thing that line is doing 
#print(rot13) # ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
user_input = input('Enter any word: ')
word = " " #'uryyb'
# print(alphabet.index('c'))
# print(rot13[4])
for letter in user_input:  
    index_letter = alphabet.index(letter) # .index function searches the list alphabet for the letter, and returns letters index. .INDEX will return the number 
    word += rot13[index_letter]
    print(index_letter)
    print(rot13[index_letter])
print(word)
"""
Enter any word: hello
7
u
4
r
11
y
11
y
14
b
uryyb
"""

# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m


# v1
# def rot13(text):
#   ...
# ​
# print(rot13('hello')) # uryyb
# ​
# # v2
# ​
# def rotn(text, n):
#   ...
# ​
# print(rotn('hello', 13)) # uryyb
# ​
# ​
# # option 1
# # use .find to look up the index of a character in the alphabet
# # use that same index to look up the corresponding character in the rotated alphabet
# # add the rotated character to the output
# char = 'j'
# #           0123456789
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# #           nopqrstuvwxyzabcdefghijklm
# rot_alphabet = alphabet[13:] + alphabet[:13]
# print(rot_alphabet)
# index = alphabet.index(char)
# print(index)
# print(rot_alphabet[index])

# def rot13_v1(text):
#   alphabet = 'abcdefghijklmnopqrstuvwxyz'
#   rot_alphabet = alphabet[13:] + alphabet[:13]
#   rot_alphabet = 'nopqrstuvwxyzabcdefghijklm'

# ​
# # option 2
# # use .find to look up the index of a character in the alphabet
# # add 13 to the index, and mod it so it wraps back around
# # e.g. the index of 'r' is 18
# # (18 + 13)%26 == 5
# ​
# ​
# # option 3
# # use ord to find the ascii code of a character
# # subtract 97 so the sequence starts at 0
# # http://www.asciitable.com/
# print(ord('a')) # 97
# print(ord('b')) # 98
# ​
# ​
# ​
# # option 4
# # hard-code a dictionary, use it to look up the rotated character
# {'a': 'n', 'b': 'o', 'c': 'p'}
# ​
# ​
# # option 5
# # generate a dictionary?

# import string

# def rot13(text):
# #   ...
# # ​
# # print(rot13('hello')) # uryyb

# char = 'j'
# #           0123456789
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# #           nopqrstuvwxyzabcdefghijklm
# rot_alphabet = alphabet[13:] + alphabet[:13]
# print(rot_alphabet)
# index = alphabet.index(char)
# print(index)
# print(rot_alphabet[index])


###############################################################################################
"""
# v1
​
def rot13(text):
​
  # loop over the character
  # for char in text:
  #   print(char)
​
​
  #           0123456789...
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  char = 'h'
​
  # find vs index =======================
  # print(alphabet.find(char)) # 7
  # print(alphabet.index(char)) # 7
  # print(alphabet.find('!')) # -1
  # print(alphabet.index('!')) # crash
​
  # use .find to look up the index of the character in the alphabet
  index = alphabet.find(char)
  rotated_alphabet = 'nopqrstuv...'
  # use that index in the rotated alphabet to get the corresponding rotated character
  rotated_char = rotated_alphabet[index]
  print(rotated_char) # u
  
  # 'string builder pattern'
  # s = ''
  # for fruit in ['apples', 'bananas', 'pears']:
  #   s += fruit + '! '
  # print(s)
​
  # return output_string
​
​
​
def rot13_fancy(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  char = 's'
  index = alphabet.find(char)
  index += 13
  index %= len(alphabet)
  print(alphabet[index])
  
​
# print(rot13_fancy('hello')) # uryyb
​
​
​
# v2
​
def rotn(text, n):
  ...
​
print(rotn('hello', 13)) # uryyb
print(rotn('hello', 2)) # jgnnq
print(rotn('jgnnq', -2)) # hello
​
text = input('what is your text?')
n = int(input('what is the rotation amount? '))
print(rotn(text, n))
"""
#########################################################################################################################


