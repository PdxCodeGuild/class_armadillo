import random
import time

# This python file creates a list of random emoticons.

run = True
count = 0
Checkin = False
# This main run loop validates input and checks for Vertical or Horizontal
# emoticons.
while run:
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
            print("I'm sorry that's not a valid response.")
    elif prompt == "N":
        print("Then why did you even come here?")
        exit()
    else:
        print("I'm sorry that's not a valid response.")

# These next 2 whiles check which type of face to make, and generate 5
# 1 at a time while iterating a counter up.
while count < 5:
    if vert == "H":
        rand_eyes = (":", "=", "8", ";", "|", "B")
        rand_nose = ("^", "-", "o", "")
        rand_mouth = ("D", ")", "(", "[", "]", "P", "S")
        eyes = random.choice(rand_eyes)
        nose = random.choice(rand_nose)
        mouth = random.choice(rand_mouth)
        print(f"{eyes}{nose}{mouth}")

    if vert == "V":
        rand_eyes = ("^", "@", "*", "-", "u", ">")
        rand_mouth = ("_", ".", "~", "-",)
        eyes = random.choice(rand_eyes)
        mouth = random.choice(rand_mouth)

        print(f"({eyes}{mouth}{eyes})")
    count += 1

# When the counter reaches 5, check if they want 5 more.
    if count >= 5:
        run = False
        while not run:
            response = input("would you like to make some more? (Y/N) ")
            if response == "Y":
                count = 0
                run = True
            elif response == "N":
                print("have a great day! =D")
                exit()
            else:
                print("I'm sorry that's not a valid response.")
