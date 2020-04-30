"""
Think Python Notes
"""
import random
import math
import time
import string


person = input('Enter a person: ')

# the input is initially a string
# adjectives = input('Enter two adjectives seperated by a comma. ')
adjectives = 'motivated,discouraged' # for testing
print(adjectives) # is 1 string
print(type(adjectives)) 


# the input is converted to a list
adjectives = adjectives.split(',')
print(adjectives) # is now a list containing 2 strings
print(type(adjectives)) 


# will print the word in adjectives with the coresponding index  
print(adjectives[0]) # prints 
print(adjectives[1])

adjective1, adjective2 = input('Enter two adjectives, seperated by a coma: ').split(',')

print(adjective1, adjective2)