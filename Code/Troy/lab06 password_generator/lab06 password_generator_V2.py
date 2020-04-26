# Lab 06 Password Generator
# Troy Fitzgerald

'''Version 2
Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string.'''

# imports the module.
import random
import string

# assigns the functions to alphabet. 
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# has the user input the number of passwords to be generated.
number = input('How many passwords would you like to create? - ')
number = int(number)

# has the user input how long they  would like the password to be.
length = input('How long would you like your password to be? - ')
length = int(length)

print('\nHere are your password(s): ')

# runs loop over alphabet and chooses random characters based on the input assigned.
for p in range(number): 
    password = ''
    for c in range(length):
        password += random.choice(alphabet)
    print(password)
