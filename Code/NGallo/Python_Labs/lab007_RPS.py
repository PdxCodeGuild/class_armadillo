# Lab 007
# Nick Gallo
# 04/08/2020

import random

print("\n\n----- Rock, Paper and Scissors -----\n")

# user_character = input("Pick your weapon r (rock), p (paper), s (scissors): ")


keep_it_going = True

def RPS():

    emojis = {'r' : "\u26AB", 'p': "\u267B", 's': "\u2700"}
    print(emojis)
    rock_paper_scissors = ['r','p', 's']

    computer_character = random.choice(rock_paper_scissors)
    print(computer_character)

    while True:
        user_character = input("Pick your weapon r (rock), p (paper), s (scissors): ")
        if user_character == computer_character:
            print(f"You tied! {user_character} and {computer_character} are the same")
        elif user_character == r and computer_character == s:
            print("You won!")


RPS()




'''
Lab 7: Rock Paper Scissors
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper (tie)
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)
Version 2 (optional)
After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

Version 3 (optional)
Rock, paper, scissors, lizard, Spock! https://www.instructables.com/id/How-to-Play-Rock-Paper-Scissors-Lizard-Spock/

'''