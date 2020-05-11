# Lab 06


import string
import random


#Keeps the question going
while True:
    # this is a yes/no question for user
    user = input("can you help me generate a password with random characters? y/n: ")

    # this line let's you specifically pick a number
    digits = int(input("I would like you to choose a number between 5 and 35: "))

    # Returns all lowercase letters, uppercase letters, and digits
    stuff = (string.ascii_lowercase + string.ascii_uppercase + string.digits)

    # empty string joined with random.sample beginning with stuff for the amount of digits
    cell_password = "".join(random.sample(stuff, digits))

    print (cell_password)