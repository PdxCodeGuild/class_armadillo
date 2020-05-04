"""
Think Python Notes
"""
import random
import math
import time
import string


# person = input('Enter a person: ')

# # the input is initially a string
# # adjectives = input('Enter two adjectives seperated by a comma. ')
# adjectives = 'motivated,discouraged' # for testing
# print(adjectives) # is 1 string
# print(type(adjectives)) 


# # the input is converted to a list
# adjectives = adjectives.split(',')
# print(adjectives) # is now a list containing 2 strings
# print(type(adjectives)) 


# # will print the word in adjectives with the coresponding index  
# print(adjectives[0]) # prints 
# print(adjectives[1])

# adjective1, adjective2 = input('Enter two adjectives, seperated by a coma: ').split(',')

# print(adjective1, adjective2)

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

colors = [Fore.BLUE, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.CYAN, Fore.WHITE, Fore.MAGENTA]
eye_list = ['◕','♡','◡','˘','μ','•','￢','눈','--','~','个','±','×','x','☆','◣','◢','◎','ಠ']
mouth_list = ['‿', '﹏', '‸','-','ロ']
hands_list = ['凸','っ','ψ','ノ','／','＼','╮','╭','ლ','w','⊂','⊃']
color = random.choice(colors)
eyes = random.choice(eye_list)
mouth = random.choice(mouth_list)
hands = random.choice(hands_list)
emoticon = str(f"{hands}({eyes}{mouth}{eyes}){hands}")
print(str(f"{hands}({eyes}{mouth}{eyes}){hands}"))