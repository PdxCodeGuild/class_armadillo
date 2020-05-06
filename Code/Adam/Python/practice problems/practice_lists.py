"""
List Practice Problems
"""

""" Problem 1 """
#   Write a function using random.randint to generate an index, use that index to pick a random element of a 
# list and return it.

import random 

#   input a list, ouput a random element of the list
def random_element(a_list):
    index = random.randint(0, 2) # generate a random integer 
    # generate a random int within a range equal to the length of the list
    # use the random index to pick an element of the list
    return a_list[index]


# print(random_element(['apples', 'bananas', 'pears'])) # 'apples', 'bananas' or 'pears'


""" Problem 2 """
#   Write a REPL (read, evaluate, print, loop) which asks users for a list of numbers, which they enter, until 
# they say 'done'. Then print out the list.



# example run -----------------
# Enter a number (or 'done'): 5
# Enter a number (or 'done'): 34
# Enter a number (or 'done'): 515
# Enter a number (or 'done'): done
# [5, 34, 515]

""" Problem 3 """
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.