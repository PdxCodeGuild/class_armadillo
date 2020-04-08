import random
import time

eyes = [';', ':', 'B', '=']
noses = ['-', '<', 'o', '^']
mouths = [']', ')', '3', 'D']

x = 0
while x < 5:

    random_eye = random.choice(eyes)
    random_nose = random.choice(noses)
    random_mouth = random.choice(mouths)
    emoticon  = random_eye + random_nose + random_mouth
    print(emoticon)
    x += 1


vert_eye = ["'", "^", "-", "*"]
vert_mouth = [".", "_", ]
cheek = ["(", "[", ")", "]"]

user = input("Would you like to see a verticle emoticon? Y/N:")
if user == 'Y':
    rv_cheek = random.choice(cheek)
    rv_eye = random.choice(vert_eye)
    rv_mouth = random.choice(vert_mouth)
    v_emoticon = rv_cheek + rv_eye + rv_mouth + rv_eye + rv_cheek 
    print(v_emoticon)
elif user == 'N':
    print('Adios!')

