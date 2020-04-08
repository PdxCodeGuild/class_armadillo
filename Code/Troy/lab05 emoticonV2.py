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


#emoticon = ['=^p', ';-)', ':-{', '']

eyes = [';', ':', '=']
eyes = random.choice(eyes)
print(eyes, end='')

nose = ['^', '-', '*']
nose = random.choice(nose)
print(nose, end='')

mouth = [')', 'O', '}', '/', 'p']
mouth = random.choice(mouth)
print(mouth, end='')

# i = 0
# while i < 5:
#     eyes = random.choice(eyes)
#     nose = random.choice(nose)
#     mouth = random.choice(mouth)
#     print (eyes, nose, mouth, end='')
#     i += 1
