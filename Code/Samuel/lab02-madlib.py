# PDX Code Guild Fullstack Course
# Lab 02 MadLib
# Samuel Purdy
# 4/6/2020

# Version 1 Initial Assignment
# Version 2 Optional added on lines 30 to 42, and on lines 46 to 52
# Version 3 Optional added on line 29, and lines 55 to 66.

# Importing the random module for use
import random

# Custom Module used to verify inputs when using input().
import verify
# Inputs for verify.valid_input() to check against.
valid_inputs = ["Yes", "No"]

# Game rules to make sure the user wants to continue to play the game. Set to "Yes" by default to run through the game once.
game_working = "Yes"
print_words = "Yes"

# Initializing variables to hold changing information
adjective = ""
noun = ""
plural_noun = ""
adverb = ""
verb_ending_in_ing = ""
silly_word_plural = ""
first_name = ""
number = 0
another_first_name = ""

# While game_working == "Yes", keep looping through the code to play the game. game_working is initialized as "Yes"
while game_working == "Yes":

    # Gets the inputs from the player, then spliting the string accordingly depending on which inputs were asked.
    adjective = input("Please enter in 4 adjectives separated by commas: ").strip()
    adjective = adjective.split(",")
    noun = input("Please enter in a noun: ")
    plural_noun = input("Please enter in 3 plural nouns separated by commas: ").strip()
    plural_noun = plural_noun.split(",")
    adverb = input("Please enter in an adverb: ")
    verb_ending_in_ing = input("Please enter in a verb ending in \"ing\":")
    silly_word_plural = input("Please enter in a plural silly word: (Silly words can be not real words.) ")
    first_name = input("Please enter in a first name: ")
    number = input("Please enter in a number: ")
    another_first_name = input("Please enter in 6 different first names, each separated by commas: ").strip()
    another_first_name = another_first_name.split(",")

    # While print_words == "Yes", continue looping to print the story. print_words is initialized to "Yes"
    while print_words == "Yes":
        print(f"When we look up into the sky on a/an {random.choice(adjective)} summer night, we see millions of tiny spots of lite.")
        print(f"Each on represents a/an {noun} which is the center of a/an {random.choice(adjective)} solar system with dozens of {random.choice(plural_noun)} revolving {adverb} around a distant sun.")
        print(f"Sometimes these suns expand and begin {verb_ending_in_ing} their neighbors. Soon they will become so big they will turn into {silly_word_plural}.")
        print(f"Eventually they subside and become {random.choice(adjective)} giants or perhaps black {random.choice(plural_noun)}.")
        print(f"Our own planet, which we call {first_name}, circles around our {random.choice(adjective)} sun {number} times every year. There are eight other planets in our solar system.")
        print(f"They are named {another_first_name[0]}, {another_first_name[1]}, {another_first_name[2]}, {another_first_name[3]}, {another_first_name[4]}, {another_first_name[5]}, Jupiter, and Mars.")
        print(f"Scientists who study these planets are called {random.choice(plural_noun)}.")
        # Resets print words so that it can inquire if the player wants to print the story again after printing.
        print_words = None
        # Checks to see if the user wants to print the story again, causing some words to change due to random.choice(), "Yes" continues the loop, "No" exits the loop.
        while not verify.valid_input(print_words, valid_inputs, against_string= True, against_list= True):
            print_words = input("Would you like to read the story again? (Yes/No) ")
    
    # Resets game rules in order to check to see if the player wants to play again. print_words switched back to "Yes" so that it would print the words again if the user desired.
    print_words = "Yes"
    game_working = None

    # Checks to see if the user wants to play the game again, "Yes" continues the loop, "No" exits the loop.
    while not verify.valid_input(game_working, valid_inputs, against_string= True, against_list= True):
        game_working = input("Would you like to make another story? (Yes/No) ")

# If there is any other way you would prefer me to do comments, please let me know, I want to make sure these are sufficient and helpful.