# Lab 23 Computter Science - Data Structures & Algorithms
# Troy Fitzgerald

'''Implement linear search, which simply loops through the given list 
and check if each element is equal to the value we're searching for. If
it is, return the index at which it was found, otherwise, return a value
indicating that it was not found.'''

import math

nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#user_question = int(input('What is the target you wish to know? '))

def binary_search(nums_list, target):
    low_end = 0
    up_end = len(nums_list)-1
    in_the_mid = ((low_end + up_end)/2)
    target = [nums_list] 
    while low_end < up_end:
        if (nums_list[in_the_mid] == target):
            return f'The target is {in_the_mid}'
        elif (nums_list[in_the_mid] < target):
            low_end = in_the_mid + 1
        elif (nums_list[in_the_mid] > target):
            up_end = in_the_mid - 1
        else:
            return in_the_mid
    return ('No target found')

index = binary_search(nums_list, 6)
print(index)




