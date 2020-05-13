#Lab 6 Password Generator Version 2

#Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string

#importing modules to use random and string
import random
import string


#Convert the user input to a int
n = int(input('How many characters do you want your password to be? '))

#assigning strings to variables
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
punctuation = string.punctuation
digits = string.digits
letters = string.ascii_letters + string.digits + string.punctuation

#Initializing variables
password = ""
counter = 0

#Add a character everytime the loop runs to create the password according to the user's input #
while counter <n:
    counter += 1
    password += random.choice(letters)
print(f"Your password is: {password}. ")