


for i in range(10):
    print('x', end='')

quit()

import random

eyes_list = [':', ';', '=']
noses_list = ['^', 'o', '']
mouths_list = [')', ']', '}', 'D', 'P']

# for i in range(5):
#     eyes = random.choice(eyes_list)
#     nose = random.choice(noses_list)
#     mouth = random.choice(mouths_list)
#     emoticon = eyes + nose + mouth
#     print(emoticon)

num_emoticons = int(input('How many emoticons would you like? '))

i = 0
while i < num_emoticons:
    eyes = random.choice(eyes_list)
    nose = random.choice(noses_list)
    mouth = random.choice(mouths_list)
    emoticon = eyes + nose + mouth
    print(emoticon)
    i += 1





