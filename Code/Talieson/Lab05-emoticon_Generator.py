from colorama import Fore
import random
import time

run = True
count = 0

while run:
    prompt = input("Do you want to know how you're feeling today? (Y/N) ")
    if prompt == "Y":
        vert = input("Do you want vertical or horizonal emoticons? (V/H) ")
        if vert == "H":
            print("I'll give you 5 options to pick from!")
            time.sleep(1)
            run = False
            break
        elif vert == "V":
            print("I'll give you 5 options to pick from!")
            time.sleep(1)
            run = False
            break
        else:
            prompt = False
            print("I'm sorry that's not a valid resposne.")
    elif prompt == "N":
        print("Then why did you even come here?")
        exit()
    else:
        print("I'm sorry that's not a valid response.")

while prompt == "Y" and count < 5 and vert == "H":
    rand_eyes = (":", "=", "8", ";", "|", "B")
    rand_nose = ("^", "-", "o", "")
    rand_mouth = ("D", ")", "(", "[", "]", "P", "S")
    eyes = random.choice(rand_eyes)
    nose = random.choice(rand_nose)
    mouth = random.choice(rand_mouth)

    print(f"{eyes}{nose}{mouth}")
    count += 1

while prompt == "Y" and count < 5 and vert == "V":
    rand_eyes = ("^", "@", "*", "-", "u", ">")
    rand_mouth = ("_", ".", "~", "-",)
    eyes = random.choice(rand_eyes)
    mouth = random.choice(rand_mouth)

    print(f"({eyes}{mouth}{eyes})")
    count += 1

if count >= 5 and not run:
    response = input('would you like to continue? (Y/N)')
    response = response == 'Y'
if response:
    count = 0
    run = True
