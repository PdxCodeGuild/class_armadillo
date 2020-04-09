import random 

import string 


letters = string.ascii_letters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation 
characters = upper + letters + digits + punctuation

num = int(input("how many characters do you want in your password? "))
nums = int(input("how many numbers do you want in your password? "))
upper = int(input("how many upper case letters do you want in your password? "))
lowers = int(input("how many lower case letters do you want in your password? "))
punc = int(input("how many special characters do you want in your password? "))
password = ''
for i in range(num):
    password += random.choice(characters)
print(password)


