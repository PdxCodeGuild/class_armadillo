"""

Lab 2: Mad Libs=====================================================================================
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Version 2 (optional)================================================================================

-Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, 
 separated by commas, then use the .split() function to store each adjective and later use it in 
 your story.
-Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

Version 3 (optional)================================================================================
-Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether 
 they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again 
 until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.
 
 """
import random

 while true:
     print("Let's play Madlibs!")
     
     """
     V2 - utilize lists.
     """
     adjectives = [] #need 4 adjectives
     first_names = [] #need 2 first names
     nouns = [] # 2 nouns 
     pl_nouns = []
     animals = [] #1 animal
     verbs = [] # 1 verb
     verb_ings = [] # 3 verbs ending in -ing
     adverbs = [] # 1 adv

     """
     Ask the user for each word you'll put in your Mad Lib
     """

     """
     Use the random module to select which adjective goes where in the story.
     """

     print(f"They say my school is haunted; my {adj1} friend {first_name} says he saw a {adj2} {noun1} floating at the end of the hall near the cafeteria. Some say if you {verb1} down the hallway at night, you'll hear a {animal} {verbing} {adverb}. My {adj3} friend {first_name2} saw a {adj4} {noun2} {verbing2} under one of the tables. I hope I never see any {plnoun} {verbing3}; eating lunch there is scary enough!")
    


