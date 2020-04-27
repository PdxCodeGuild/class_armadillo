"""
Lab: Hangman Game ========================================================================

Let's write a program to play a game of hangman. In the data folder, you'll find 
english.txt which contains a list of several thousand english words. Write a function 
load_words(path) which reads the text from this file and return a list of strings which 
are greater than 5 letters. Randomly pick a word from that list and begin the game. Allow 
the user 10 tries to guess the letters of the word. Keep track of the letters the user has 
already guessed.

Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in 
the word, show the blanks with the letters filled in. If they guess a letter which is not 
in the word, tell them and subtract 1 from their remaining guesses. If they guess a letter 
they've guessed before, tell them and do not subtract 1 from their guesses.

Be kind, if the user can't guess the word in the number of allotted guesses, print the word 
and ask them if they'd like to play again.

Feel free to customize the user interface, but provide these minimum features. Below is an 
example run of the program.

"""
import random

def load_words(path):

    with open(path, 'r') as f: # open the file as f
        words = f.read() # f.read() returns a string of the contents of the file
    list_of_words = words.split() # words.split() splits that string on whitespace ('\n' in this case)
    
    list_of_long_words = [] # start with an empty list for words w/ more than 5 letters
    for word in list_of_words: # loop over over list_of_words
        if len(word) > 5: # if a word has more than 5 characters,
            list_of_long_words.append(word) #append it to list_of_long_words
    return list_of_long_words # return a list of strings greater than 5 letters

path = "Code\Adam\mob_hangman\english.txt" # path to folder from my python/ directory (may be different for some students)

hangman_words = load_words(path)

"""
Randomly pick a word from that list and begin the game.
"""
# random_word = random.choice(hangman_words) # random word
# guesses = 10 # give the user 10 guesses
# already_guessed = [] # create an empty list for guessed letters
# print(random_word) # print random_word for testing purposes

while True: # while the user has guesses remaining
    guesses = 10 # give the user 10 guesses
    already_guessed = [] # create an empty list for guessed letters
    random_word = random.choice(hangman_words) # random word
    

    while guesses > 0:
        winning_word = 0

        for letter in random_word: # loop over random_word
            if letter in already_guessed: # if the letter is in already_guessed,
                winning_word += 1
                print(f'{letter} ', end='') # print that letter in the "_ _ _ _" template
            else: 
                print('_ ', end='') # otherwise, just print "_"
        print() # print() just creates an empty line

        if winning_word == len(random_word):
            print("You win!")
            break

        # elif guesses == 0:
        #     print(f"We deeply regret to inform you that you have run out of guesses.\nBy the way the correct word is {random_word}...")
        #     random_word = random.choice(hangman_words) # random word
        #     continue

        print(f"# of guesses remaining: {guesses}")

        user_guess = input("Guess a letter: ").lower()
        if user_guess in random_word and user_guess not in already_guessed: # if the guess is in random_word
            print('good job')
            already_guessed.append(user_guess) # append the guess to already_guessed

        elif user_guess not in random_word and user_guess not in already_guessed:
            already_guessed.append(user_guess) # otherwise add the guess to already_guessed
            guesses -= 1 # guesses = guesses - 1 # subtract 1 for wrong guess

        elif user_guess in already_guessed: # if the guess is in already_guessed
            print(f"You have already guessed {user_guess}") # let the user know

        else:
            print("Not a valid guess!")
            # already_guessed.append(user_guess) # otherwise add the guess to already_guessed
            # guesses -= 1 # guesses = guesses - 1 # subtract 1 for wrong guess
        print(already_guessed)
        print()
        # break
    print()
    
    user_answer = input(f"You're out of guesses.\nThe word was {random_word}.\nWould you like to play again? ")
    if user_answer in ['yes', 'y']:
        continue
    elif user_answer in ['no', 'n']:
        print('Goodbye.')
        break
    else:
        print("Enter a valid response.")





# print(random_word)
# print(hangman_words)