#lab 23 works through linear search and binary search algorithms

# Version 1 Linear Search

def linear_search(nums, value):
    for i in range(len(nums)):  #iterate over nums list
        if nums[i] == value:  # if number equals given value
            return i #return index
        else:    
            print("none")  # otherwise prints none
    return 3
nums = [1, 2, 3, 4, 5, 6, 7, 8]  #nums list
index = linear_search(nums, 3)  #index defined
print(index) #2   
#Version 2 Binary Search:

#Version 2 Pseudocode:
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

def binary_search(nums, value):
    lowest = 0 # define lowest index in list
    highest = len(nums)-1 # define highest index in list
    while lowest <= highest: #if lowest index <= highest, 
        middle = (highest + lowest) // 2 # sum lowest and highest and floor divide by 2
        if nums[middle] < target:  # if middle index is less than number we're searching for
            lowest = middle + 1  # lowest becomes middle index +1
        elif nums[middle] > target: # if middle index is > num we're searching for
            highest = middle - 1  # highest number becomes  middle number -1
        else:
            return middle  #otherwise target is middle
    return False # if loop terminates without locating value "False"                

nums = [1, 2, 3, 4, 5, 6, 7, 8] # list of nums
index = linear_search(nums, 3)  # index defined
print(index) #2