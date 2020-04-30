#review_loops by instructor: 


# while ===================================

# i = 1
# while i <= 10:
#   print(i, 'looping!')
#   i += 1
# print('done')

# user_input = ''
# count = 0
# while user_input != 'done':
#   user_input = input('enter a number or \'done\': ')
#   count += 1
#   print(user_input)
# print(count)

# for ===================================

# llama is an arbitrary variable name
# each iteration it will be a different value
# if you give range a single number
# it will loop from 0 up to but not including that number
# for llama in range(10):
#   print(llama)

# two numbers - lower bound and upper bound
# for i in range(1, 11):
#   print(i)


# three numbers - lower bound, upper bound, increment
# for i in range(0, 101, 5):
#   print(i)



# for i in range(20, 0, -1):
#   print(i)


# nums = []
# for i in range(0, 101, 5):
#   nums.append(i)
# print(nums)

# nums = list(range(0, 101, 5))
# print(nums)

# using a range to iterate over the indices of a list
#            0          1         2          3          4
# fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocado']
# for i in range(len(fruits)):
#   print(i, fruits[i])
# print()

# iterate over the indices of a list in reverse
# for i in range(len(fruits)-1, -1, -1):
#   print(i, fruits[i])

fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocado']

# for i in range(len(fruits)):
#   fruits[i] += '!'
# print(fruits)

# this won't work because strings are immutible
# fruit += '!' just creates a new object
# fruits = ['apples', 'bananas', 'pears', 'cherries', 'avocado']
# for fruit in fruits:
#   fruit += '!'
# print(fruits)

# fruit = fruits[0]
# fruit += '!'
# print(fruits[0])

# fruits = [
#   {
#     'name': 'apples',
#     'price': 1.0
#   },{
#     'name': 'bananas',
#     'price': 2.0
#   },{
#     'name': 'cherries',
#     'price': 3.0
#   }
# ]
# for fruit in fruits:
#   fruit['name'] += '!'
#   fruit['price'] *= 1.06
# print(fruits)


# iterate over the characters of a string
# text = 'hello world!'
# output = ''
# for char in text:
#   output += char+char
# print(output)


# import random
# nums = [random.randint(1, 20) for i in range(100)]
# nums = list(set(nums))
# print(nums)


# iterate over the keys of a dictionary
# prices = {
#   'apples': 1.0,
#   'bananas': 2.0,
#   'cherries': 3.0
# }
# for key in prices:
#   print(key, prices[key])






# continue, break ===================================


fruits = ['apples', 'bananas', 'cherries', 'avocado', 'kumquot']
for fruit in fruits:
  if fruit == 'bananas':
    continue
  elif fruit == 'pears':
    break
  print(fruit)
else:
  print('will run if you don\'t break')