'''Let's generate a password of length n using a while loop and random.choice, 
this will be a string of random characters.

Hint: random.choice can be used to pick a character out of a string, as well as 
an element out of a list.

Concepts Covered
input, print
looping
random.choice
the 'sting builder pattern'
Version 2
Allow the user to enter the value of n, remember to convert its type, as input returns a string.'''

# imports the module.
import random
import time
import string

# assigns the functions to alphabet. 
alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# prints the  below strings
print('Please make a password.  It should be 10 characters long. ')

input('I will make a password using random choices. Press enter to get your password... ')

# runs loop over alphabet and chooses random characters based on the input assigned. 
for i in range(10):
    print(random.choice(alphabet), end= '')






