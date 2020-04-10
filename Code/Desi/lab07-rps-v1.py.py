Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

# The computer will ask the user for their choice (rock,paper, scissors)
user = input("We are going to play rock, paper, scissors.  I am going to 
randomly choose between the three choices and I want you to choose as well.")

rock vs rock (tie)
if user == computer:
    print("This is a tie")
rock vs paper
elif user == "rock" and computer == "paper":
    print("Computer wins")
rock vs scissors
elif user == "rock" and computer == "scissors":
    print("User wins")
paper vs rock
elif user == "paper" and computer == "rock":
    print("User wins! Yeay!")
paper vs paper (tie)

paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)


Version 2 (optional)
After playing, ask them if they'd like to play again. If they say yes, 
restart the game, otherwise exit.

Version 3 (optional)