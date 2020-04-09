'''Let's play rock-paper-scissors with the computer.

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
scissors vs scissors (tie)'''

import random
import time 

choice = ["rock", "paper", "scissors"]

print("Want to throw hands?")

while True:
    print("Wanna run it again? ")  
    user_move = input("Enter 'y' for yes and 'n' for no: ")

    if user_move == 'y':
        user_move = input("Ah snap, here we go...I choose... ")

    elif user_move == 'n':
        print("Keep movin fool!")
        quit()

    computer = random.choice(choice)

    print(computer)

    if user_move == "rock" and computer == "paper":
        print("Damn, you win!  Paper covers rock.")
    elif user_move == "rock" and computer == "scissors":
        print("Boom! You lose Sucka!  Rock smashes scissors.")
    elif user_move == "rock" and computer == "rock":
        print("Crapsticks! It is a tie!")
    elif user_move == "scissors" and computer == "paper":
        print("Boom! You lose Sucka!  Scissors cut paper.")
    elif user_move == "scissors" and computer == "rock":
        print("Damn, you win!  Rock smashes scissors.")
    elif user_move == "scissors" and computer == "scissors":
        print("Crapsticks! It is a tie!")
    elif user_move == "paper" and computer == "rock":
        print("Damn, you win!  Paper covers rock.")
    elif user_move == "paper" and computer == "scissors":
        print("Boom! You lose Sucka!  Scissors cut paper.")
    elif user_move == "paper" and computer == "paper":
        print("Crapsticks! It is a tie!")

