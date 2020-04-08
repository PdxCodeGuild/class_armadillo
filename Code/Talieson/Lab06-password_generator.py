import random
import string

# Establishes the libraries we'll be pulling characters from
characters = string.ascii_lowercase + string.ascii_uppercase
digits = string.digits
specials = string.punctuation
rand_alphabet = characters + digits + specials

# Main loop
while True:
    # Check if the password should be fully randomized or not
    full_rand = input("Want a random password? (Y/N): ")
    if full_rand == "Y" or "N":
        break
    else:
        print("Not a valid input. ")

# If the password is suppose to be randomized, randomize length and characters
if full_rand == "Y":
    length = random.randint(7, 16)
    password = "".join(random.sample(rand_alphabet, length))
    print(f"Here is your new password: {password}")

# If not fully random, ask for # of each type of characters, join and randomize
if full_rand == "N":
    letters = int(input("How many characters should be letters? "))
    password = "".join(random.sample(characters, letters))

    numbers = int(input("How many characters should be numbers? "))
    password += "".join(random.sample(digits, numbers))

    punctuation = int(input("How many special characters should there be? "))
    password += "".join(random.sample(specials, punctuation))

# Password is still in order, need to shuffle, so convert to a list -> shuffle
    password_list = list(password)
    random.shuffle(password_list)
    password = "".join(password_list)

    print(f"Here is your new password: {password}")
