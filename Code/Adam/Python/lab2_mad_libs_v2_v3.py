"""
Lab 2: Mad Libs ===============================================================

  Write a simple program that prompts the user for several inputs then prints a 
  Mad Lib as the result.

Version 2 (optional)
- Make a functional solution that utilizes lists. For example, ask the user for 
  3 adjectives, separated by commas, then use the .split() function to store each 
  adjective and later use it in your story.
- Add randomness! Use the random module, rather than selecting which adjective 
  goes where in the story.

Version 3 (optional)

- Make it a repeatable game. Once you're done prompting the user for words, prompt 
  them for whether they'd like to hear the story. Use a while loop to keep asking 
  if they'd like to hear the story again until the answer is 'no'. You could then 
  ask them if they'd like to make another story, and so on.
"""


import random # V2 - for random selection from a list.


adjectives = [] # V2 - utilize lists.
pl_nouns = []
verbs_ing =  []


while True:
  response = input('Would you like to play Mad Libs? yes or no: ').lower() # make lowercase
  if response == 'yes': # V3 - make the game repeatable
    # V2 - ask the user for 3 adjectives, separated by commas.
    #    - use the .split() function to store each adjective and later use it in your story.
    adj_1, adj_2 = input('Enter two adjectives, seperated by a coma: ').split(',') 
    # adj_1, adj_2 = 'happy,sad'.split(',') # for testing
    adjectives = [adj_1, adj_2]
    ## Testing
    # print(adjectives)
    # print(random.choice(adjectives))


    pl_noun_1, pl_noun_2, pl_noun_3 = input('Enter three pl_nouns, seperated by a coma: ').split(',')
    # pl_noun_1, pl_noun_2, pl_noun_3 = 'men,women,children'.split(',') # for testing
    pl_nouns = [pl_noun_1, pl_noun_2, pl_noun_3] 
    ## Testing
    # print(pl_nouns)
    # print(random.choice(pl_nouns))


    verb_ing_1, verb_ing_2 = input('Enter two verbs ending in ing, seperated by a coma: ').split(',')
    # verb_ing_1, verb_ing_2 = 'running,skipping'.split(',') # for testing
    verbs_ing = [verb_ing_1, verb_ing_2] 
    ## Testing
    # print(verbs_ing)
    # print(random.choice(verbs_ing))

    # original_qute = "The best leaders are those most interested in surrounding themselves with assistants and associates smarter than they are. They are frank in admitting this and are willing to pay for such talents.\" -Antos Parrish"

    again = 'yes'
    while again == 'yes': # allow the user to hear the story again
      madlib = f"\nThe {random.choice(adjectives)} {random.choice(pl_nouns)} are those most interested in {random.choice(verbs_ing)} themselves with {random.choice(pl_nouns)} and {random.choice(pl_nouns)} smarter than they are. They are {random.choice(adjectives)} in admitting this and are {random.choice(verbs_ing)} to pay for such talents.\" -Some weirdo\n"
      print(madlib)

      again = input('Would you like to hear the story again? yes or no: ')
  elif response == 'no':
    break