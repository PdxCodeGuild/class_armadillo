import random
user_score = 0
comp_score = 0


choices = ["rock", "paper", "scissors"]

comp = random.choice(choices)

user = input("Choose: rock, paper, scissors: ").lower()

answer = ["yes", "ya", "yea", "sure", "ok"]

while user not in choices:
    user = input("Please enter valid input: ").lower()


   
 
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
elif user == "scissors":
    if comp == "rock":
                print(f"You chose {user} and computer chose {comp}. You lose!")
    else:
            print(f"You chose {user} and computer chose {comp}. You win!")
        
i = input("would you like to play again? ")
if i in (answer):
    i = (user)
    print(i)
                    






