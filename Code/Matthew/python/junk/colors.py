
# pychalk
from colorama import Fore, Back, Style
import time
import random

# colors

# https://pypi.org/project/colorama/
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

print(Fore.GREEN + ' look it\'s green')
print('still green')
print(Fore.RESET + 'its back to normal')

print(Fore.MAGENTA + Back.GREEN + 'omg my eyes')
print(Fore.RESET + Back.RESET)


colors = [Fore.MAGENTA, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.BLACK]
i = 0
while i < 1:
    color = random.choice(colors)
    print(color + 'random colors!')
    time.sleep(1)
    i += 1

time.sleep(2)

# ascii art
# https://www.asciiart.eu/
parakeets = r'''
         \\
 \\      (o>
 (o>     //\ 
_(()_____V_/_____
 ||      ||
         ||
'''
print(parakeets)



# print one letter at a time
message = 'hello welcome to my program'
i = 0
while i < len(message):
    print(message[i], end='', flush=True)
    time.sleep(0.1)
    i += 1



