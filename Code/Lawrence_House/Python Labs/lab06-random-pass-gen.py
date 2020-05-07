import random
import string

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

user_choice = int(input('Gonna make a password for you. How many characters do you want? '))

print("\nAlright! Here you go! \n")

for i in range(user_choice):
    print(random.choice(alphabet), end=(" "))

