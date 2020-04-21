"""
Lab 5: Random Emoticon Generator

Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

1. Define a list of eyes
2. Define a list of noses
3. Define a list of mouths
4. Randomly pick a set of eyes
5. Randomly pick a nose
6. Randomly pick a mouth
7. Assemble and display the emoticon

"""
import time
import random

from colorama import Fore

colors = [Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.CYAN, Fore.WHITE, Fore.MAGENTA]
eye_list = ["◕","♡","◡","˘","μ","•","￢","눈","--","~","个","±","×","x","☆","◣","◢","◎","ಠ"]
#nose_list = ["▽","ω","_"]
mouth_list = ["‿", "﹏", "‸","-","ロ"]
hands_list = ["凸","っ","ψ","ノ","／","＼","╮","╭","ლ","w","⊂","⊃"]

print("Welcome to the Random Emoticon Generator!")

#while_loop
i = 0
while i < 4:
    color = random.choice(colors)
    eyes = random.choice(eye_list)
    mouth = random.choice(mouth_list)
    hands = random.choice(hands_list)
    emoticon = str(f"{hands}({eyes}{mouth}{eyes}){hands}")
    print(color + emoticon)
    time.sleep(1)
    i += 1

