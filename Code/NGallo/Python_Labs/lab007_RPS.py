# Lab 007
# Nick Gallo
# 04/08/2020

import random

print("\n\n----- Rock, Paper and Scissors -----\n")

keep_it_going = True

def RPS():

    emojis = {'r' : "\u26AB ", 'p': "\u267B ", 's': "\u2700 ", 'q': 'q'}
        
    rock_paper_scissors = ['r','p', 's']

    while True:
        user_character = input("Pick your weapon \u26AB  (r), \u267B  (p), \u2700  (s): ").lower().strip()
        print("\n")
        computer_character = random.choice(rock_paper_scissors)

        if user_character in rock_paper_scissors:

            user_character_emoji = emojis[user_character]

            computer_character_emoji = emojis[computer_character]

            if user_character == computer_character:
                print(f"You tied! {user_character_emoji} and {computer_character_emoji} are the same\n")
            elif user_character == 'r' and computer_character == 's':
                print(f"You won! {user_character_emoji} beats {computer_character_emoji}\n")
            elif user_character == 's' and computer_character == 'p':
                print(f"You won! {user_character_emoji} beats {computer_character_emoji}\n")
            elif user_character == 'p' and computer_character == 'r':
                print(f"You won! {user_character_emoji} beats {computer_character_emoji}\n")
            elif user_character == 'r' and computer_character == 'p':
                print(f"You lost. {user_character_emoji} is beat by {computer_character_emoji}\n")
            elif user_character == 's' and computer_character == 'r':
                print(f"You lost. {user_character_emoji} is beat by {computer_character_emoji}\n")
            elif user_character == 'p' and computer_character == 's':
                print(f"You lost. {user_character_emoji} is beat by {computer_character_emoji}\n")
        
        elif user_character == 'q':
            print("Goodbye!")
            exit()

        else:
            print("invalid character try again or press (q) to quit\n")

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