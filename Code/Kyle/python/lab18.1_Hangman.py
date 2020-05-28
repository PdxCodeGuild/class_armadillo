import random
affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not']
negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']
kill_commands1 = ["quit", "q", "exit", "stop", "esc", "escape"]
kill_commands2 = ["quit", "exit", "stop", "esc", "escape"]
word_list = ["lions", "tigers", "bears", "eagles"]
secret_word = ""
guesses = ""
game_letters = []
guessed_letters = []


# Welcomes the user to the game and gives the amount of guesses
print("\nWelcome to Lab 19: Hangman")


# codes a few 'quit' options 
def endgame():
    print("Goodbye!")
    quit()

# asks the user if they want to play again.
def play_again():
    while True:
        ask_again = input("Would you like to play again? ").lower().replace(" ", "")
        if ask_again in affirmatives:
            hangman_game()
        elif ask_again in negatives:
            print("Goodbye! ")
            break
        elif ask_again in kill_commands1:
            endgame()
        else:
            print("I'm sorry, I don't understand that response. Please try again. ")

# runs the entire hangman game
def hangman_game():
    guesses = random.randint(10, 13)
    print(f"You have {guesses} guesses to determine the right answer.")
    guessed_letters = []
    # Generate a secret word to guess
    secret_word = random.choice(word_list)

    # Tell the user how many letters it contains
    for i in range(len(secret_word)):
        game_letters.append('_')
    # game_letters =  ' '.join(game_letters)
    for i in range(len(secret_word)):
        number_of_letters = len(secret_word)
    print(f"The word contains {number_of_letters} letters: {' '.join(game_letters)}")

    #start game
    while True:

        # Ask the user for a letter
        user_guess = input(f"Please guess a letter: ").lower().replace(" ", "")

        # Option to end the game
        if user_guess in kill_commands2:
            endgame()

        # Check to make sure the guess is a valid letter
        while not user_guess.isalpha():
            print(f"'{user_guess}' is not a letter. Please try again. ")
            user_guess = input(f"Please guess a letter: ").lower().replace(" ", "")

        # Check to make sure the guess is only one letter
        while not len(user_guess) == 1:
            print(f"'{user_guess}' is not a valid answer - Please guess a single alphabet character. ")
            user_guess = input(f"Please guess a letter: ").lower().replace(" ", "")

        # check to see if the user has already guessed that letter
        while user_guess in guessed_letters:
            print(f"You've already guessed '{user_guess}'. Try a different letter. ")
            user_guess = input(f"Please guess a letter: ").lower().replace(" ", "")

        # Add guess to a list of guessed letters
        guessed_letters.append(user_guess)

        #If user guess is not correct
        if user_guess not in secret_word:
            guesses -= 1
            print(f"\nI'm sorry, '{user_guess}' is not correct. You have {guesses} guesses remaining.")
            print(f"You've guessed {guessed_letters} in this game. \n")
            print(f"\n{' '.join(game_letters)}")

        # if user guess is correct
        elif user_guess in secret_word:
            for i in range(len(secret_word)):
                secret_letter = secret_word[i]
                if secret_letter == user_guess:
                    game_letters[i] = user_guess
            if game_letters == list(secret_word):
                print(f"\n{' '.join(game_letters)}")
                print(f"Well done! You've correctly guessed the secret word: {secret_word}. ")
                guessed_letters = [] 
                break      
            print(f"Well done! '{user_guess}' is a correct guess. You still have {guesses} guesses remaining. ")
            print(f"\n{' '.join(game_letters)}")

        # 1 guess left
        if guesses == 1:
            print(f'You have {guesses} guess remaining. Better think hard and make this one count!')

        # No guesses left
        if guesses == 0:
            print("I'm sorry, you have no more guesses remaining. The man hangs, you lose!")
            print(f"The correct word was '{secret_word}.' You only had {' '.join(game_letters)}. ")
            break

hangman_game()
play_again()