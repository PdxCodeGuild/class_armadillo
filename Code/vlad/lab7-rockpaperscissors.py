#Lab 7: Rock Paper Scissors

import random

choices = ["rock", "paper", "scissors"]

while True:
  comp = random.choice(choices)  # to test to see if the program is working I can force a choice by commenting this line and making it select rock
      #comp = "rock"
  user = input("Choose,rock, paper, or scissors: ").lower()  # to make sure that the inputs are lower cases add the .lower()

      # use a while LOOP
  while user not in choices:
    user = input("Choose rock, paper, or scissors: ").lower()

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

  if user not in ["yes", "y", "yeah", "sure"]:
      break
