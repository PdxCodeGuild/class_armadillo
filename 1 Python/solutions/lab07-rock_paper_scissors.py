"""
Lab 7: play rock-paper-scissors with the computer
"""

import random

rps = ['rock', 'paper', 'scissors'] #list of possible options



# def find_in_list(elements, element):
#     for i in range(len(elements)):
#         if element == elements[i]:
#             return i
#     return -1


while True:
    user_choice = input('rock, paper, or scissors? ').lower()
    # if user_choice == 'rock' or user_choice == 'paper' or user_choice == 'scissors':
    if user_choice in rps:
        break

print('user choice: ' + user_choice)

comp_choice = random.choice(rps)
print('computer choice: ' + comp_choice)

# rock - paper
# rock - scissors
# paper - rock
# paper - scissors
# scissors - rock
# scissors - paper

# if user_choice == comp_choice:
#     print('tie!')
# elif user_choice == 'rock' and comp_choice == 'paper':
#     print('computer wins!')
# elif user_choice == 'rock' and comp_choice == 'scissors':
#     print('user wins!')
# elif user_choice == 'paper' and comp_choice == 'rock':
#     print('user wins!')
# elif user_choice == 'paper' and comp_choice == 'scissors':
#     print('computer wins!')
# elif user_choice == 'scissors' and comp_choice == 'rock':
#     print('computer wins!')
# elif user_choice == 'scissors' and comp_choice == 'paper':
#     print('user wins!')
#


user_choice = rps.index(user_choice)
comp_choice = rps.index(comp_choice)


#  0       1       2
# rock, paper, scissors







if user_choice == comp_choice:
    print('tie')
elif (user_choice + 1)%3 == comp_choice:
    print('computer won')
else:
    print('user won')





# first one is the user choice
# second is the computer choice
# rps = {
#     'rock': {
#         'rock': 'tie',
#         'paper': 'computer wins',
#         'scissors': 'user wins'
#     },
#     'paper': {
#
#     }
# }
# user_choice = 'rock'
# computer_choice = 'scissors'
# print(rps[user_choice][computer_choice])
# print(rps['rock']['scissors'])


