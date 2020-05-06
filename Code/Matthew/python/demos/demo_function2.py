



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


def add():
  print(nums)
  total = 0
  for num in nums:
    total += num
  return total


add([1, 2, 3, 4])
# add((1, 2, 3, 4))
exit()

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



# x = 10
# print(x := 20)
# y = (x := 20) + 1

# print(f'{x=}')



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
