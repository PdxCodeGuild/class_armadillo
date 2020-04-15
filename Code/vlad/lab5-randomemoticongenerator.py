#Lab 5: Random Emoticon Generator Version 1, Version 2, and Version 3 


# Define a list of eyes
# Define a list of noses
# Define a list of mouths
# Randomly pick a set of eyes
# Randomly pick a nose
# Randomly pick a mouth
# Assemble and display the emoticon



import random

eyes = [':', '=', ';']
noses = ["-", 'c', '^']
mouths = ["]", "}", ">", ")"]



i = 0
while i < 5:
    nose = random.choice(noses)
    eye = random.choice(eyes)
    mouth = random.choice(mouths)

    face = eye + nose + mouth

    print(face)

    i += 1



