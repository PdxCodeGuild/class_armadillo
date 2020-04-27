# Lab 05 Emoticon
# Troy Fitzgerald


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

# imports the modules.
import random
import time
import colorama

# describes the list of eyes for the emoticon and prints them at random.
eyes = ['>   <', '#   #', '"   "', '*   *']
eyes = random.choice(eyes)
print(eyes)
# describes the list of noses for the emoticon and prints them at random.
nose = ['  - ', '  \ ', '  b ', '  o ']
nose = random.choice(nose)
print(nose)
# describes the list of mouths for the emoticon and prints them at random.
mouth = ['______', '(_______)', 'xxxxxxx', '\_____/']
mouth = random.choice(mouth)
print(mouth)
