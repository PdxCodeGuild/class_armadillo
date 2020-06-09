import random

choices = ["rock", "paper", "scissors"]


user = input("choose rock paper or scissors: ")

computer = random.choice(choices)
print(computer)
​

if user  == "rock" and computer == "paper":
    print("you lose!")
elif user == "rock" and computer == "scissors": 
    print("ypu win!!")
elif user == "rock" and computer == "rock":
    print("its a tie!")
elif user == "paper" and computer == "scissors":
    print("you lose!")
elif user == "paper" and computer == "rock":
    print("you win!")
elif user == "paper" and computer == "paper":
    print("its a tie!")
elif user == "scissors" and computer == "rock":
    print("you lose!")
elif user == "scissors" and computer == "paper":
    print("you win!")
elif user == "scissors" and computer == "scissors":
    print("its a tie!")