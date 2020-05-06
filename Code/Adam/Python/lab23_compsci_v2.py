"""
Lab 23 Computer Science - Data Structures & Algorithms

Big-O Notation is a measure of the complexity of an algorithm, specifically how 
many steps an algorithm takes depending on the size of the input. For example, 
performing a linear search on a list of n elements takes, on average, n/2 steps, 
so we say a linear search is O(n). We throw away multiplicative and additive 
factors to characterize algorithms independently of the hardware it's running on. 


Version 2 - Binary Search

Implement binary search, which requires that a list is sorted. Begin by defining 
two indices: low and high. Initialize low as the lowest index in the list and 
high as the highest. Loop while low is less then high. For each iteration, calculate 
a third index mid which is in the middle between low and high. If the element at mid 
is the one you're searching for, return it, otherwise check if the target value is 
less than or greater than the one at mid. If it's less, make high equal to mid and 
loop. If it's greater, make low equal to mid and loop. If the loop terminates 
without returning, return a value indicating that it was not found.

Example run:

 L        M           H
[1, 2, 3, 4, 5, 6, 7, 8]
 L  M     H
[1, 2, 3, 4, 5, 6, 7, 8]
    L  M  H
[1, 2, 3, 4, 5, 6, 7, 8]

Psuedocode:

// A - the list
// n - the length of the list
// T - the value we're searching for
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful


Stub:


def binary_search(nums, value):
  ...
nums = [1, 2, 3, 4, 5, 6, 7, 8]
index = binary_search(nums, 3)
print(index) # 2

"""
import random

def binary_search(nums, num):
    while nums[0] < nums[-1]:
        print(nums[0]) # prints the char at index 0
        print(nums.index(nums[0])) # prints the index at 1
        low = nums.index(nums[0]) # 
        print(f'low is: {low}')
        print(nums[-1])
        print(nums.index(nums[-1]))
        high = nums.index(nums[-1])
        print(f'high is: {high}')
        mid = int(len(nums)/2)
        print(f'mid is: {mid}')
        break
        # if num in range(low, mid):
        #     nums = [0:mid:] 
        #     print(nums)
        #     print('the number is lower than mid')
        # elif num in range(mid, high):
        #     nums = []
        #     print(nums)
        #     print('the number is higher than mid')
        # elif num == mid:
        #     return print(f'num is: {mid}')
        

nums = [1, 2, 3, 4, 5, 6, 7, 8]
num = 2
binary_search(nums, num)