import random
import string

# ask user how many letters he wants in his password
b = input("How many letters do you want in your password?: ")


# using (.isdigit) to make sure input is a number  
while not b.isdigit():

    # if input is not a number 
    b = input("You must enter a number: ")
 
 # input is a number 
else:
    b = int(b)

c = input("How many special characters?: ")


# using (.isdigit) to make sure input is a number  
while not c.isdigit():

    # if input is not a number 
    c = input("You must enter a number: ")
 
 # input is a number 
else:
    c = int(c)

# variable password is = to open '' so we can put our password as a string
password = " "
alphabet = string.ascii_letters + string.digits + string.punctuation

letters = string.ascii_letters

for i in range(b):
    password += random.choice(letters)

puncs = string.punctuation
for i in range(c):
    password += random.choice(puncs)

print(password)