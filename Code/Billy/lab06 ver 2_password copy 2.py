import string
import random
import time

print('\n' + '~'*43)
print('Welcome to the Lab 6 Password Generator...')
print('~'*43)

time.sleep(1.5)

letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

all_characters = letters + digits + punctuation

user_length = int(input("\nHow long do you want your password? "))

time.sleep(0.5)

word = ""
for x in range(user_length):
    word += random.choice(all_characters)
 
# random.shuffle can't accept string arguments, must convert to list
sel_characters = list(word)     # convert string into a list of characters
random.shuffle(sel_characters)  # shuffle the list of characters
password = ''.join(sel_characters)  # convert the list of characters back into a string
  
print("\nYour new password is:\n")
time.sleep(1)
password_msg = password + '\n\n'
i = 0
while i < len(password_msg):
    print(password_msg[i], end='', flush=True)
    time.sleep(0.1)
    i += 1
        
    



'''
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered
input, print
looping
random.choice
the 'sting builder pattern'

Version 2
Allow the user to enter the value of n, remember to convert its type, as input returns a string.
'''