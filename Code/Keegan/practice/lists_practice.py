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
    every_other = []
    index = 0
    while index < len(nums):
        
        if index % 2 == 0:  # if the current value of index is even
            every_other.append(nums[index])  # [0, 2, 4, 6, 8]
            
            # del nums[index]  # delete the value from the list at the index.
            # deleting from the original list doesn't work in this case
            # because it changes the length of the list over which we are iterating,
            # therefore giving us weird results
        
        index += 1  

    print(every_other)  # after the loop is ended, print nums list
    return

# print_every_other_with_while([0, 1, 2, 3, 4, 5, 6, 7, 8]) 
# num_list = [random.randint(1,100) for i in range(1,10)]  # list comprehension for creating a list with 10 random integers between 1 and 10
# print_every_other_with_while(num_list)

# -------------------------- #
# April 15, 2020

# same as above but with a for loop
def print_every_other_with_for(nums):
    '''
    Print out every other element of a list using a for loop.
    '''
    new_list = []  # create an empty list to hold our new values
    for i in range(0, len(nums), 2):  # loop through every other index of our original list, using range(start, stop, step=2)
        new_list.append(nums[i]) # append the value at every other index to our new list

    print(new_list)  # print the list at the end of the loop
    return

# print_every_other_with_for([0, 1, 2, 3, 4, 5, 6, 7, 8][::-1]) # [::-1] at the end of a list will reverse it
# num_list = [random.randint(1,100) for i in range(0,10)]  # list comprehension for creating a list with 10 random integers between 1 and 10
# print(num_list)
# print_every_other_with_while(num_list)


# Problem 5

def reverse(nums):
    '''
    Write a function that returns the reverse of a list.
    '''
    #return nums[::-1] # fancy split notation
    # nums.reverse() # fance list method to reverse a list in place 
    # return nums
 
    new_list = [] # holder for new list
    for i in range(len(nums) - 1, -1, -1):  # start the range at the end of the list, count down to the beginning, subtracting 1 each time
        new_list.append(nums[i])  # add the element from the original list at the current index to the new list
    
    return new_list

# num_list = [1, 2, 3]
# print(reverse(num_list))

# Problem 6

def extract_less_than_ten(nums):
    '''
    Write a function to move all the elements of a list 
    with value less than 10 to a new list and return it.
    '''

    less_than_ten = [] # empty list for storing new values

    # loop through each element in the list
    for index in range(len(nums)): 
        num = nums[index]  # variable for the current value of the list at the current index
        if num < 10: # if the value is num is less than 10, add it to the new list
            less_than_ten.append(num)  

    return less_than_ten

# nums_list = [random.randint(1,100) for i in range(0,100)]
# print(nums_list)
# nums_list = [2, 8, 12, 18]
# print(extract_less_than_ten(nums_list)) # [2, 8]


# Problem 7

def common_elements(nums1, nums2):
    '''
    Write a function to find all common elements between two lists.
    '''
    # return set(nums1).intersection(nums2)  # fancy way using sets, though doesn't work with multiple recurring values in the lists

    # find the smaller of the two lists
    if len(nums1) < len(nums2):
        short_list = nums1
    else:
        short_list = nums2 

    # check each value of the smaller list to see if it was in the larger

    # if it is, add to new list


nums1 = [1, 2, 3, 2]
nums2 = [2, 3, 4, 3]

print(common_elements(nums1, nums2))

# -------------------------- #
# April 16, 2020

# Problem 12

# [n+1] = n + [n-1]
def fibonacci(n):
    '''
    Returns the first n Fibonacci Numbers
    '''
    fib = []

    for i in range(0, n):
        if i < 2:
            fib.append(1)
        else:
            next = fib[i - 1] + fib[i - 2]
            fib.append(next)
    return fib
    
# print(fibonacci(8))

def fibonacci_recursive(n, fib = []):
    '''
    Recursively generate n Fibonacci numbers
    '''
   
    index = len(fib) - 1   # current index is the last index in the list

    if len(fib) < 2:       # the first two values in the fib sequence are 1
        fib.append(1)
    else:
        # every other value is the sum of the previous two
        fib.append(fib[index] + fib[index - 1])  
    
    # if our list is n items long, return the list
    if len(fib) == n:
        return fib

    # otherwise, call fib_rec() again with n and the new list
    return fibonacci_recursive(n, fib)


# print(fibonacci_recursive(8))



# Problem 13

def minimum(nums):
    # return min(nums)   # one line solution using Python's min()
    nums = sorted(nums)  # sort the list
    return nums[0]

def maximum(nums):
    # return max(nums)   # one line solution using Python's max()
    nums = sorted(nums)  # sort the list
    return nums[-1]

def mean(nums):
    total = 0

    # for index in range(0, len(nums)):   # another way to write our loop
    #     total += nums[index]

    for num in nums:
        total += num
    
    return total / len(nums)

def mode(nums):
    # dictionary that will store each number and the number of times it occurs
    num_occurences = {}  

    # loop through all numbers in the list
    for num in nums:

        # string representation of the current number in the list
        cur_key = str(num)  

        # if the current num is not a key in the dict
        if cur_key not in num_occurences:
            # create the key
            num_occurences[cur_key] = 1
        
        # if the current num IS a key, increment its occurence value
        else:
            num_occurences[cur_key] += 1
    
    cur_mode = str(nums[0])

    for key in num_occurences:
        if num_occurences[key] > num_occurences[cur_mode]:
            cur_mode = key

  # return (key, value)
    return (int(cur_mode), num_occurences[cur_mode])
    
nums = [random.randint(1, 10) for i in range(10)]  # list comprehension generate 10 numbers

# print(f"{nums = }")
# print(mode(nums))
# print(f"Average: {mean(nums)}")
# print(minimum(nums))



# Problem 14
