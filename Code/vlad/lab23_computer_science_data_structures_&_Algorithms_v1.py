# Lab 23 Computer Science - Data Structures & Algorithms Version 1: 

""" 
# Lab 23 Computer Science - Data Structures & Algorithms

[Big-O Notation](https://en.wikipedia.org/wiki/Big_O_notation) is a measure of the complexity of an algorithm, specifically how many steps an algorithm takes depending on the size of the input. For example, performing a linear search on a list of `n` elements takes, on average, `n/2` steps, so we say a linear search is `O(n)`. We throw away multiplicative and additive factors to characterize algorithms independently of the hardware it's running on. [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
"""

# Lab 23 Computer Science - Data Structures & Algorithms
# Big-O Notation is a measure of the complexity of an algorithm, specifically how many steps an algorithm takes depending on the size of the input. For example, performing a linear search on a list of n elements takes, on average, n/2 steps, so we say a linear search is O(n). We throw away multiplicative and additive factors to characterize algorithms independently of the hardware it's running on. Big-O Cheat Sheet

# Version 1 - Linear Search
# Implement linear search, which simply loops through the given list and check if each element is equal to the value we're searching for. If it is, return the index at which it was found, otherwise, return a value indicating that it was not found.

# Example run:

#  I
# [1, 2, 3, 4, 5, 6, 7, 8]
#     I
# [1, 2, 3, 4, 5, 6, 7, 8]
#        I
# [1, 2, 3, 4, 5, 6, 7, 8]
# Stub:

# def linear_search(nums, value):
#   ...
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index) # 2

# finding the element in the list given the value

def linear_search(nums, value): # function nums is a list 
    if value not in nums:
        return None
    else:
        index = nums.index(value) # defining index nums.index(value) index is the location it is like the dictionary which we look by using the key
        return index 

    return index
    # for num in nums:
    # print(num)
    # if num == nums.index()

# nums = [1,2,3,4,5,6,7,8]
nums = [1,2,4,5,6,7,8]
index = linear_search(nums, 3) # value is the second thing being pass into the function the first object is a list 
print(index) #2 this is printing the index variable which is defined at line 37 index = nums.index(value)
# print(nums[3])
# print(nums.index(3))


       

