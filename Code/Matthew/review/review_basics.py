

# I/O - input, print ====================================================

# name = input('what is your name? ')
# print(name)

# age = int(input('what is your age? '))
# print(age + 1)

# sep is what's printed between the values
# end is printed at the end

# print('hi', end=' ')
# print('hello', end=' ')
# print('bye')

# print('apples', 'bananas', 5.0)
# print('apples', 'bananas', 5.0, sep=' ', end='\n') # default
# print('apples', 'bananas', 5.0, sep='_')
# print('apples', 'bananas', 5.0, sep='__', end='\n\n')
# print('hi')

# print('hello\nthere')


# types ====================================================

# None - placeholder, the absence of a value

x = None
if x is None:
  ...
# print(x)
# print(type(x))

# x = None
# y = None
# print(id(x))
# print(id(y))

# use case for None
# number_grade = 87
# letter_grade = None
# if number_grade > 90:
#   letter_grade = 'A'
# elif number_grade > 80:
#   letter_grade = 'B'
# print(letter_grade)

# int - integer ====================================

x = 10

# float - floating point number =====================

x = 10.0
# print(5 + 5.0)



# x = float('nan')
# y = float('inf')
# z = float('-inf')
# print(x)
# print(y)
# print(z)

# def min(nums):
#   running_min = float('inf')
#   for num in nums:
#     if num < running_min:
#       running_min = num
#   return running_min



# import math
# print(math.log(0))

# try:
#   1/0
# except ZeroDivisionError:
#   print('error caught')

# string - text ====================================

x = 'I\'m a string'

# list - ordered collection ====================================

x = ['apples', 'bananas', 'pears']
x[0] = 'avocado'
# print(x)

# tuple - immutible lists ====================================
# tuples are usually used to group together heterogeneous data

x = ('apples', 5.0)
# x[0] = 'avocado' # no
# x.append('avocado) # no


# dictionary ====================================

x = {'apples': 5.0, 'bananas': 6.0}
# print(x['apples'])

# conversion functions ====================================


# bool()
# int()
# float()
# str()
# list()
# tuple()
# dict()

# everything is truthy except False, 0, None, '', [], {}

# while True:
# if 5 == 5:
# x = 5
# if x:


# if 'False':
# if 5:
#   print('5 is True I guess??')

# print(bool('False'))
# print(int('5'))
# print(float('5.0'))

# age = 5
# print('my age is ' + str(age))

# fruits = ['apples', 'bananas', 'pears']
# fruits = str(fruits)
# print(fruits)

# print(list('abc123'))


# arithmetic ====================================

# + - * / **

# floor division - throws away the remainder
# print(5/2)
# print(5//2)

# modulus - gives the remainder of the division
# print(5%2)
# print(122%100)

# x = 5
# if x%2 == 0:
#   print('x is even')
# else:
#   print('x is odd')

# fruits = ['apples', 'bananas', 'pears']
# for i in range(100):
#   print(i, i%len(fruits), fruits[i%len(fruits)])


# abs, round, min, max, sum =================================

# print(abs(-5))

# print(round(5.2))
# print(round(5.8))
# print(round(3.1415963, 3))

# print(min(1, 2, 3, 4))
# print(max(1, 2, 3, 4))
# print(sum([1, 2, 3, 4]))




