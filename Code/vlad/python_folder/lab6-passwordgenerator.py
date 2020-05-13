#Lab 6: Password Generator Version 1 and Version 2 

# Version 1
# Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters, e.g. a62xB95. Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

# Concepts Covered
# input, print
# looping
# random.choice
# the 'sting builder pattern'

# Version  2 
# Allow the user to enter the value of n, remember to
#  convert its type to an int, as input returns a string.

import random  # contain function and choices to randomaze 
import string  # contain function and choices to randomaze 

#lower = string.ascii_lowercase  # the .dot will go inside the string module
#upper = string.ascii_uppercase  # the .dot will go inside the string module

letters = string.ascii_letters
digits = string.digits
punctuations = string.punctuation
letters_input = int(input('How many letters do you want: '))
digits_input = int(input('How many digits do you want: '))
punctuation_input = int(input('How many Puncuations do you want: '))
word = []

for i in range(letters_input):
    word.append(random.choice(letters))
for i in range(digits_input):
    word.append(random.choice(digits))
for i in range(punctuation_input):
    word.append(random.choice(punctuations))
# print(lower + upper)
# print(letters)
# exit() this portion will stop the code here and wont allow anything below to run it can be used for testing the code

#user = int(input("Enter a password length: "))  # you have to enter a number and then the generator will create a password for you. 
#word = ""  # different way to write it word = str() 

#print(list(range(user)))

#for i in range(user):
   #print(f"{i=}")  print the value of i for each iteration each that (pass through) the for loop
 #   word += random.choice(letters)  # other way to write this line is:  word = word + random.choice(letters)
#
#word.shuffle() st
random.shuffle(word)
print(''.join(word))



