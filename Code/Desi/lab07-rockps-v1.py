import random

# mistakes made
#import def statement and 2 variables in def statement parenthesis



# The computer will ask the user for their choice 
# (rock,paper, scissors)

# The computer will randomly choose rock, paper or scissors
#rock vs rock (tie)

def who_wins(user, computer):
 
    if user == computer:
        print("This is a tie")
    #rock vs paper
    elif user == "rock" and computer == "paper":
        print("Computer wins")
    #rock vs scissors
    elif user == "rock" and computer == "scissors":
        print("User wins")
    #paper vs rock
    elif user == "paper" and computer == "rock":
        print("User wins! Yeay!")
    #paper vs paper (tie)
    elif user == "paper" and computer == "paper":
        print("Everyone is a winner!")
    #paper vs scissors
    elif user == "paper" and computer == "scissors":
        print("The computer won!")
    #scissors vs rock
    elif user == "scissors" and computer == "rock":
        print("Computer wins!")
    #scissors vs paper
    elif user =="scissors" and computer == "paper":
        print("User wins! Yippee")
    #scissors vs scissors (tie)
    elif user == "scissors" and computer == "scissors":
        print("Another tie")

user = input("We are going to play rock, paper, scissors."
+  "I am going to randomly choose between the three"
 + "choices - type 'rock', 'paper', or 'scissors'! : ")
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

print(who_wins(user, computer))



# Version 2 (optional)
# After playing, ask them if they'd like to play again. If they say yes, 
# restart the game, otherwise exit.

# Version 3 (optional)