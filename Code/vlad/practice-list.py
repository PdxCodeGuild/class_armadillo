#Practice list and function
import random
#from random import randint  # if we just want randint

# April 14, 2020

## Problem 1 ####
def random_element(some_list):
    '''
    Write a function using random.randint to generate an index, 
    use that index to pick a random element of a list and return it.
    '''
    index = random.randint(0, len(some_list) - 1)  # select random index
    return some_list[index]  # return value at that index


# fruits_list = ['apples', 'bananas', 'pears', 'mango', 'grapefruit', 'peaches']
# print(random_element(fruits_list))

### Problem 2 ###
def get_numbers():
    '''
    Write a REPL which asks users for a list of numbers, 
    which they enter, until they say 'done'. 
    Then print out the list.
    '''
    numbers = []

    user_input = ''  #  str() can be used to define a blank string instead of ''
    while user_input != 'done':  # until the user enters 'done' instead of a number
        user_input = input("Enter a number (or 'done'): ")
        
        if not user_input.isalpha():  # if the user input doesn't contain letters
            user_input = int(user_input)  #  convert the input to an integer
            
            numbers.append(user_input)  # add the input to the list
    
    return numbers # after the user enters 'done', end the while loop and return numbers list

# print(get_numbers())


### Problem 3 ###
def even_evens(nums):
    '''
    Write a function that takes a list of numbers.
    Returns True if there is an even number of even numbers.
    '''
    even_number_counter = 0  # counter variable for counting even numbers

    # check each number to see if it is even
    for i in range(len(nums)):
        num = nums[i]  # variable to store the value of the list nums at the index i 

        # if num is even, count it
        if num % 2 == 0:
            even_number_counter += 1
    
    # if the count is even, return True

    # if even_number_counter % 2 == 0:   # the long way
    #     return True
    # else: 
    #     return False

    return even_number_counter % 2 == 0  # the short way

list1 = [5, 6, 2]
list2 = [5, 5, 2]

# print(even_evens(list1))  # True
# print(even_evens(list2))  # False

### Problem 4 ###
def print_every_other_with_while(nums):
    '''
    Print out every other element of a list using a while loop.
    '''
    #  split a list at every other element nums[0:-1:2] => list_name[first_index : last_index : step]  
    index = 0
    while index < len(nums):
        
        if index % 2 == 1:  # if the current value of index is odd
            del nums[index]  # delete the value from the list at the index
        
        index += 1  

    print(nums)  # after the loop is ended, print nums list

# print_every_other_with_while([0, 1, 2, 3, 4, 5, 6, 7, 8])    
# def print_every_other_with_for(nums):
    # '''
    # Print out every other element of a list using a for loop.
    # '''
#     pass