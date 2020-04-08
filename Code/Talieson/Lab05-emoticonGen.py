from colorama import Fore
import random
import time


amount = 0

while True:
    prompt = input("Do you want to know how you're feeling today? (Y/N) ")
    if prompt == "Y":
        vert = input("Do you want vertical or horizonal emoticons? (V/H) ")
        if vert == "H":
            print("I'll give you 5 options to pick from!")
            time.sleep(1)
            break
        elif vert == "V":
            print("I'll give you 5 options to pick from!")
            time.sleep(1)
            break
        else:
            prompt = False
            print("I'm sorry that's not a valid resposne.")
    elif prompt == "N":
        print("Then why did you even come here?")
        exit()
    else:
        print("I'm sorry that's not a valid response.")

while prompt == "Y" and amount < 5 and vert == "H":
    randEyes = (":", "=", "8", ";", "|", "B")
    randNose = ("^", "-", "")
    randMouth = ("D", ")", "(", "[", "]", "P", "S")
    eyes = random.choice(randEyes)
    nose = random.choice(randNose)
    mouth = random.choice(randMouth)

    print(f"{eyes}{nose}{mouth}")
    amount += 1

while prompt == "Y" and amount < 5 and vert == "V":
    randEyes = ("^", "@", "*", "-")
    randMouth = ("_", ".", "~")
    eyes = random.choice(randEyes)
    mouth = random.choice(randMouth)

    print(f"{eyes}{mouth}{eyes}")
    amount += 1
