import random
import matplotlib.pyplot as plt



def add(a, b):
    return a + b



def total(nums):
    r = 0
    for num in nums:
        r += num
    return(r)


def find_pair(nums, target):
    for num1 in nums:
        for num2 in nums:
            if num1 + num2 == target:
                return [num1, num2]
    return None

# # O(n^2)
# def has_duplicates(nums):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i == j:
#                 print("same number, skipping")
#                 continue
#                 print("inner loop", nums[i], "==", nums[j], "?")
#             if nums[i] == nums[j]:
#                 return True
#     return False
# has_duplicates([1,2,3,4])


# comparison between lists and stacks

class AlgorithmStepCounter:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def reset(self):
        self.counter = 0

    def value(self):
        return self.counter

    def __str__(self):
        return str(self.counter)



def has_duplicates(nums, counter):
    for i in range(len(nums)):
        for j in range(len(nums)):
            counter.increment()
            if i == j:
                continue
            if nums[i] == nums[j]:
                return True
    return False

results = []
counter = AlgorithmStepCounter()
# for n in range(1000):
#     nums = [range.randint(0, 99) for i in range(n)]
#     #nums = [i for i in range(n)]
#     has_duplicates(nums, counter)
#     results.append((n, counter.value()))
#     counter.reset

max_input_size = 400
for n in range(max_input_size):
    total = 0
    n_trials = 100
    for j in range(n_trials):
        nums = [random.randint(0, n) for i in range(n)]
        has_duplicates(nums, counter)
        total += counter.value()
        counter.reset()
        print(f"{round(n/max_input_size*100,2)}%")
        results.append((n, total / n_trials))

print(results)
# split the data into x and y vlaues
x = [result[0] for result in results]
y = [result[1] for result in results]

# make a chart
plt.plot(x, y)
plt.show()

# binary search O(log(n))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] input list - must be sorted for the algorithm to work
# what is the index of 8?
# step 1 - establish lower and upper bound
#  L=0                        U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step 2 - calculate the mid (lower + upper) // 2
#  L=0         M=4            U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step 3 - check if nums[M] < target (5 < 8) - we know 8 is between M and U
#  L=0         M=4            U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step 4 - update the lower and upper bound
#              L=4            U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step 5 - calculate the mid (lower + upper) // 2
#              L=4   M=6      U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step 6 - check if nums[M] < target (7 < 8) - we know 8 is between M and U
#              L=4   M=6      U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step 7 - update the lower and upper bound
#                    L=6      U=9
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# step 8 - calculate the mid (lower + upper) // 2
#                    L=6 M=7   U=9
# [1, 2, 3, 4, 5, 6, 7,  8, 9, 10]
# step 9 the value at M is our target, return M