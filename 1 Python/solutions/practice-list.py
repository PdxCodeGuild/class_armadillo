

import random

def random_list(a, b, n):
    return [random.randint(a, b) for i in range(n)]

# print(random_list(1, 100, 100))


# Problem 1
#
# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.
#
# def random_element(a):
#     ...
#
# fruits = ['apples', 'bananas', 'pears']
# random_element(fruits) could return 'apples', 'bananas' or 'pears'
#


# Problem 2
#
# Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.
#
# Enter a number (or 'done'): 5
# Enter a number (or 'done'): 34
# Enter a number (or 'done'): 515
# Enter a number (or 'done'): done
# [5, 34, 515]
#


# Problem 3
#
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.
#
# eveneven([5, 6, 2]) → True
# eveneven([5, 5, 2]) → False
#



def eveneven(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count % 2 == 0


# print(eveneven([5, 6, 2]))
# print(eveneven([5, 5, 2]))
#
# import random
# for j in range(10):
#     nums = [random.randint(1,10) for i in range(10)]
#     print(nums)
#     print(eveneven(nums))
#     print()



# Problem 4
#
# Print out every other element of a list, first using a while loop, then using a for loop.
#
# >>> nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# >>> print_every_other(nums)
# 0, 2, 4, 6, 8
#


# Problem 5
#
# Write a function that returns the reverse of a list.
#
# def reverse(nums):


# Problem 6
#
# Write a function to move all the elements of a list with value less than 10 to a new list and return it.
#
# def extract_less_than_ten(nums):


# Problem 7
#
# Write a function to find all common elements between two lists.
#
# def common_elements(nums1, nums2):

def common_elements(nums1, nums2):
    common = []
    nums2 = nums2.copy()
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                common.append(nums1[i])
                nums2.pop(j)
                # del nums2[j]
                break

    return common



# print(common_elements([1, 2, 3], [2, 3, 4]))
# print(common_elements([1, 2, 3], [4, 5, 6]))
#
# nums1 = random_list(1, 10, 10)
# nums2 = random_list(1, 10, 10)
# nums1.sort()
# nums2.sort()
# nums1 = [3, 3, 3, 4, 4, 6, 7, 7, 8, 9, 10]
# nums2 = [2, 3, 4, 4, 5, 5, 8, 9, 9, 10]
# print(nums1)
# print(nums2)
# print(common_elements(nums1, nums2))






# Problem 8
#
# Write a function to combine two lists of equal length into one, alternating elements.
#
# def combine(nums1, nums2):
#     ...
# combine(['a','b','c'],[1,2,3]) → ['a', 1, 'b', 2, 'c', 3]
#


# Problem 9
#
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
#
# nums = [5, 6, 2, 3]
# target = 7
# find_pair(nums, target) → [5, 2]
#
# Optional: return a list of all pairs of numbers that sum to a target value.


# Problem 10
#
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
#
# merge([5,2,1], [6,8,2]) → [[5,6],[2,8],[1,2]]
#


# Problem 11
#
# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
#
# nums = [[5,2,3],[4,5,1],[7,6,3]]
# combine_all(nums) → [5,2,3,4,5,1,7,6,3]
#


# Problem 12
#
# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
#
# fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(n):
    fib = []
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

print(fibonacci(10))




# Problem 13
#
# Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
#
# def minimum(nums):
#     ...
#
# def maxmimum(nums):
#     ...
#
# def mean(nums):
#     ...
#
# def mode(nums): # (OPTIONAL)
#     ...
#


# Problem 14
#
# Write a function which takes a list as a parameter and returns a new list with all the numbers that are duplicates
#
# def find_unique(nums):
#     ...
# nums = [1, 2, 2, 3]
# unique_nums = find_unique(nums) → [1, 3]




# def duplicates(nums):
    # dups = []
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j]:
    #             dups.append(nums[i])
    #             dups.append(nums[j])
    #             break
    # return dups


# [1, 2, 2, 3, 3, 3, 4, 4, 5]
# [F, T, T, T, T, T, T, T, F]
def duplicates(nums):
    bs = []
    for i in range(len(nums)):
        b = False
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                b = True
                break
        bs.append(b)

    dups = []
    for i in range(len(bs)):
        if bs[i]:
            dups.append(nums[i])

    return dups

# print(duplicates([1, 2, 2, 3, 3, 3, 4, 4, 5]))


# test_list = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6]
# print(test_list)
# print(duplicates(test_list))
#
# for i in range(10):
#     nums = random_list(1, 10, 10)
#     print(nums)
#     print(duplicates(nums))
#     print()
