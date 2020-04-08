
import random


eyes_list = ['.', '-', ';', '@', '^']
mouths_list = ['_', 'o']

for i in range(10):
    eyes = random.choice(eyes_list)
    mouth = random.choice(mouths_list)
    print('(' + eyes + mouth + eyes + ')')

# i = 0
# while i < 10:
#     ...
#     i += 1
