import string
import random
import time

letters = string.ascii_letters + string.punctuation + string.digits
password = ""

print("Welcome to Password Generator \n")
time.sleep(1)
user = input(f"How Many Charecters Would You Like: {1,10}): ")

for letter in range (0,10):
    password += random.choice(letters)
    
print(password)