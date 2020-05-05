​
import random
import matplotlib.pyplot as plt
​
# Big-O Notation is a measure of an algotihm's complexity
# independent of details about the implementation or hardware
# O(2*n) == O(n+100) == O(n) we don't care about multiplicative or additive factors
# O(5n^2 + 6n + 3) == O(n^2)
# https://en.wikipedia.org/wiki/Big_O_notation
​
​
# this algorithm takes 1 step
# O(1) - constant time
# e.g. using an index to access an element out of a list
# e.g. using a key to get a value out of a dictionary
# e.g. id(), arithmetic operators
def add(a, b):
    return a + b
​
# for n numbers, this algorithms takes n steps
# this means total is O(n)
# O(2*(assignment + forloop_setup + n*addition + n*assignment + return))
# O(n)
# e.g. 'hello world'.find('o')
# e.g. 'a b c d'.split()
# e.g. 'abcdabc'.count('a')
def total(nums):
    r = 0
    for num in nums:
        r += num
    return r
​
# def count(text, to_find):
#     counter = 0
#     for char in text:
#         if char == to_find:
#             counter += 1
#     return counter
# print(count('hello world').count('o'))
​
​
​
# for n numbers, this algorithm takes n^2 steps
# this means find_pair is O(n^2)
def find_pair(nums, target):
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == target:
                return [num1, num2]
    return None
​
# O(n^2)
# def has_duplicates(nums):
#     for i in range(len(nums)):
#         print('outer loop', nums[i])
#         for j in range(len(nums)):
#             if i == j:
#                 print('same number, skipping')
#                 continue
#             print('inner loop', nums[i], '==', nums[j], '?')
#             if nums[i] == nums[j]:
#                 return True
#     return False
# has_duplicates([1, 2, 3, 4])
​
​
​
# comparison between lists and stacks
​
class AlgorithmStepCounter:
    def __init__(self):
        self.counter = 0
    
    def increment(self):
        self.counter += 1
    
    def reset(self):
        self.counter = 0
    
    def value(self):
        return self.counter
​
    def __str__(self):
        return str(self.counter)
​
​
​
​
​
​
def has_duplicates(nums, counter):
    for i in range(len(nums)):
        for j in range(len(nums)):
            counter.increment()
            if i == j:
                continue
            if nums[i] == nums[j]:
                return True
    return False
​
results = []
counter = AlgorithmStepCounter()
# for n in range(1000):
#     nums = [random.randint(0, 99) for i in range(n)] # average case
#     # nums = [i for i in range(n)] # worse case - no duplicates - has_duplicates takes n^2 steps
#     has_duplicates(nums, counter)
#     results.append((n, counter.value()))
#     counter.reset()
​
max_input_size = 400
for n in range(max_input_size):
    total = 0
    n_trials = 100
    for j in range(n_trials):
        nums = [random.randint(0, n) for i in range(n)] # average case
        has_duplicates(nums, counter)
        total += counter.value()
        counter.reset()
    print(f'{round(n/max_input_size*100,2)}%')
    results.append((n, total / n_trials))
​
​
print(results)
# split our data into x and y values
x_values = [result[0] for result in results]
y_values = [result[1] for result in results]
​
​
# make a fancy chart
plt.plot(x_values, y_values)
plt.show()
​
​
​
​
# binary search O(log(n))
​
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] input list - must be sorted for the algorithm to work
# what is the index of 8?
​
# step 1 - establish lower and upper bound
#  L=0                        U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
​
# step 2 - calculate the mid (lower + upper) // 2
#  L=0         M=4            U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
​
# step 3 - check if nums[M] < target (5 < 8) - we know 8 is between M and U
#  L=0         M=4            U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
​
# step 4 - update the lower and upper bound
#              L=4            U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
​
# step 5 - calculate the mid (lower + upper) // 2
#              L=4   M=6      U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
​
# step 6 - check if nums[M] < target (7 < 8) - we know 8 is between M and U
#              L=4   M=6      U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
​
# step 7 - update the lower and upper bound
#                    L=6      U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
​
# step 8 - calculate the mid (lower + upper) // 2
#                    L=6 M=7   U=9
# [1, 2, 3, 4, 5, 6, 7,  8, 9, 10]
​
# step 9 the value at M is our target, return 