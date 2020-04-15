#Practice Problems: Lists on April 15, 2020


""""
Practice Problems: Lists https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/practice/practice03-lists.md

""""

# Problem 5
# Write a function that returns the reverse of a list.
def reverse(nums):
    nums.reverse()
    return nums
# print(reverse([1, 2, 3])) # 3, 2, 1

# Problem 6
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.
def extract_less_than_ten(nums):
    new_list = []

    for num in nums:
        if num < 10:
            new_list.append(num)
    return new_list
# print(extract_less_than_ten([2, 8, 12, 18])) # [2, 8]

# Problem 7
# Write a function to find all common elements between two lists.
def common_elements(nums1, nums2):
    new_list = []
    for num1 in nums1:
        print(num1)
        for num2 in nums2:
            print(num2)
            if num1 == num2:
                new_list.append(num1)
    return new_list
# print(common_elements([1, 2, 3], [2, 3, 4])) # [2, 3]


# Problem 8
# Write a function to combine two lists of equal length into one, alternating elements.
def combine(letters, nums):
    new_list = []
        
    i = 0
    while i <= len(letters)-1:
        new_list.append(letters[i])
        new_list.append(nums[i])
        i+=1
    print(new_list)

    # for i in range(0,len(letters)-1,3):
    #     new_list.append(letters[i])
    #     new_list.append(nums[i])
    # print(new_list)
# print(combine(['a','b','c'],[1,2,3])) # ['a', 1, 'b', 2, 'c', 3]


# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number. Optional: return a list of all pairs of numbers that sum to a target value.

# range(start,stop,step)
def find_pair(nums, target):
    new_list = []
    # for i in range(0,len(nums),1):
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == target:
               new_list.append(num1)
    return new_list
# print(find_pair([5, 6, 2, 3], 7)) # [5, 2]
        
        
# Problem 10
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
def merge(nums1, nums2):
    new_list = []

    for i in range(0,len(nums1),1):
        new_list.append([nums1[i], nums2[i]])
    return new_list
# print(merge([5,2,1], [6,8,2])) # [[5,6],[2,8],[1,2]]

# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
def combine_all(nums):
    new_list = []
    for num1 in nums:
        for num2 in num1:
            new_list.append(num2)
    return new_list

# print(combine_all([[5,2,3],[4,5,1],[7,6,3]])) # [5,2,3,4,5,1,7,6,3]

# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
# a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
def fibonacci(n):
    
# print(fibonacci(8)) # [1, 1, 2, 3, 5, 8, 13, 21]


####################################################################################################


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
