import random


eyes = [':', '|', '8']
noses = ['^', '~', ']']
mouths = [']', '#', '*']
eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)
emoticon = eye + nose + mouth
print(f'here is your result:  {emoticon}')