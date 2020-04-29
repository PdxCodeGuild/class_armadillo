"""

Lab 2: Mad Libs=====================================================================================
- Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Version 2 (optional)================================================================================

- Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, 
  separated by commas, then use the .split() function to store each adjective and later use it in 
  your story.
- Add randomness! Use the random module, rather than selecting which adjective goes where in the story.

Version 3 (optional)================================================================================
- Make it a repeatable game. 
- After prompting the user for words, ask if they'd like to hear the story. 
- Use a while loop to keep asking if they'd like to hear the story again 
  until the answer is 'no'.  
- Ask them if they'd like to make another story, and so on.

V2: Utilize lists

V3: Ask if user wants to hear story. Ask if they'd like to hear it again.  Ask if they want to play again.



 
"""

import random


# V2 - Use the random module to select which adjective goes where in the story.

def random_list_item(a_list):
    random_list_item = str(random.choice(a_list))
    a_list.remove(random_list_item) # prevents words from repeating
    return random_list_item

# print(f"They say my school is haunted; my {random_list_item(adjectives)} friend {random_list_item(first_names)} says he saw a {random_list_item(adjectives)} {random_list_item(nouns)} floating at the end of the hall near the cafeteria. Some say if you {random_list_item(verbs)} down the hallway at night, you'll hear a {random_list_item(animals)} {random_list_item(verb_ings)} {random_list_item(adverbs)}. My {random_list_item(adjectives)} friend {random_list_item(first_names)} saw a {random_list_item(adjectives)} {random_list_item(nouns)} {random_list_item(verb_ings)} under one of the tables. I hope I never see any {random_list_item(pl_nouns)} {random_list_item(verb_ings)}; eating lunch there is scary enough!")


# V2 - Utilize lists

# For testing
# adjectives = ['dark', 'wet', 'slimy', 'rancid'] #need 4 adjectives
# first_names = ['Adam', 'Sarah'] #need 2 first names
# nouns = ['alley', 'trash'] # 2 nouns 
# pl_nouns = ['people']
# animals = ['cat'] #1 animal
# verbs = ['run'] # 1 verb
# verb_ings = ['tripping','smashing','playing'] # 3 verbs ending in -ing
# adverbs = ['sadly'] # 1 adv

#  Lists         min required words for mad lib
adjectives = [] #need 4 adjectives
first_names = [] #need 2 first names
nouns = [] # 2 nouns 
pl_nouns = []
animals = [] #1 animal
verbs = [] # 1 verb
verb_ings = [] # 3 verbs ending in -ing
adverbs = [] # 1 adv


participation = True

while participation is True:

    in_or_out = input("Would you like to play Mad Libs? ")
    in_or_out = str(in_or_out).lower
    # print(in_or_out)

    if in_or_out == "yes" or "y":
        adjective = input("Enter 4 adjectives seperated by commas: ")
        adjectives = adjective.split(',')
    
        first_name = input("Enter 2 first names: ")
        first_names = first_name.split(',')

        noun = input("Enter 2 nouns: ")
        nouns = noun.split(',')

        pl_noun = input("Enter 2 plural noun: ")
        pl_nouns = pl_noun.split(',')

        animal = input("Enter 2 animals: ")
        animals = animal.split(',')

        verb = input("Enter 2 verbs: ")
        verbs = verb.split(',')

        verb_ing = input("Enter 3 verbs ending with ing: (ex. swimming) ")
        verb_ings = verb_ing.split(',')

        adverb = input("Enter 2 adverbs: ")





    elif in_or_out == "no" or "n":
        print("Goodbye. ")
        participation = False



        print(f"They say my school is haunted; my {random_list_item(adjectives)} friend {random_list_item(first_names)} says he saw a {random_list_item(adjectives)} {random_list_item(nouns)} floating at the end of the hall near the cafeteria. Some say if you {random_list_item(verbs)} down the hallway at night, you'll hear a {random_list_item(animals)} {random_list_item(verb_ings)} {random_list_item(adverbs)}. My {random_list_item(adjectives)} friend {random_list_item(first_names)} saw a {random_list_item(adjectives)} {random_list_item(nouns)} {random_list_item(verb_ings)} under one of the tables. I hope I never see any {random_list_item(pl_nouns)} {random_list_item(verb_ings)}; eating lunch there is scary enough!")
