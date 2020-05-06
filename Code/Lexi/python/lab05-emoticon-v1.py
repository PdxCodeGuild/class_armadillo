# Lab 5: Random Emoticon Generator
# Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\. You can view a long list on wikipedia.

# Define a list of eyes
# Define a list of noses
# Define a list of mouths
# Randomly pick a set of eyes
# Randomly pick a nose
# Randomly pick a mouth
# Use concatenation to combine them and display the emoticon
import random

question = input("Want to see what you look like as an ASCII emoji?")

i = 0
while i < 5:
    i += 1
    eyes = [':', '|', '8']
    noses = ['^', '~', ']']
    mouths = [']', '#', '*']
    if question == 'yes':
        eye = random.choice(eyes)
        nose = random.choice(noses)
        mouth = random.choice(mouths)
        emoticon = eye + nose + mouth
        print(f'here is your result:  {emoticon}')
    else:
        break
        print("ok, come again")
