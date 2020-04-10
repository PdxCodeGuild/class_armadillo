import random
import time

print('\n' + '~'*44)
print('Welcome to the \'Rock Paper Scissors\' game...')
print('~'*44)

time.sleep(1)

choices = ["rock", "paper", "scissors"]

user = input("Choose rock, paper or scissors: ")

computer = random.choice(choices)

time.sleep(1)

print("\nYou: "+ user)
print("Computer: " + computer + '\n')

time.sleep(1)

if user == "rock" and computer == "paper":
    print("You lose!")
elif user == "rock" and computer == "scissors":
    print("You win!!")      
elif user == "paper" and computer == "rock":
    print("You win!!")  
elif user == "paper" and computer == "scissors":
    print("You lose!!")  
elif user == "scissors" and computer == "rock":
    print("You lose!!") 
elif user == "scissors" and computer == "paper":
    print("You win!!")
elif user == computer:
    print("It's a tie!!!")

print('\n')


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