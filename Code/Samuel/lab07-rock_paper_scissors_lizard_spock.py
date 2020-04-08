# PDX Code Guild Fullstack Course
# Lab 07 Rock Paper Scissors Lizard Spock
# Samuel Purdy
# 4/8/2020

# Imports Random Module.
import random

# Moveset: R = Rock, P = Paper, S = Scissors.
possible_moves = ["R", "P", "S", "L", "K"]

# Defining variables.
user_input = "Y"
user_move = "Y"


def check_valid_move(str1):
    for move in possible_moves:
        if str1 == move:
            return True
    return False


# Keeps playing the game if the user wants to.
while user_input == "Y":
    # Prints the choices.
    print("--------------------------------------")
    print("Rock Paper Scissors Lizard Spock Game!")
    print("R = Rock")
    print("P = Paper")
    print("S = Scissors")
    print("L = Lizard")
    print("K = Spock")

    # Checks to make sure the user uses the correct moves.
    while not check_valid_move(user_move.upper):
        user_move = input("Choose one: ")

    # Prints User move and computer move
    print(f"You chose {user_move.upper}")

    # Generates a random move for the computer to use.
    computer_move = random.choice(possible_moves)

    # Prints the computers move
    print(f"The computer chose {computer_move}")

    # Checks to see who won or if it's a draw.
    if user_move.upper == computer_move:
        print("It's a draw!")
    # Checks user Rock cases
    elif user_move.upper == "R" and computer_move == "P":
        print("Computer wins!")
    elif user_move.upper == "R" and computer_move == "S":
        print("User wins!")
    elif user_move.upper == "R" and computer_move == "K":
        print("Computer wins!")
    elif user_move.upper == "R" and computer_move == "L":
        print("User wins!")
    # Checks user Paper cases
    elif user_move.upper == "P" and computer_move == "R":
        print("User wins!")
    elif user_move.upper == "P" and computer_move == "S":
        print("Computer wins!")
    elif user_move.upper == "P" and computer_move == "K":
        print("User wins!")
    elif user_move.upper == "P" and computer_move == "L":
        print("Computer wins!")
    # Checks user Scissors cases
    elif user_move.upper == "S" and computer_move == "R":
        print("Computer wins!")
    elif user_move.upper == "S" and computer_move == "P":
        print("User wins!")
    elif user_move.upper == "S" and computer_move == "K":
        print("Computer wins!")
    elif user_move.upper == "S" and computer_move == "L":
        print("User wins!")
    # Checks user Lizard cases
    elif user_move.upper == "L" and computer_move == "R":
        print("Computer wins!")
    elif user_move.upper == "L" and computer_move == "P":
        print("User wins!")
    elif user_move.upper == "L" and computer_move == "S":
        print("Computer wins!")
    elif user_move.upper == "L" and computer_move == "K":
        print("User wins!")
    # Checks user Spock cases
    elif user_move.upper == "K" and computer_move == "R":
        print("User wins!")
    elif user_move.upper == "K" and computer_move == "P":
        print("Computer wins!")
    elif user_move.upper == "K" and computer_move == "S":
        print("User wins!")
    elif user_move.upper == "K" and computer_move == "L":
        print("Computer wins!")

    # Resets inputs incase the player wishes to play again.
    user_move = "Y"
    user_input = "S"

    # Asks the user if they want to play again.
    while user_input.upper != "Y" and user_input.upper != "N":
        user_input = input("Play again? (Y/N) ")
