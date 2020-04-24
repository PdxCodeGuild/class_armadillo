"""

Lab 2: Mad Libs=====================================================================================
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Instructions
1. Search the interwebs for an example Mad Lib
2. Ask the user for each word you'll put in your Mad Lib
3. Use string concatenation to put each word into the Mad Lib

"""

print("Let's play Madlibs!")

adj1 = input("Enter an adjective. ")
first_name = input("Enter a first name. ")
adj2 = input("Enter another adjective. ")
noun1 = input("Enter a noun. ")
verb1 = input("Enter a verb. ")
animal = input("Enter an animal name. ")
verbing = input("Enter a verb ending with -ing. ")
adverb = input("Enter an adverb. ")
adj3 = input("Enter an adjective. ")
first_name2 = input("Enter another first name. ")
adj4 = input("Enter another adjective. ")
noun2 = input("Enter another noun. ")
verbing2 = input("Enter another verb ending in -ing. ")
plnoun = input("Enter a plural noun. ")
verbing3 = input("Enter one more verb ending in -ing. ")

print(f"They say my school is haunted; my {adj1} friend {first_name} says he saw a {adj2} {noun1} floating at the end of the hall near the cafeteria. Some say if you {verb1} down the hallway at night, you'll hear a {animal} {verbing} {adverb}. My {adj3} friend {first_name2} saw a {adj4} {noun2} {verbing2} under one of the tables. I hope I never see any {plnoun} {verbing3}; eating lunch there is scary enough!")
