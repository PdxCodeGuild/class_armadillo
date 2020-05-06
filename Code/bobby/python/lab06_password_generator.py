#My Lab 06 Random Password Generator

# I imported the string modual so I can add the ascii_letter, punctuation, 
# and digits to the program so I wouldn't have to hard code everything.
# Import random is to randomly generate the password.
# Import time is being used to give the user a chance to read a statment before the next one shows on screen.
import string
import random
import time

# I am using letters is my string name to pull up the information within the moduals.
# Password is my string name used in my for loop to call on the random modual to generate the password
letters = string.ascii_letters + string.punctuation + string.digits
password = ""

# Greetings message
print("Welcome to Password Generator \n")
time.sleep(1)

# This section is where the program askes the user to input how long they would like their password to be.
password_length = int(input("How Many Charecters Would You Like?: "))

# The for loop is the part of the progeram that takes what the user entered and generates the Random Pass word.
for letter in range (0, password_length):
    password += random.choice(letters)
# This is what the generated password
print(password)