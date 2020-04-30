import string
import random
import time

print('\n' + '~'*43)
print('Welcome to the Lab 6 Password Generator...')
print('~'*43)

time.sleep(1.5)

# ascii letters, digits, special characters
letters = string.ascii_letters 
digits = string.digits
punctuation = string.punctuation

all_characters = letters + digits + punctuation # combined

user_length = int(input("\nHow long do you want your password? ")) # integer for desired length

time.sleep(0.5) # time delay

word = "" # empty string for estaablishing word
for x in range(user_length): # user input for password length
    word += random.choice(all_characters) # builds word
 
# random.shuffle can't accept string arguments, must convert to list
sel_characters = list(word)     # convert string into a list of characters
random.shuffle(sel_characters)  # shuffle the list of characters
password = ''.join(sel_characters)  # convert the list of characters back into a string
  
print("\nYour new password is:\n") # prints one letter at a time
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