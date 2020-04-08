from colorama import Fore
import random
import time


amount = 0

while True:
    prompt = input("Do you want to know how you're feeling today? (Y/N) ")
    if prompt == "Y":
        print("I'll give you 5 options to pick from!")
        time.sleep(1)
        break
    elif prompt == "N":
        print("Then why did you even come here?")
        exit()
    else:
        print("I'm sorry that's not a valid response.")

while prompt == "Y" and amount < 5:
    randEyes = (":", "=", "8", ";", "|", "B")
    randNose = ("^", "-", "")
    randMouth = ("D", ")", "(", "[", "]", "P", "S")
    eyes = random.choice(randEyes)
    nose = random.choice(randNose)
    mouth = random.choice(randMouth)

    print(f"{eyes}{nose}{mouth}")
    amount += 1
