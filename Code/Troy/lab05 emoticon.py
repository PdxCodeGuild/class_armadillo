"""Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth.

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon
import random

fruits = ['apple', 'banana', 'pineapple']
fruit = random.choice(fruits)
# print(fruit)"""

import random
import time
import colorama

#emoticon = ['eyes', 'nose', 'mouth']

eyes = ['>   <', '#   #', '"   "', '*   *']
eyes = random.choice(eyes)
print(eyes)

nose = ['  - ', '  \ ', '  b ', '  o ']
nose = random.choice(nose)
print(nose)

mouth = ['______', '(_______)', 'xxxxxxx', '\_____/']
mouth = random.choice(mouth)
print(mouth)
