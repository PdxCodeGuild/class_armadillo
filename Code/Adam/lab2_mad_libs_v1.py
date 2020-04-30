"""

Lab 2: Mad Libs=====================================================================================
Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

Instructions
1. Search the interwebs for an example Mad Lib
2. Ask the user for each word you'll put in your Mad Lib
3. Use string concatenation to put each word into the Mad Lib

"""


# madlib words that need to be enterd by user
adj_1 = input('Enter an adjective: ')
adj_2 = input('Enter another adjective: ')
noun_1 = input('Enter a noun: ')
noun_2 = input('Enter another noun: ')
noun_3 = input('Enter one more noun: ')
verb_ing_1 = input('Enter a verb ending in ing: ')
verb_ing_2 = input('Enter another verb ending in ing: ')

# original_quote = "The best leaders are those most interested in surrounding themselves with assistants and associates smarter than they are. They are frank in admitting this and are willing to pay for such talents.\" -Antos Parrish"
# store f string in madlib
madlib = f"The {adj_1} {noun_1} are those most interested in {verb_ing_1} themselves with {noun_2} and {noun_3} smarter than they are. They are {adj_2} in admitting this and are {verb_ing_2} to pay for such talents.\" -Somebody"

#display madlib
print(madlib)