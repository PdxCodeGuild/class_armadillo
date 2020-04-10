#   Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

import random

#   Emote part lists

eye = [':', ';','=','8']

nose = ['^','-','o']

mouth = [')','(','O','3','D']

#   Randomizer

eyes = random.choice(eye)
nose = random.choice(nose)
mouth = random.choice(mouth)

#   Emote printer w/ while loop

emote = 0
while emote < 5:
    print(eyes,nose,mouth)
    emote += 1

