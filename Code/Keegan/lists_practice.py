import random
#from random import randint  # if we just want randint


def random_element(some_list):
    index = random.randint(0, len(some_list) - 1)  # select random index
    return some_list[index]  # return value at that index


# fruits_list = ['apples', 'bananas', 'pears', 'mango', 'grapefruit', 'peaches']
# print(random_element(fruits_list))


def get_numbers():

    numbers = []

    user_input = ''  #  str() can be used to define a blank string instead of ''
    while user_input != 'done':  # until the user enters 'done' instead of a number
        user_input = input("Enter a number (or 'done'): ")
        
        if not user_input.isalpha():  # if the user input doesn't contain letters
            user_input = int(user_input)  #  convert the input to an integer
            
            numbers.append(user_input)  # add the input to the list
    
    return numbers # after the user enters 'done', end the while loop and return numbers list

# print(get_numbers())



def even_evens(nums):

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

# with while loop
def print_every_other_with_while(nums):
    #  split a list at every other element nums[0:-1:2] => list_name[first_index : last_index : step]  
    index = 0
    while index < len(nums):
        
        if index % 2 == 1:  # if the current value of index is odd
            del nums[index]  # delete the value from the list at the index
        
        index += 1  

    print(nums)  # after the loop is ended, print nums list

# print_every_other_with_while([0, 1, 2, 3, 4, 5, 6, 7, 8])    
# def print_every_other_with_for(nums):
#     pass