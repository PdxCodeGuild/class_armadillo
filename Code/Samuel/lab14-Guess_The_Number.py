# PDX Code Guild Fullstack Course
# Lab 14 Guess The Number
# Samuel Purdy
# 4/22/2020

# Imports Random Module
import random

# Initiates input variables
user_input = 'F'
user_start = "Y"

# Initiates player choosing variables
computer_int = random.randint(1,10)
user_guess = "f"
user_number_guesses = 0
user_last_guess = 0

# Game over rule
game_over = False

# Initiates computer choosing variables
user_int = "f"
computer_guess = 0
computer_number_guesses = 0
comp_last_guess = 0

# Checks to see if the player wants to play again. Yes by default to start the loop
while user_start == "Y":
    print("----------------------------------------")
    print("Guess the Number Game!")
    print("G = Guess the number")
    print("C = Computer guesses the number")

    # Asks the player if they want to guess the number or for the computer to guess the number
    while user_input != 'G' and user_input != 'C':
        user_input = input('Would you like to guess the number, or do you want the computer to guess the number? (G/C) ')
    if user_input == 'G':

        # Runs the game so the player can guess the number
        while not game_over:

            # Checks to see if the player is guessing a valid number, while also recording the number
            while not user_guess.isnumeric() or int(user_guess) < 1 and int(user_guess) > 10:
                user_guess = input("Guess a number between 1 and 10: ")

            # Checks to see if the number guessed is the correct number or not
            if int(user_guess) == computer_int:

                # If the number is right, it prints victory and the number of times guessed until they got the right number
                user_number_guesses += 1
                print("You guessed the right number!")
                print(f"It took you {user_number_guesses} number of tries to guess the right number!")

                # Sets game rule to True to end the game
                game_over = True

                # Resets Variables incase the player wishes to play the game again
                computer_int = random.randint(1,10)
                user_guess = "f"
                user_number_guesses = 0

            # Checks to see if the player has gone over 10 guesses
            elif user_number_guesses == 9:

                # Tells the player they have lost for going over the 10 guesses.
                print("You have guessed 10 times, you have lost!")

                # Sets game rule to True to end the game
                game_over = True

                # Resets Variables incase the player wishes to play the game again
                computer_int = random.randint(1,10)
                user_guess = "f"
                user_number_guesses = 0
            else:

                # Tells whether or not the player was too high or low to the computers number
                user_number_guesses += 1
                if int(user_guess) > computer_int:
                    print("Your guess was too high!")
                else:
                    print("Your guess was too low!")

                # Checks to see if the players last guess was closer or not, then printing a message if it was. 
                # If the number was not closer, it will just set the last guess to the number guessed. 
                # If there was no last guessed, it will set the last guess to number guessed.
                if user_last_guess == 0:
                    user_last_guess = int(user_guess)
                elif int(user_guess) > user_last_guess and user_last_guess < computer_int:
                    print("Your current guess is closer than your last guess!")
                    user_last_guess = int(user_guess)
                elif int(user_guess) < user_last_guess and user_last_guess > computer_int:
                    print("Your current guess is closer than your last guess!")
                    user_last_guess = int(user_guess)
                else:
                    user_last_guess = int(user_guess)
                user_guess = "f"

        # Resets game rule and user input
        game_over = False
        user_input = 'F'

    # Starts the game where the player began by choosing a number, and the computer has to guess.
    else:

        # Checks to see if the player has selected a valid number,
        while not user_int.isnumeric() or int(user_int) < 1 and int(user_int) > 10:
            user_int = input("Please set a number between 1 and 10: ")

        # Starts the computer guessing by setting a random number between 1 and 10. It also prints the number guessed by the computer.
        while not game_over:
            computer_guess = random.randint(1,10)
            print(f"The computer guessed {computer_guess}")

            # Checks to see if the computer guessed the right number or not
            if computer_guess == int(user_int):

                # If the number is correct, it will print victory, and the number of guesses.
                computer_number_guesses += 1
                print("The computer guessed the right number!")
                print(f"It took the computer {computer_number_guesses} number of tries to guess the right number!")

                # Resets game rule to stop the game
                game_over = True

                # Resets Variables incase the player wishes to play the game again
                user_int = "f"
                computer_guess = 0
                computer_number_guesses = 0

            # Checks to see if the computer has gone over 10 guesses.
            elif computer_number_guesses == 9:

                # Tells the player they have lost for going over the 10 guesses.
                print("The computer has guessed 10 times, they have lost!")

                # Resets game rule to stop the game
                game_over = True

                # Resets Variables incase the player wishes to play the game again
                user_int = "f"
                computer_guess = 0
                computer_number_guesses = 0
            else:

                # Tells whether or not the computer was too high or low with their guess.
                computer_number_guesses += 1
                if int(user_int) > computer_guess:
                    print("The computers guess was too high!")
                else:
                    print("The computers guess was too low!")

                # Checks to see if the computers last guess was closer or not, then printing a message if it was. 
                # If the number was not closer, it will just set the last guess to the number guessed. 
                # If there was no last guessed, it will set the last guess to number guessed.
                if comp_last_guess == 0:
                    comp_last_guess = computer_guess
                elif computer_guess > comp_last_guess and comp_last_guess < int(user_int):
                    print("Your current guess is closer than your last guess!")
                    comp_last_guess = computer_guess
                elif computer_guess < comp_last_guess and comp_last_guess > int(user_int):
                    print("Your current guess is closer than your last guess!")
                    comp_last_guess = computer_guess
                else:
                    comp_last_guess = computer_guess

        # Resets game rule and user input
        game_over = False
        user_input = 'F' 
        
    # Resets user start to check and see if they want to play again or not.
    user_start = "F" 
    while user_start != "Y" and user_start != "N":
        user_start = input("Would you like to play another game? (Y/N) ")