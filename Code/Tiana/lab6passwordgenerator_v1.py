# Lab 6 Password Generator Version 1

#importing modules to be able to use random and string
import random
import string

#Assigning strings to variables
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
punctuation = string.punctuation
digits = string.digits
letters = string.ascii_letters + string.digits + string.punctuation

#Initializing the variable for counter and password so they can be used later 
password = ""
counter = 0

#Looping until the password is not less than 10
while counter < 10:
    counter += 1
    password += random.choice(letters)
print('The password is: ' + password )