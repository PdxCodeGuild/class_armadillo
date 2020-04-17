#function practice 

'''Problem 12
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

# def double_letters(word):
#     '''
#     Double every character in a string and return the result
#     '''
#     return ''.join([a*2 for a in word])

# # print(double_letters("hello"))

# def latest_letter(word):
#     return sorted(word)[-1]

# # print(latest_letter("pneumonoultramicroscopicsilicovolcanoconiosis"))

# def count_letter(letter, word):
#     '''
#     Return the number of instances of a letter in a string
#     '''
#     return len([char for char in word if char == letter])

# # print(count_letter("i", "pneumonoultramicroscopicsilicovolcanoconiosis"))
# # print(count_letter("l", "hello"))

# def print_powers_2(n):
#     print(', '.join([str(2 ** i) for i in range(n)]))

