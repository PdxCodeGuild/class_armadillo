# Lab 6 Password Generator

import random
import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
punctuation = string.punctuation
digits = string.digits
letters = string.ascii_letters + string.digits + string.punctuation
password = ""
counter = 0
while counter < 10:
    counter += 1
    password += random.choice(letters)
print(password)