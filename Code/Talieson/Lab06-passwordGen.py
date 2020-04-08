import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase
digits = string.digits
specials = string.punctuation
randAlphabet = characters + digits + specials

while True:
    fullRand = input("Want a random password? (Y/N): ")
    if fullRand == "Y" or "N":
        break
    else:
        print("Not a valid input. ")

if fullRand == "Y":
    length = random.randint(7, 16)
    password = "".join(random.sample(randAlphabet, length))
    print("Here is your new password: " + password)

if fullRand == "N":
    letters = int(input("How many characters should be letters? "))
    password = "".join(random.sample(characters, letters))

    numbers = int(input("How many characters should be numbers? "))
    password += "".join(random.sample(digits, numbers))

    punctuation = int(input("How many special characters should there be? "))
    password + "".join(random.sample(specials, punctuation))

    print("Here is your new password: ")
    print(password)
