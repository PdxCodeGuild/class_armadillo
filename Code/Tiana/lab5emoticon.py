#Lab 5 Emoticons

import random

#Define a list of face parts
eyes = ['n', '=', '@', '^', '@', '^', '=','!', 'n', 'o', '0']
mouths = ['______', '.']

#Randomly pick parts for emoticons
eyes2 = random.choice(eyes)
mouths2 = random.choice(mouths)

#assemble and display the emoticon
face = eyes2 + mouths2 + eyes2
print('(' + eyes2 + mouths2 + eyes2 + ')')

#generate 5 random emoticons.
i = 0
while i < 5:
    eyes2 = random.choice(eyes)
    mouths2 = random.choice(mouths)
    print('(' + eyes2 + mouths2 + eyes2 + ')')
    

    i += 1
