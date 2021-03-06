import string
import random
import time

print('\n' + '~'*43)
print('Welcome to the Lab 6 Password Generator...')
print('~'*43)

time.sleep(1.5)

# ascii letters, digits, special char
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

# user input for desired password parameters
user_uppercase = int(input("\nHow many upper case letters? "))
user_lowercase = int(input("How many lower case letters? "))
user_numbers = int(input("How many numbers? "))
user_punct = int(input("How many special characters? "))

time.sleep(0.5) # time delay

word = "" # establishes empty string for password

for n in range(user_uppercase): # uses input parameters to build password
    word += random.choice(upper)

for n in range(user_lowercase):
    word += random.choice(lower)

for n in range(user_numbers):
    word += random.choice(digits)

for n in range(user_punct):
    word += random.choice(punctuation)
  
# random.shuffle can't accept string arguments, must convert to list
characters = list(word)     # convert string into a list of characters
random.shuffle(characters)  # shuffle the list of characters
password = ''.join(characters)  # convert the list of characters back into a string
  
print("\nYour new password is:\n") # prints password
time.sleep(1)
password_msg = password + '\n\n'
i = 0
while i < len(password_msg):
    print(password_msg[i], end='', flush=True)
    time.sleep(0.1)
    i += 1
        
    







'''
Lab 6: Password Generator
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered
input, print
looping
random.choice
the 'sting builder pattern'
Version 2
Allow the user to enter the value of n, remember to convert its type, as input returns a string.

Version 3 (optional)
Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters 
they'd like in their password. Generate a password accordingly.
'''