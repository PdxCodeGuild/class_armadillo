
# Import random is for the program to randomly chose between the choices
# Import time is used to give the user time to read the welcome message 
# and rules before the program moves on to the next function
import random
import time
# The welcome message
print("Welcome to Rock, Paper, Scissors \n")
time.sleep(3)
# Rules of the game
print("Winning Rules of the Rock paper scissor game as follows: \n"
"Rock vs paper->paper wins \n"
"Rock vs scissor->Rock wins \n"
"paper vs scissor->scissor wins \n")
time.sleep(3)
# The main section of the game. 
# I used a While loop, to loop through the different portinos of the program. 
# Telling the program what to do depending on the user choice and the programs random choice
while True:
    print("Enter choice \n1. Rock \n2. paper \n3. scissor \n")

    choice = int(input("User turn: "))

    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
    # This shows what the user's choice is
    print("user choice is: " + choice_name)

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else: 
        comp_choice_name = 'Scissor'
    # This shows what the computers choice is
    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " VS " + comp_choice_name)
    # This section of the While loop shows whice move won
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice == 1)):
        print("****PAPER WINS**** \n", end = "")
        result = "Paper"

    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        print("****ROCK WINS**** \n", end = "")
        result = "Rock"
    else:
        print("****SCISSOR WINS**** \n", end = "")
        result = "Scissor"
    # This is the continue option with a simple Y or N input response.
    #  If user chooses Y the game repeats, if the user chooses N the 
    # program moves to the end meassage
    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break
    # The end message
print("\nThanks for playing")