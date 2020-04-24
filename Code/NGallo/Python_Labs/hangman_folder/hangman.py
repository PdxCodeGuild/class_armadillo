import random

def loads_words():
    with open ("english.txt","r") as file: # opens file, python "(r)eads" as file
        words = file.read() # assigns giant string to words
    split_words = words.split('\n') # breaks up giant sting and puts them into a variable called "split words" and it is a list of strings

    words_more_five = [] # list that we will append to from the for loop
    for word in split_words: # literally, for the word in the list of words (split_Words)
        if len(word) >= 5: # if the length of the word (variable only in for loop) is greater than 5
            words_more_five.append(word) # append will add word greater than 5 to words_more_than_five
    
    return words_more_five #returns an object ["word", "word", "word"] forever

list_words = loads_words() # list_words = function 

play_word = random.choice(list_words) # chooses a random word from the list 

play_word = "coding"
# print(play_word)

underscores = ['_'] * len(play_word) # this will create a list of _ the length of the play_word

turns = 0 # while turns less than 10 - this starts us at 0
guesses = [] # list to append user's letter guess to

while turns <= 10:

    print(f"you've guessed {turns} times.\n")
    print(f"you have {10 - turns} left\n")
    print(f"here are the letters you've guessed: {guesses}\n") # print statements for game
    print(f"Here is the word to guess: {underscores}\n")

    turns += 1 # adds a turn to turns outside of loop
    user_guess = input("Enter a letter: ")
    guesses.append(user_guess)
    for i in range(len(play_word)):
        if play_word[i] == user_guess:
            underscores = underscores.replace("_", user_guess)

print(user_guess)

# underscores = ' '.join(underscores) # this will break the letter out of the list and return a giant string of chars 



# 0 1 2 3 4 5 6 7
# d r e a d f u l
# _ _ _ _ _ _ _ _
# enter a letter: d
# d _ _ _ d _ _ _

# print guess this word _ _ _ _ _ _ _ 

# user enters a letter

# if the letter is in play_word replace _ with letter
# if the letter is not in play_word -1 guess and ask user to enter a letter 
# an empty list that will print to the terminal of guessed letters 

# print(len(word) replace with _ * len of word "_ _ _ _ _ _")
# print(list_words[:100])

# Lab: Hangman
# Let's write a program to play a game of hangman. In the data folder, you'll find english.txt which contains a list of several thousand english words. Write a function load_words(path) which reads the text from this file and return a list of strings which are greater than 5 letters. Randomly pick a word from that list and begin the game. Allow the user 10 tries to guess the letters of the word. Keep track of the letters the user has already guessed.

# Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. If they guess a letter they've guessed before, tell them and do not subtract 1 from their guesses.

# Be kind, if the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

# Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.

# _ _ _ _ _ _ _ _ _
# # of guesses remaining: 10
# already guessed:

# Guess a letter: a
# _ a _ _ _ _ a _ _
# # of guesses remaining: 10
# already guessed: a

# Guess a letter: a
# You've already guessed that
# _ a _ _ _ _ a _ _
# # of guesses remaining: 10
# already guessed: a

# Guess a letter: k
# _ a _ _ _ _ a _ _
# # of guesses remaining: 9
# already guessed: a, k
# Guess a letter: