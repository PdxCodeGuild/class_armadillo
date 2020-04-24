import random
import string

def loads_words(file_path):
    with open (file_path, "r") as file: # opens file, python "(r)eads" as file
        words = file.read() # assigns giant string to words
    split_words = words.split('\n') # breaks up giant sting and puts them into a variable called "split words" and it is a list of strings

    words_more_five = [] # list that we will append to from the for loop
    for word in split_words: # literally, for the word in the list of words (split_Words)
        if len(word) >= 5: # if the length of the word (variable only in for loop) is greater than 5
            words_more_five.append(word) # append will add word greater than 5 to words_more_than_five
    
    return words_more_five #returns an object ["word", "word", "word"] forever

list_words = loads_words("english.txt") # list_words = function 

play_word = random.choice(list_words) # chooses a random word from the list 

underscores = ['_'] * len(play_word) # this will create a list of _ the length of the play_word
# underscores = ' '.join(underscores)
turns = 0 # while turns less than 10 - this starts us at 0
max_turns = int(len(play_word) * 1.5)
guesses = [] # list to append user's letter guess to

# game loop - loop until we run out of turns
while turns <= max_turns:
    
    # show the user some helpful info, use join to print lists more nicely
    print(f"you've guessed {turns} times, you have {max_turns - turns} left")
    print(f"here are the letters you've guessed: {' '.join(guesses)}")
    print(f"Here is the word to guess: {' '.join(underscores)}") 

    # get a letter from the user
    guessed_letter = input("Enter a letter: ").lower()

    # check if the input from the user is actually a letter
    if guessed_letter not in string.ascii_lowercase:
        print("I don't get that")
        continue
    
    # check if the user has already guessed that letter
    if guessed_letter in guesses:
        print("you already guessed that")
        continue
    
    # add the guessed letter to the list of previous guesses
    guesses.append(guessed_letter)

    # check if the letter is in the chosen word
    if guessed_letter in play_word:
        # if it is, replace the _'s in underscores with that letter
        for i in range(len(play_word)):
            if play_word[i] == guessed_letter:
                underscores[i] = guessed_letter
    else: # if the letter is not in the chosen word
        # increment turns
        turns += 1
        # check if the user lost, if so exit the loop
        if turns == max_turns:
            print(f"You ran out of guesses, the word was {play_word}")
            break
        print('the letter not in the word')

    # check if we won (there are no more _ in underscores)
    if "_" not in underscores:
        print(f"the word was {play_word}")
        print("YOU WON!")
        break

# play_again = input("Would you like to play again? y/n")
    # if play_again == "y":
        
    # else:
    #     print("Goodbye")
    #     exit()




    #boolean flag check
    # found_letter = False
    # for i in range(len(play_word)):
    #     if play_word[i] == guessed_letter:
    #         underscores[i] = guessed_letter
    #         found_letter = True
    # if not found_letter:
    #     print('letter not found')

# underscores = ' '.join(underscores) # this will break the letter out of the list and return a giant string of chars 
# 0 1 2 3 4 5
# c o d i n g
# _ _ _ _ _ _
# enter a letter: d
# d _ _ _ d _ _ _

# print guess this word _ _ _ _ _ _ _ 

# user enters a letter

# if the letter is in play_word replace _ with letter
# if the letter is not in play_word -1 guess and ask user to enter a letter 
# an empty list that will print to the terminal of guessed letters 

# print(len(word) replace with _ * len of word "_ _ _ _ _ _")
# print(list_words[:100])




'''
(4/24/20 - MOB with Matt, scribe - Nick Gallo)
Lab: Hangman

Let's write a program to play a game of hangman. In the data folder, you'll find `english.txt` which contains a list of several thousand english words. Write a function `load_words(path)` which reads the text from this file and return a list of strings which are greater than 5 letters. Randomly pick a word from that list and begin the game. Allow the user 10 tries to guess the letters of the word. Keep track of the letters the user has already guessed.

Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. If they guess a letter they've guessed before, tell them and do **not** subtract 1 from their guesses.

Be kind, if the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.

```
_ _ _ _ _ _ _ _ _
# of guesses remaining: 10
already guessed:

Guess a letter: a
_ a _ _ _ _ a _ _
# of guesses remaining: 10
already guessed: a

Guess a letter: a
You've already guessed that
_ a _ _ _ _ a _ _
# of guesses remaining: 10
already guessed: a

Guess a letter: k
_ a _ _ _ _ a _ _
# of guesses remaining: 9
already guessed: a, k
Guess a letter:
'''