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

# imports the module.
import random

# describes the list of eyes for the emoticon and prints them at random.
eyes = [';', ':', '=']
eyes = random.choice(eyes)
#print(eyes, end='') - test print the eyes.

# describes the list of noses for the emoticon and prints them at random.
nose = ['^', '-', '*']
nose = random.choice(nose)
#print(nose, end='') - test print the nose.

# describes the list of mouths for the emoticon and prints them at random.
mouth = [')', 'O', '}', '/', 'p']
mouth = random.choice(mouth)
#print(mouth, end='') - test prints the mouth.

# runs a loop to print an emoticon on each line up to the input value.
i = 0
while i < 5:    
    print (eyes, nose, mouth)
    i += 1
