"""
Lab 5: Random Emoticon Generator ==============================================

Let's generate emoticons by assembling a randomly choosing a set of eyes, a 
nose, and a mouth. Examples of emoticons are :-D =^P and :\. You can view a long 
list on wikipedia.

1. Define a list of eyes
2. Define a list of noses
3. Define a list of mouths
4. Randomly pick a set of eyes
5. Randomly pick a nose
6. Randomly pick a mouth
7. Use concatenation to combine them and display the emoticon

Example output:

:-P

Version 2
- Use a while loop to generate 5 emoticons.

Version 3
- Randomly generate vertical emoticons like ^_^ (-_-), [*.*]

"""

import time
import random

from colorama import Fore


# V3 - Randomly generate vertical emoticons
def gen_emote():
    # define lists for eyes, nose, mouth
    colors = [Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.CYAN, Fore.WHITE, Fore.MAGENTA]
    eye_list = ['◕','♡','◡','˘','μ','•','￢','눈','--','~','个','±','×','x','☆','◣','◢','◎','ಠ']
    mouth_list = ['‿', '﹏', '‸','-','ロ']
    hands_list = ['凸','っ','ψ','ノ','／','＼','╮','╭','ლ','w','⊂','⊃']
    color = random.choice(colors)
    eyes = random.choice(eye_list)
    mouth = random.choice(mouth_list)
    hands = random.choice(hands_list)
    emoticon = str(f"{hands}({eyes}{mouth}{eyes}){hands}")
    print(color + emoticon)

print(f'Welcome to the Random Emoticon Generator!')


how_many = input('How many emoticons would you like to generate? ')
how_many = int(how_many)
# V2 - Use a while loop to generate 5 emoticons. 
# user can generate as many as they'd like
i = 0
while i < how_many:
    gen_emote()
    time.sleep(1)
    i += 1