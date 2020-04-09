import string
import random

print("\n\n-----Password Generator-----\n")

def password_generator():
    i = 0
    keep_it_going = True
    possible_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password_length = input("enter the length of password you want: ")
    password_length = int(password_length)

    rando = []
    while i in range(password_length):
        rando.append(random.choice(possible_chars))
        i += 1
    rando_string = ''.join(rando)    
    print(rando_string)
password_generator()