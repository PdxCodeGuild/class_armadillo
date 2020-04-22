"""
Lab 6: Password Generator

Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters, e.g. a62xB95. Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.

Concepts Covered
-input, print
-looping
-random.choice
-the 'sting builder pattern'

"""

import time
import string
import random

alphabet =  string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

print('Welome to Password Generator!')

time.sleep(1)

#n is the length of the password and the upper bound
n = int(input('How long would you like the password to be? '))

i = 0

password = ''

#while loop
while i < n:
    password += random.choice(alphabet)
    i += 1
time.sleep(1)   
print(password)
