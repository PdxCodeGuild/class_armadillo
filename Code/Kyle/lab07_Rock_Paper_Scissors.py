# Let's play rock-paper-scissors with the computer.

#     The computer will ask the user for their choice (rock, paper, scissors)
#     The computer will randomly choose rock, paper or scissors
#     Determine who won and tell the user

# Let's list all the cases:

#     rock vs rock (tie)
#     rock vs paper
#     rock vs scissors
#     paper vs rock
#     paper vs paper (tie)
#     paper vs scissors
#     scissors vs rock
#     scissors vs paper
#     scissors vs scissors (tie)

import random
import time
time_int = 3
game_options = ["paper", "rock", "scissors"]
kill_commands = ["quit", "q", "exit", "stop", "esc", "escape"]
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way', "nah"]

# tied to the kill_commands, allows a user's entry to end the game without quit() command
def endgame():
    if time_int == 0:
        time.sleep(time_int)
        print("Goodbye. ")
        quit()
    elif time_int == 1:
        print(f"Self-destruct in {time_int} second...")
        time.sleep(time_int)
        print("Goodbye. ")
        quit()
    else:
        print(f"Self-destruct in {time_int} seconds...")
        time.sleep(time_int)
        print("Goodbye. ")
        quit()

# runs the Rock, Paper, Scissors game as a function vs program's organic while loop
def rock_paper_scissors_game():
    # repeating global variable in function.
    game_options = ["paper", "rock", "scissors"]
    # Loop 1. Ask for the user entry
    while True:
        user_entry = input("Shoot your shot. Rock, Paper, or Scissors: ").lower().strip()
        computer_entry = random.choice(game_options)
        if user_entry in game_options:
            break
        elif user_entry in kill_commands:
            endgame()
        else:
            print("Not a valid response. Please try again. \n")
    
    # Loop 2. Run the Game.
    while True:
        if user_entry == "rock" and computer_entry == "rock":
            print("You selected Rock and the computer chose Rock. ")
            print("You tied!")
            break
        elif user_entry == "rock" and computer_entry == "paper":
            print("You selected Rock and the computer chose Paper. ")
            print("You lost!")
            break
        elif user_entry == "rock" and computer_entry == "scissors":
            print("You selected Rock and the computer chose Scissors. ")        
            print("You won!")
            break
        elif user_entry == "paper" and computer_entry == "paper":
            print("You selected Paper and the computer chose Paper. ")
            print("You tied!")
            break
        elif user_entry == "paper" and computer_entry == "rock":
            print("You selected Paper and the computer chose Rock. ")        
            print("You won!")
            break
        elif user_entry == "paper" and computer_entry == "scissors":
            print("You selected Paper and the computer chose Scissors. ")        
            print("You lost!")
            break
        elif user_entry == "scissors" and computer_entry == "rock":
            print("You selected Scissors and the computer chose Rock. ")        
            print("You lost!")
            break
        elif user_entry == "scissors" and computer_entry == "paper":
            print("You selected Scissors and the computer chose Paper. ")        
            print("You won!")
            break
        elif user_entry == "scissors" and computer_entry == "scissors":
            print("You selected Scissors and the computer chose Scissors. ")        
            print("You tied!")
            break
        else:
            False

# Asks the user to play
while True:
    play_game = input("Would you like to play, 'Rock, Paper, Scissors?' ").lower().strip()

    if play_game in affirmatives:
        break
    if play_game in negatives:
        print("I'm sorry to hear. Goodbye. ")
        endgame()
    elif play_game in kill_commands:
        endgame()
    else:
        print("Not a valid response. Please try again. \n")

rock_paper_scissors_game()

# repeat loop
repeat = True
while repeat:
    play_again = input("Would you like to play again? ")
    if play_again in affirmatives:
        rock_paper_scissors_game()
    elif play_again in negatives:
        print("Thank you for playing")
        repeat = False
    elif play_again in kill_commands:
        endgame()
    else:
        print("I don't understand that response. Please try again. \n")


