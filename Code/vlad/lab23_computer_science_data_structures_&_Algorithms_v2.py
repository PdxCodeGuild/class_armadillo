# Lab 23 Computer Science - Data Structures & Algorithms Version 2: 


# Version 2 - Binary Search
# Implement binary search, which requires that a list is sorted. Begin by defining two indices: low and high. Initialize low as the lowest index in the list and high as the highest. Loop while low is less then high. For each iteration, calculate a third index mid which is in the middle between low and high. If the element at mid is the one you're searching for, return it, otherwise check is the target value is less than or greater than the one at mid. If it's less, make high equal to mid and loop. If it's greater, make low equal to mid and loop. If the loop terminates without returning, return a value indicating that it was not found.

import math

def binary_search(nums, value): # # defining index nums.index(value) index is the location it is like the dictionary which we look by using the key
    nums.sort()
    low = nums[0] # to get the lower value in the index
    high = nums[-1] # to get the highest value in the index
    # print(low)
    # print(high)
    mid = int(len(nums) /2) #get
    # print(mid)
    while low <= high: 
        x = math.floor((low + high) / 2)
        if nums[x] < value:
            low = x + 1
        elif nums[x] > value:
            high = x - 1
        else:
            return x
    return None


nums = [5,6,8,7,1,2,3,4]    
index = binary_search(nums, 3) # need to put the debugger where the function is called s
print(nums) # [1, 2, 3, 4, 5, 6, 7, 8]
print(index)


# Example run:

#  L        M           H
# [1, 2, 3, 4, 5, 6, 7, 8]
#  L  M     H
# [1, 2, 3, 4, 5, 6, 7, 8]
#     L  M  H
# [1, 2, 3, 4, 5, 6, 7, 8]
# Psuedocode:

# // A - the list
# // n - the length of the list
# // T - the value we're searching for
# function binary_search(A, n, T) is
#     L := 0
#     R := n − 1
#     while L ≤ R do
#         m := floor((L + R) / 2)
#         if A[m] < T then
#             L := m + 1
#         else if A[m] > T then
#             R := m - 1
#         else:
#             return m
#     return unsuccessful
# Stub:

# def binary_search(nums, value):
#   ...
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# index = linear_search(nums, 3)
# print(index) # 2


# import random
# import matplotlib.pyplot as plt

# # Big-O Notation is a measure of an algotihm's complexity
# # independent of details about the implementation or hardware
# # O(2*n) == O(n+100) == O(n) we don't care about multiplicative or additive factors
# # O(5n^2 + 6n + 3) == O(n^2)
# # https://en.wikipedia.org/wiki/Big_O_notation


# # this algorithm takes 1 step
# # O(1) - constant time
# # e.g. using an index to access an element out of a list
# # e.g. using a key to get a value out of a dictionary
# # e.g. id(), arithmetic operators
# def add(a, b):
#     return a + b

# # for n numbers, this algorithms takes n steps
# # this means total is O(n)
# # O(2*(assignment + forloop_setup + n*addition + n*assignment + return))
# # O(n)
# # e.g. 'hello world'.find('o')
# # e.g. 'a b c d'.split()
# # e.g. 'abcdabc'.count('a')
# def total(nums):
#     r = 0
#     for num in nums:
#         r += num
#     return r

# # def count(text, to_find):
# #     counter = 0
# #     for char in text:
# #         if char == to_find:
# #             counter += 1
# #     return counter
# # print(count('hello world').count('o'))



# # for n numbers, this algorithm takes n^2 steps
# # this means find_pair is O(n^2)
# def find_pair(nums, target):
#     for num1 in nums:
#         for num2 in nums:
#             if num1 + num2 == target:
#                 return [num1, num2]
#     return None

# # O(n^2)
# # def has_duplicates(nums):
# #     for i in range(len(nums)):
# #         print('outer loop', nums[i])
# #         for j in range(len(nums)):
# #             if i == j:
# #                 print('same number, skipping')
# #                 continue
# #             print('inner loop', nums[i], '==', nums[j], '?')
# #             if nums[i] == nums[j]:
# #                 return True
# #     return False
# # has_duplicates([1, 2, 3, 4])



# # comparison between lists and stacks

# class AlgorithmStepCounter:
#     def __init__(self):
#         self.counter = 0
    
#     def increment(self):
#         self.counter += 1
    
#     def reset(self):
#         self.counter = 0
    
#     def value(self):
#         return self.counter

#     def __str__(self):
#         return str(self.counter)






# def has_duplicates(nums, counter):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             counter.increment()
#             if i == j:
#                 continue
#             if nums[i] == nums[j]:
#                 return True
#     return False

# results = []
# counter = AlgorithmStepCounter()
# # for n in range(1000):
# #     nums = [random.randint(0, 99) for i in range(n)] # average case
# #     # nums = [i for i in range(n)] # worse case - no duplicates - has_duplicates takes n^2 steps
# #     has_duplicates(nums, counter)
# #     results.append((n, counter.value()))
# #     counter.reset()

# max_input_size = 400
# for n in range(max_input_size):
#     total = 0
#     n_trials = 100
#     for j in range(n_trials):
#         nums = [random.randint(0, n) for i in range(n)] # average case
#         has_duplicates(nums, counter)
#         total += counter.value()
#         counter.reset()
#     print(f'{round(n/max_input_size*100,2)}%')
#     results.append((n, total / n_trials))


# print(results)
# # split our data into x and y values
# x_values = [result[0] for result in results]
# y_values = [result[1] for result in results]


# # make a fancy chart
# plt.plot(x_values, y_values)
# plt.show()




# # binary search O(log(n))

# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] input list - must be sorted for the algorithm to work
# # what is the index of 8?

# # step 1 - establish lower and upper bound
# #  L=0                        U=9
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # step 2 - calculate the mid (lower + upper) // 2
# #  L=0         M=4            U=9
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # step 3 - check if nums[M] < target (5 < 8) - we know 8 is between M and U
# #  L=0         M=4            U=9
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # step 4 - update the lower and upper bound
# #              L=4            U=9
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # step 5 - calculate the mid (lower + upper) // 2
# #              L=4   M=6      U=9
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # step 6 - check if nums[M] < target (7 < 8) - we know 8 is between M and U
# #              L=4   M=6      U=9
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # step 7 - update the lower and upper bound
# #                    L=6      U=9
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # step 8 - calculate the mid (lower + upper) // 2
# #                    L=6 M=7   U=9
# # [1, 2, 3, 4, 5, 6, 7,  8, 9, 10]

# # step 9 the value at M is our target, return M