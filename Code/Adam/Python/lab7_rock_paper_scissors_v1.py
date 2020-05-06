"""
Lab 7: Rock Paper Scissors

Let's play rock-paper-scissors with the computer.

1. The computer will ask the user for their choice (rock, paper, scissors)
2. The computer will randomly choose rock, paper or scissors
3. Determine who won and tell the user

Let's list all the cases:

-rock vs rock (tie)
-rock vs paper
-rock vs scissors
-paper vs rock
-paper vs paper (tie)
-paper vs scissors
-scissors vs rock
-scissors vs paper
-scissors vs scissors (tie)

"""

import random
import time

options = ['rock', 'paper', 'scissor']

print('Welcome to Rock, Paper, Scissors! ') 

time.sleep(1)

print('3...')

time.sleep(.5)

print('2...')

time.sleep(.5)

print('1...')

time.sleep(.5)

print('SHOOT!')

time.sleep(.5)

player_shoots = input('rock, paper, or scissor? ')

comp_shoots = random.choice(options)

time.sleep(1)

print(f'computer:{comp_shoots} / player:{player_shoots}')

time.sleep(1)

if player_shoots == comp_shoots:
    print("It's a tie. ")
elif player_shoots == "rock" and comp_shoots == "paper":
    print("Paper wraps rock; you lose! ")
elif player_shoots == "rock" and comp_shoots == "scissor":
    print("Rock breaks scissors; you win! ")
elif player_shoots == "paper" and comp_shoots == "rock":
    print("Paper wraps rock; you win!")
elif player_shoots == "paper" and comp_shoots == "scissor":
    print("Scissor cuts paper; you lose! ")
elif player_shoots == "scissor" and comp_shoots == "rock":
    print("Rock breaks scissor; you lose! ")
elif player_shoots == "scissor" and comp_shoots == "paper":
    print("Scissor cuts papr; you win!")


# # lower - conver to lowercase
# # strip - removes whitespace form the beginning and end
# response = input('Would you like to play?').lower().strip()
# # response = True if response == 'yes' else False
# response = response == 'yes'
# if response in ['yes', 'y', 'ok']:
#     pass
