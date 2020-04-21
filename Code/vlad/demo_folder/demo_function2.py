#  Demo function2 04 21 2020 by instructor: 



# calculator using functions as variables ============================

# def add(a, b):
#   return a + b

# def subtract(a, b):
#   return a - b

# operators = {
#   '+': add,
#   '-': subtract
# }
# print(operators)

# operator = input('what is the operator? ')
# operand1 = float(input('what is the operand 1? '))
# operand2 = float(input('what is the operand 2? '))

# print(operators[operator](operand1, operand2))





# using a function as a variable ===============

def say_hello():
  print('hello!')

# y = say_hello
# y()

# implicit return of None

# print(say_hello)
# print(say_hello())
# x = say_hello()
# print(x)



def add(a, b):
  print(id(a))
  return a + b

# num1 = 5
# num2 = 7
# print(id(num1))
# num3 = add(num1, num2)
# print(num3)
# print(add(10, 5))



# scoping ====================================

def functionA(a, b):
  print(z)

def functionB():
  x = 5
  y = 6
  z = 7
  functionA(x, y)


# print(x) # crash - x is not defined
# functionA(5, 2) # crash - z is not defined


# make functions self-contained
# only operate on the parameters, and return something
# no side effects - no changing external variables, no printing
# calling the function with the same paramters should give the same result
# code predictability

# nums = []
def get_numbers():
  nums = [] # move declaration to inside the list to avoid side-effects
  while True:
    num = input('enter a number or \'done\': ')
    if num == 'done':
      break # leaves the loop immediately, no need for an else
    nums.append(int(num))
  return nums

# print(get_numbers())
# print(get_numbers())





# crashes
# def add(a=1, b):
#   return a + b
# print(add(5))


# crash
# def add(a, b=1, c):
#   return a + b + c


def add(nums):
  total = 0
  for num in nums:
    total += num
  return total

# add([1, 2, 3, 4])
# add((1, 2, 3, 4))


# putting * before a parameter allows you to take any number of arguments
# they're turned into a tuple
# syntactic sugar
def add(*nums):
  print(nums)
  print(type(nums))
  total = 0
  for num in nums:
    total += num
  return total

# add(1, 2)
# add(1, 2, 3)
# add(1, 2, 3, 4)



x = 10
print(x := 20)
y = (x := 20) + 1

print(f'{x=}')



# **kwargs

def print_prices(prices):
  for key in prices:
    print(key, prices[key])
print_prices({'apples': 1.0, 'bananas': 2.0, 'cherries': 3.0})

def print_prices(**prices):
  for key in prices:
    print(key, prices[key])
print_prices(apples=1.0, bananas=2.0, cherries=3.0)


# returning multiple values =====================

# long way, less fancy
def get_dimensions():
  return [500, 200]
dimensions = get_dimensions()
width = dimensions[0]
height = dimensions[1]


# short way, more fancy
def get_dimensions():
  return 500, 200
# dimensions = get_dimensions()
width, height = get_dimensions()
print(width)
print(height)


# example - swapping element in a list
#       0  1  2
nums = [1, 2, 3]

# can't do this, we erase nums[0]
# nums[0] = nums[2]
# nums[2] = nums[0]
# print(nums)

# this is how to swap in other languages
# t = nums[0]
# nums[0] = nums[2]
# nums[2] = t
# print(nums)

# tuple unpacking   tuple packing
# nums[0], nums[2] = nums[2], nums[0]
# print(nums)


# lambda expressions ============================

# def add(a, b):
#   return a + b
# add = lambda a, b: a + b
# print(add(5, 2))

# increment = lambda x: x + 1
# x = 10
# x = increment(x)
# x = increment(x)
# print(x)

# passing a function as a parameter what?!?
def perform_operation(nums, f):
  for i in range(len(nums)):
    nums[i] = f(nums[i])

# longer way
def double(x):
  return x * 2
nums = [1, 2, 3, 4]
perform_operation(nums, double)
print(nums)

# shorter way
nums = [1, 2, 3, 4]
print(nums)
perform_operation(nums, lambda x: x**2)
print(nums)




#https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/docs/09%20-%20Functions.md
# Functions
# Functions are isolated pieces of code that take input, perform some operation, and return a result. Functions we've used so far include input(), print(), len(), etc. Python provides many built-in functions for you to use. For all the built-in functions, check the official docs

# Built-In Functions
# I/O
# input() prompts the user for input on the terminal
# print() displays text to the user on the terminal
# Arithmetic Functions
# abs() returns the absolute value of a number
# round() rounds a number, an optional second argument can specify how many decimal places the output should have
# min() returns the minimum of the values passed to it
# max() returns the maximum of the values passed to it
# sum() returns the sum of the values passed to it
# Type Conversion
# int() converts a value to an int
# float() converts a value to a float
# str() converts a value to a string
# chr() converts an int to a string containing the character with that unicode value, for example chr(97) returns the string 'a'
# bool() converts a value to a boolean
# list() converts a value to a list
# tuple() converts a value to a tuple
# set() converts a value to a set
# dict() converts a value to a dict
# List Operations
# len() returns the length of a list
# sorted() sorts a list
# reversed() reverses a list
# Defining Functions
# We can define our own functions using the def keyword. This allows us to execute sections of code repeatedly.

# def say_hello():
#     print('hello!')

# say_hello()
# say_hello()
# say_hello()

# >>> hello!
# >>> hello!
# >>> hello!
# The function above takes no parameters and returns no values. You can specify parameters by listing variables in the parantheses of the function definition.

# Parameters
# def say_hello(first_name, last_name):
#     print('Hello ' + first_name + ' ' + last_name)

# fn = input('what is your first name? ')
# ln = input('what is your last name? ')
# say_hello(fn, ln)
# Notice that the variable names outside the function don't have to match the variable names inside the function. When the values are passed as parameters, they take on new names, local only to the function.

# Passing by Position
# Thus far, we’ve been passing arguments to functions by position. The values at the call site are bound to the variables in the function signature in order.

# def subtract(a, b):
#   return a - b
# subtract(5, 8)  #> -3 (a=5, b=8)
# Optional Arguments
# Most positional arguments are like the above, required arguments. But it’s also possible to have functions that take optional arguments. If they are specified when the function is called, then the caller’s value is used. Otherwise, the default value from the function definition is used.

# def subtract(a, b=1):
#   return a - b
# subtract(5)  #> 4 (a=5, b=1)
# subtract(5, 8) # -3 (a=5, b=8)
# Passing by Keyword
# Optional arguments may also be passed by keyword in any order, as long as they come after all positional arguments.

# def subtract(a, b=1, c=0):
#   return a - b - c
# subtract(5, b=8) # -3 (a = 5, b = 8, c = 0)
# subtract(5, c=9) # -5 (a=5, b=1, c=9)
# subtract(5, c=9, b=8) # -12 (a=5, b=8, c=9)
# *args & **kwargs
# When reading more advanced Python code, you might see functions written like the following:

# def print_movie_ratings(username, *args, **kwargs):
#     """Update the user’s ratings for movies.
#     Update movies from *args that are keys in **kwargs.
#     """
#     for arg in args:  # Loop through the tuple `args`
#         if arg in kwargs:  # Loop through keys of the `kwargs` dictionary
#             print(arg, kwargs[arg])

# print_movie_ratings('jane', 'Sharknado', 'Frozen', 'Transformers', Sharknado=3, Frozen=2, Fargo=5)

# """ Output is:
# Sharknado 3
# Frozen 2
# """
# This syntax is used to create functions that can take a varying number of arguments.

# Note: The special thing about these variable names isn’t args and kwargs. It’s the * and **. You can name these arguments anything that’s a legal variable name, but by convention they’re named *args and **kwargs.

# Within the function above, *args is defined as a tuple of the positional arguments passed to the function that don’t have explicit names in our function signature. **kwargs is defined as a dictionary of any keyword arguments passed to the function that don’t match keywords in the function signature. You can find more information about both here.

# Returning
# We can also return values from a function, which is often the result of some computation or operation. The code below returns the lesser of two values. Notice we don't need an else, once a the interpreter reaches a return, it immediately exits a function.

# def min(a, b):
#     if a < b:
#         return a
#     return b
# x = min(5, 2)
# print(x)
# 2

# Implicit Return - None
# If a function does not return anything, it implicitly returns None

# def say_hi():
#     print('hi')
# x = say_hi()
# print(x)
# None

# Returning Multiple Values
# You can return multiple values using automatic tuple packing and unpacking.

# def get_dimensions():
#     return 500, 200
# width, height = get_dimensions()
# print(width)
# print(height)
# 500 200

# Recursion
# Functions can call other functions, producing a chain of invocation. Functions can even call themselves, this is called recursion. It's important to have a 'stop condition', otherwise this results in infinite recursion and you'll get a 'stack overflow'.

# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)
# def fibonacci(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
#  # this only works on sorted lists
# def binary_search_recurse(num, nums, low, high):
#     if low >= high:
#         return None
#     mid = (low + high) // 2
#     if nums[mid] == num:
#         return mid
#     elif nums[mid] < num: # search in the upper half
#         return binary_search_recurse(num, nums, mid+1, high)
#     else: # search in the lower half
#         return binary_search_recurse(num, nums, low, mid+1)

        
# def binary_search(num, nums):
#     return binary_search_recurse(num, nums, 0, len(nums)-1)
# Lambda Functions
# Lambda expressions are a shorter way to define functions and are written as lambda arguments: expression.

# a = lambda x,y: x + y
# print(a(5,4)) # 9

# s = lambda x,y: x-y
# print(s(5,4)) # 1