"""
Lab 5: generate emoticons
"""

import random


# i = 0
# while i < 10:
#
#     list_eyes = [':', '=', ';']
#     list_noses = ['', '-', '\'', '^', '+']
#     list_mouths = [')', ']', '|', '/', '\\', 'D', 'P', '3']
#
#     eyes = random.choice(list_eyes)
#     nose = random.choice(list_noses)
#     mouth = random.choice(list_mouths)
#
#     emoticon = eyes + nose + mouth
#     print(emoticon)
#
#     i += 1


def create_emoticon():

    list_eyes = [':', '=', ';']
    list_noses = ['', '-', '\'', '^', '+']
    list_mouths = [')', ']', '|', '/', '\\', 'D', 'P', '3']

    eyes = random.choice(list_eyes)
    nose = random.choice(list_noses)
    mouth = random.choice(list_mouths)

    emoticon = eyes + nose + mouth

    return emoticon


for i in range(10):
    print(create_emoticon())
