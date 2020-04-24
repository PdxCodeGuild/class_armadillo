import random
from os import path

# Loads the words based on the path.
# path = file location destination.
def load_words(path):
    words_to_set = list()

    # Makes the file readable.
    with open(path, 'r') as word_file:
        text = word_file.read()
    
    # splits the text into a list based on \n new lines.
    text = text.split("\n")

    # If the length of the word is longer than 5, it will add it to the 
    # list of words to return.
    for word in text:
        if len(word) > 5:
            words_to_set.append(word)
    return words_to_set    

# Returns a valid input from the user based on the letters they have guessed. 
# It will make sure that the user picks a letter and something that is not 
# greater than one.
# letters = Letters Guessed
def handle_input(letters):
    user_input = str()
    while not user_input.isalpha() or user_input in letters or len(user_input) > 1:
        user_input = input("Enter in a letter to guess: ")
        if not user_input.isalpha():
            print("The input is not a letter.")
        elif user_input in letters:
            print(f"You've already guessed: {user_input}.")
        elif len(user_input) > 1:
            print("Please enter in a single letter.")
    return user_input

# Prints the hangman in the console, and prints the appropriate parts 
# based on the number of guessed.
# guesses = number of guesses the user has made.
def print_hangman(guesses):
    print(" ++---------+")
    print(" ||        ", end="")
    if guesses <= 9:
        print(" | ")
    else:
        print("")
    print(" ||        ", end="")
    if guesses <= 8:
        print(" | ")
    else:
        print("")
    print(" ||        ", end="")
    if guesses <= 7:
        print(" | ")
    else:
        print("")
    print(" ||        ", end="")
    if guesses <= 6:
        print(" O ")
    else:
        print("")
    print(" ||        ", end="")
    if guesses <= 5:
        print("-", end="")
        if guesses >= 5:
            print("")
    else:
        print("")
    if guesses <= 4:
        print("+", end="")
        if guesses >= 4:
            print("")
    if guesses <= 3:
        print("-")
    print(" ||        ", end="")
    if guesses <= 2:
        print(" | ")
    else:
        print("")
    print(" ||        ", end="")
    if guesses <= 1:
        print("/", end="")
        if guesses >= 1:
            print("")
    else:
        print("")
    if guesses <= 0:
        print(" \\")
    
    print("[][]       ")

# Initializing all the variables we are using.
path = '../../1 Python/data/english.txt'
words = load_words(path)
letters_guessed = list()
word_to_check = str()
guesses_left = int()
user_input = str()
random_word = str()
letters_left = int()
correct_guess = False

# Loops through the game.
while True:
    # Sets the number of guesses
    
    guesses_left = 10
    print("Welcome to hangman!")

    # Selects a random word
    random_word = random.choice(words)
    
    # Gets the number of letters so we know how many letters are left.
    letters_left = len(random_word)
    
    # If the number of guesses hits 0, the game ends.
    while guesses_left > 0:

        # Resets the correct guess.
        correct_guess = False
        
        # Prints the hangman, based on the number of guesses left.
        print_hangman(guesses_left)
        print(f"You have {guesses_left} guesses left.")

        # Prints all letters guessed.
        print("Letters guessed: ", end = " ")
        letters_guessed.sort()
        for i in range(len(letters_guessed)):
            print(letters_guessed[i], end = " ")
        print("\n")

        # Prints the word with blanks, for each correct letter 
        # guessed, it will print the actual word in its place.
        for i in range(len(random_word)):
            if random_word[i] in letters_guessed:
                print(random_word[i], end = " ")
            else:
                print("_", end = " ")
        print("\n")

        # If all correct letters are selected, it will print a
        # message and break from the game.
        if letters_left == 0:
            print("You've won the game!")
            break

        # Gets the guess from the user.
        user_input = handle_input(letters_guessed)

        # Records the guess from the user.
        letters_guessed.append(user_input)

        # Checks to see if the letter guessed is in the word 
        # to check.
        for i in range(len(random_word)):
            if user_input == random_word[i]:
                letters_left -= 1
                correct_guess = True
        
        # If the guess was not correct, it will decriment the 
        # number of guesses left.
        if not correct_guess:
            guesses_left -= 1
    
    # Prints a you lose message if you left the loop for having 
    # no guesses left.
    if guesses_left == 0:
        print_hangman(guesses_left)
        print("You've lost the game!")
    
    # Checks if the user wants to play again.
    while user_input != "Yes" and user_input != "No":
        user_input = input("Would you like to play again? (Yes/No) ")
    
    # Breaks out of the game to end it.
    if user_input == "No":
        break

    # Resets the variables for further use if the player wants to play again.
    user_input = str()
    letters_guessed = list()

print("Thanks for Playing!")
