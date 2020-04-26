import random
import string # new import to get ascii_lowercase
path = '../../NGallo/Python_Labs/hangman_folder/english.txt' # path to folder from my python/ directory (may be different for some students)
"""
Write a function called load_words(path) which reads the text from the file and returns a list of strings which are greater than 5 letters.
"""
def load_words(path):

    with open(path, 'r') as f: # open the file as f
        words = f.read() # f.read() returns a string of the contents of the file
    list_of_words = words.split() # words.split() splits that string on whitespace ('\n' in this case)
    
    list_of_long_words = [] # start with an empty list for words w/ more than 5 letters
    for word in list_of_words: # loop over over list_of_words
        if len(word) > 5: # if a word has more than 5 characters,
            list_of_long_words.append(word) #append it to list_of_long_words
    return list_of_long_words # return a list of strings greater than 5 letters

"""The function new_game takes in one argument (hangman_words)..."""
def new_game(hangman_words):
    random_word = random.choice(hangman_words)
    guesses = 10
    already_guessed = []
    user_wins = False # this is a new game, so the win boolean will be False
    return random_word, guesses, already_guessed, user_wins
"""...and returns a tuple of (random_word, guesses, already_guessed, user_wins)."""

"""
An even more concise version that works just the same:
def new_game(hangman_words):
    return random.choice(hangman_words), 10, [], False
"""

"""The function game_turn takes in 4 arguments and prints out everything to the terminal"""
def game_turn(random_word, guesses, already_guessed, user_wins):
    winning_word = 0 
    for letter in random_word:
        if letter in already_guessed:
            winning_word += 1
            print(f'{letter} ', end='')
        else:
            print('_ ', end='')
    print()

    if winning_word == len(random_word):
        """we have a special return here if the winning conditions are met"""
        return guesses, already_guessed, True # True is returned and unpacked into user_wins 
        """return is kind of like break, we are out of the function after this line runs"""

    print(f"Guesses remaining: {guesses}")
    print("You've already guessed:")
    print(already_guessed)

    guess = input("Guess a letter: ").lower()

    if guess in already_guessed:
        print(f"You've already guessed {guess}.")

    elif guess not in string.ascii_lowercase or len(guess) != 1: # let's check to see if guess is either not lowercase or more than one character
        print("Not a valid guess.")

    else:
        already_guessed.append(guess)
        if guess in random_word:
            print("Correct.")
        else:
            print("Incorrect.")
            guesses -= 1
    print()
    return guesses, already_guessed, user_wins
"""... and returns a tuple of 3 variables (we don't have to return random_word because it hasn't changed)"""

hangman_words = load_words(path)

while True:
    # We unpack the tuple returned by new_game to define 4 variables:
    random_word, guesses, already_guessed, user_wins = new_game(hangman_words)

    while True:
        # game_turn takes in 4 agruments, runs each turn (print outs and checking user guess) and returns the 3 variables that might have been changed by the turn (random_word will not change unless a new game starts)
        guesses, already_guessed, user_wins = game_turn(random_word, guesses, already_guessed, user_wins)
        if user_wins:
            print("Congratulations, you win!")
            break
        if guesses == 0:
            print(f"You're out of guesses.  The word was {random_word}.")
            break
    print()
    
    if input("Want to play again?").lower() in ['yes', 'y']:
        continue
    else:
        break
    
print("Thanks for playing.")

"""
There are still some improvements that can be made:
1) When we print already_guessed, it shows up a like a list.  It would be nice if it prints like a, b, c instead of ['a', 'b', 'c'].
2) What if the user could choose their difficulty (number of guesses) or the number of guesses depended on the length of the word.
3) It would be cool if the game had ASCII art instead of a guess counter:
    _____
    |   |
    |   o
    |  /|\
    |   |
    |  / \
  __|__
4) Maybe it would look better if the words were uppercase instead.
"""
  