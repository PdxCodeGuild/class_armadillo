# Hangman
# Sam, Charlie, Nicholas, Lawrence, Kyle, Keegan
# April 24, 2020
import random

def load_words(path):
    '''
    Loads list of words from a 
    .txt file located at path
    '''

    # open the file located at the path
    with open(path, 'r') as word_file:
        # .read() returns one long string with 
        # new line characters in between each line \n
        text = word_file.read()

    # split the giant string at every new line
    text = text.split('\n')
    
    word_list = []
    # check each word in the list,
    # if its length is greater than 5,
    # add it to the word list
    for word in text:
        if len(word) > 5:
            word_list.append(word)
    
    return word_list


path = '../../../1 Python/data/english.txt'

# list of potential secret words
word_list = load_words(path)

# start the game
game_on = True

# set remaining guesses
remaining_guesses = 10

# Select the secret word
secret = random.choice(word_list)

# create an empty list to store guesses
guessed_letters = []

# create an empty list to store our game board
game_board = []

# Fill game board with blanks
for i in range(len(secret)):
    game_board.append('_')

print(f"\n{' '.join(game_board)}")
while game_on:

    # ask for guess
    user_guess = input('Guess a letter: ')

    # ensure the user enters a letter
    while not user_guess.isalpha():
        print('You must guess a letter.')
        user_guess = input('Guess a letter: ')

    # ensure that the guess hasn't already been guessed
    while user_guess in guessed_letters:
        print(f"You already guessed '{user_guess}'.")
        user_guess = input('Guess a letter: ')

    # add the guess to the list of guessed letters
    guessed_letters.append(user_guess)

    # if guess not in word, decrement guesses
    if user_guess not in secret:
        print(f"\n'{user_guess}' is not in the secret word!")
        remaining_guesses -= 1

    # if guess in word replace the underscores
    # with the correct letter
    elif user_guess in secret:
        for i in range(len(secret)):
            secret_letter = secret[i]
            if secret_letter == user_guess:
                game_board[i] = user_guess
    print(f"\n{' '.join(game_board)}")
    print(f"Guesses remaining: {remaining_guesses}")
    print(f"Previous guesses: {', '.join(guessed_letters)}")

    # if we're out of guesses
    if remaining_guesses == 0:
        print("\nYou've used up all your guesses! You lose!")
        print(f"The secret word was: {secret}")
        game_on = False

    # if the user finds all the letters in the secret
    elif game_board == list(secret):
        print("\nYou found the secret word!")
        game_on = False

    # when a game has ended, ask to play again
    if not game_on:
        keep_playing = input("\nDo you want to play again? y/n: ").lower().replace(" ", "")
        while keep_playing not in ['y','n']:
            print('Invalid selection. Enter y for yes, n for no')
            keep_playing = input("\nDo you want to play again? y/n").lower().replace(" ", "")

        if keep_playing == 'y':
            # reset all game values
            remaining_guesses = 10
            secret = random.choice(word_list)
            guessed_letters = []
            game_board = []
            for i in range(len(secret)):
                game_board.append('_')

            print(f"\n{' '.join(game_board)}")
            game_on = True
            continue
        elif keep_playing == 'n':
            print('\nThanks for playing!')


