# Practice Fibonacci and Max , Min and Mean

''Problem 12
Write a function that takes n as a parameter, and 
returns a list containing the first n Fibonacci Numbers.'''

def fibonacci(n):
    
    nums = [1, 1]
    for i in range(2,n):
    print(i, i-1, i-2)
        nums.append(nums[i-1] + nums[i-2]) 
    return(nums)

print(fibonacci(15)) # [1, 1, 2, 3, 5, 8, 13, 21]

'''Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
def minimum(nums):
    ...
def maxmimum(nums):
    ...
def mean(nums):
    ...
def mode(nums): # (OPTIONAL)
    ...'''

def minimum(nums):
    nums.sort()
    return nums[0]
        
print(minimum([2, 1, 3]))


def maximum(nums):
    nums.sort()
    return nums[-1]

print(maximum([2, 1, 3]))

def mean(nums):
    total = 0
    for i in range(len(nums)):
        total += nums[i]
    total = total / len(nums)
    return total

print(mean([2, 1, 3]))   
© 2020 GitHub, Inc.