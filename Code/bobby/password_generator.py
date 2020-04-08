import string
import random
import time

letters = string.ascii_letters + string.punctuation + string.digits
password = ""

print("Welcome to Password Generator \n")
time.sleep(1)
password_length = int(input("How Many Charecters Would You Like?: "))

for letter in range (0, password_length):
    password += random.choice(letters)

print(password)