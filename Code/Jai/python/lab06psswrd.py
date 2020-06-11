import random 

import string 


letters = string.ascii_letters
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation 
characters = upper + letters + digits + punctuation

num = int(input("how many characters do you want in your password? "))
password = ''
for i in range(num):
    password += random.choice(characters)
print(password)


