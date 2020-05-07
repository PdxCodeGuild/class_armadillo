import random

# Lab 7: Rock Paper Scissors


# game choices
# assign variable comp to random .choice so it can generate a random choice from the list choices
# assign variable user to the input that the user will be inputing 




def game():
    comp = random.choice(choices)
    user = input("Choose: rock, paper, scissors: ").lower()
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




choices = ["rock", "paper", "scissors"]


game()        

while True:
    play_again = input("Do you want to play again?\nPlease type y for YES or enter any key to exit: ")
    if play_again == 'y':
        game()
        continue
    else:
        print("Thanks for playing goodbye!!")
        break
            

                    






