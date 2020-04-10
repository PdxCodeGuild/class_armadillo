

Let's generate a password of length n using a while loop and random.choice, 
this will be a string of random characters, e.g. a62xB95. Hint: random.choice 
can be used to pick a character out of a string, as well as an element out of a 
list.

Concepts Covered:
input, print
looping
random.choice
the 'sting builder pattern'

Version 2
Allow the user to enter the value of n, remember to convert its type 
to an int, as input returns a string.

Version 3 (optional)
Ask the user for how many lowercase letters, uppercase letters,
 numbers, and special characters they'd like in their password. 
 You do not want the pieces in order (e.g. 3 lowercase letters 
 followed by 3 uppercase letters...). You can use list(password_string) 
 or password_string.split('') to convert the string to a list, 
 random.shuffle(password_list) to shuffle it, and then ''.join(password_list) 
 to turn it back into a string.

random.randint(5, 15)

# import modules
import string
import random

user = input("can you help me generate a password with random characters? ")
print(user)

user = input("I would like you to choose a number between 5 and 15: ")
12

num = int(12)

print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)

letters = string.ascii_letters
print(letters)


import string
import random
user = input("can you help me generate a password with random characters? y/n")
digits = int(input("I would like you to choose a number between 5 and 15: "))
stuff = string.ascii_lowercase + string.ascii_uppercase + string.digits)
#we want to incorporate all these digits and these characters too
#choose number of digits that the user inputs
cell_password = "".join(random.sample(stuff, digits))
print (cell_password)






import string
import random
user = input("can you help me generate a password with random characters? y/n")
digits = int(input("I would like you to choose a number between 5 and 15: "))
stuff = string.ascii_lowercase + string.ascii_uppercase + string.digits)
#we want to incorporate all these digits and these characters too
#choose number of digits that the user inputs
cell_password = "".join(random.sample(stuff, digits))
print (cell_password)



import string
import random

user = input("can you help me generate a password with random characters? y/n")
digits = int(input("I would like you to choose a number between 5 and 15: "))
stuff = ("string.ascii_lowercase + string.ascii_uppercase + string.digits")
cell_password = "".join(random.sample(stuff, digits))
print (cell_password)