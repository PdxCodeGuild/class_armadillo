
# Implement linear search, which simply loops through the 
# given list and check if each element is equal to the value
#  we're searching for. If it is, return the index at which 
#  it was found, otherwise, return a value indicating that 
#  it was not found.

#defining fuction "linear_search" with 2 parameters  "num" and "value"
def linear_search(colors,value):
    #  check if each element is equal to the value
    #  we're searching for.
    if value in colors:
        index = colors.index(value)
        return index
#         in operator : The 'in' operator is used to check if 
#         a value exists in a sequence or not. 
#         which simply loops through the  given list and 
colors = ["red", "green", "yellow"]
for c in colors:
	print(c)
index = linear_search(colors, "red")
# I made a function that searched the list called colors in a 
# linear search pattern and returned the index of the given value.
print(f' {index} is the index of the value you chose')


# cookies = ["chocolate", "butterscotch", "vanilla"]

















# import random
# import matplotlib.pyplot as plt



# Array = [1, 2, 3, 4, 5, 6, 7, 8]

# def sum_search(given_array):
#   total = 0
#   for each i in given_array:
#     total += i
#   return total



# linear = O(n)
# constant time = O(1)
# quadratic time = O (n squared)

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
# def total(colors):
#     r = 0
#     for num in colors:
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
# def find_pair(colors, target):
#     for num1 in colors:
#         for num2 in colors:
#             if num1 + num2 == target:
#                 return [num1, num2]
#     return None

# # O(n^2)
# # def has_duplicates(colors):
# #     for i in range(len(colors)):
# #         print('outer loop', colors[i])
# #         for j in range(len(colors)):
# #             if i == j:
# #                 print('same number, skipping')
# #                 continue
# #             print('inner loop', colors[i], '==', colors[j], '?')
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
