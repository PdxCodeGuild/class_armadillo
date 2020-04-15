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