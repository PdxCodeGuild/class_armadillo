


import random
import math

# https://en.wikipedia.org/wiki/Arithmetic_mean
def mean(nums):
    total = 0
    for num in nums:
        total += num
    return total / len(nums)

# https://en.wikipedia.org/wiki/Variance
def variance(nums):
    average = mean(nums)
    total = 0
    for num in nums:
        total += (num - average) ** 2
    return total / len(nums)

# https://en.wikipedia.org/wiki/Standard_deviation
def standard_deviation(nums):
    return math.sqrt(variance(nums))

nums = [random.randint(1, 99) for _ in range(100)]
print(f'The mean is {mean(nums)}')
print(f'The variance is {variance(nums)}')
print(f'The standard deviation is {standard_deviation(nums)}')
