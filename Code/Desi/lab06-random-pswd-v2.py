import string
import random

user = input("can you help me generate a password with random characters? y/n")
digits = int(input("I would like you to choose a number between 5 and 15: "))
stuff = ("string.ascii_lowercase + string.ascii_uppercase + string.digits")
cell_password = "".join(random.sample(stuff, digits))
print (cell_password)