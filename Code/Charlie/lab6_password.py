import random
import string
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# letters = string.ascii_letters
# digits = string.digits
# punctuation = string.punctuation


b = input("How Many Letters: ")


# using (.isdigit) to make sure input is a number  
while not b.isdigit():

    # if input is not a number 
    b = input("You must enter a number: ")
 
 # input is a number 
else:
    b = int(b)

c = input("How many punctuation: ")


# using (.isdigit) to make sure input is a number  
while not c.isdigit():

    # if input is not a number 
    c = input("You must enter a number: ")
 
 # input is a number 
else:
    c = int(c)


password = " "
alphabet = string.ascii_letters + string.digits + string.punctuation

letters = string.ascii_letters
for i in range(b):
    password += random.choice(letters)

puncs = string.punctuation
for i in range(c):
    password += random.choice(puncs)

print(password)