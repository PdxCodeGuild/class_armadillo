"""
Lab 6: Password Generator

Let's generate a password of length n using a while loop and random.choice, this 
will be a string of random characters, e.g. a62xB95. Hint: random.choice can be 
used to pick a character out of a string, as well as an element out of a list.


Concepts Covered

input, print
looping
random.choice
the 'sting builder pattern'

Version 2

Allow the user to enter the value of n, remember to convert its type to an int, 
as input returns a string.


"""
import random
import string

# will need a large assortment of characters to draw on.
everything = string.ascii_letters + string.digits + string.punctuation


n = input('How many characters would you like in your password? ') # user chooses the length of the password
n = int(n) # n is converted to an integer 
i = 0
password = '' # each loop will add a character to password

# generate a string of random characters of length n using a while loop and random.choice
while i < n:
    password += random.choice(everything) # pick a random char from everthing
    i += 1 # add 1 to i

print(password) # when the i is equal to n the loop ends and password is printed
# print(len(password)) # test if password is right length


