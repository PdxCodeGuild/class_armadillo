import random
# verbose way:
# numbers = []
# for i in range(10):
#     if i % 2 == 0:
#         numbers.append(i)
#     else:
#         numbers.append("*")

# comprehension way:
# list_name = [action | loop | if-condition]
# numbers = [i for i in range(10) if i % 2 == 0]

# list_name = [action | if-else condition | loop]
# numbers = [i if i % 2 == 0 else '*' for i in range(10)]

# print(f"{numbers = }")

# ----------------------------------- #

# nested comprehension
# letters = 'abc'
# letter_list = [[letters[j] for i in range(len(letters))] for j in range(len(letters))]

# print(letter_list)

# ----------------------------------- #

# def even_evens(numbers):
#     '''
#     Return True if there is an even number 
#     of even numbers in a list
#     '''
#     return len([num for num in numbers if num % 2 == 0]) % 2 == 0

# list1 = [5, 6, 2] # True
# list2 = [5, 5, 2] # False
# print(even_evens(list1))
# print(even_evens(list2))

# ----------------------------------- #

# def get_every_other(nums):
#     '''
#     Print out every other element of a list using a while loop.
#     '''
#     return [nums[i] for i in range(len(nums)) if i % 2 == 0]

# num_list = [random.randint(1,100) for i in range(1,10)]  # list comprehension for creating a list with 10 random integers between 1 and 10
# print(num_list)
# print((get_every_other(num_list)))

# ----------------------------------- #

# def reverse(nums):
#     '''
#     Write a function that returns the reverse of a list.
#     '''
#     return [nums[i] for i in range(len(nums)-1, -1, -1)]

# num_list = [random.randint(1,100) for i in range(1,10)]  # list comprehension for creating a list with 10 random integers between 1 and 10
# print(num_list)
# print((reverse(num_list)))

# ----------------------------------- #

# Dictionary comprehension
# dict_name = {key:value | loop}
# fruits = ['guava', 'kiwi', 'mangosteen']

# prices = {fruits[i]:round(random.random(), 2) for i in range(len(fruits))}

# print(f"{prices = }")

# names = ['shankar', 'lakshmi', 'shiva']

# employees = {name:'' for name in names}

# print(f"{employees = }")