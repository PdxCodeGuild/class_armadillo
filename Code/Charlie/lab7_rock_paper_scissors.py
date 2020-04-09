import random

choices = ["rock", "paper", "scissors"]

comp = random.choice(choices)

user = input("Choose: rock, paper, scissors: ").lower()

while user not in choices:
    user = input("Choose: rock, paper, scissors: ").lower()
 
if user == comp:
        print(f"You chose {user} and computer chose {comp}. It is a tie")
elif user == "rock":
    if comp == "paper":
            print(f"You chose {user} and computer chose {comp}. You lose!")
    else:
            print(f"You chose {user} and computer chose {comp}. You win!")
elif user == "paper":
    if comp == "scissors":
            print(f"You chose {user} and computer chose {comp}. You lose!")
    else:
            print(f"You chose {user} and computer chose {comp}. You win!")
else:
    if comp == "rock":
            print(f"You chose {user} and computer chose {comp}. You lose!")
    else:
            print(f"You chose {user} and computer chose {comp}. You win!")
    user = input("Would you like to play again? ").lower()


