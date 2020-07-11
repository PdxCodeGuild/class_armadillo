import random
# from colorama import Fore, Back, Style
import time

# fruits = ['apple', 'bananas', 'pears']
# fruit = random.choice(fruits)
# print(fruit)


# print(fruits)
# random.shuffle(fruits)
# print(fruits)

# random_number = random.randint(0,100)
# print(random_number)

# # colors = ['green', 'yellow', 'blue', 'orange', 'red', 'pink', 'purple', 'white', 'black']

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# print('done')


# # 0 to 99(100 times)
# for i in range(100):
#     print(i)

# # 1 to 100 (100 times)
# for i in range(1, 101):
#     print(i)

#  1 to 100, even (50 times)
# for i in range(1, 101, 2):
#     print(i)



# colors = ['green', 'blue', 'orange']
# for color in colors:
#     print(color)


# if 'green' in colors:
#     pass


# msg = 'welcome to my program'
# i = 0
# while i < len(msg):
#     print(msg)
#     time.sleep(0.1)
#     i += 1



rps = ['rock', 'paper', 'scissors']

comp_choice = random.choice(rps)
while True:
    human_choice = input('Rock, paper, scissors? ').lower().strip()
    if human_choice in rps:
        break
    print('please enter a valid option')

print(human_choice)


