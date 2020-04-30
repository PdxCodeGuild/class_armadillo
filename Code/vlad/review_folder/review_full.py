#review_full  April 23 2020

# assigning the int literal 5 to the variable x

# the python interpreter only allocates one object
# s1 = 'hello'
# s2 = 'hello'
# print(id(s1))
# print(id(s2))

# ints are immutable, y+1 creates a new object, x is unchanged
x = 5
y = x
y = y + 1
print(x)
print(id(x))
print(id(y))

# lists are mutable, y.append also changes the object pointed to by x
x = ['a', 'b', 'c']
y = x
y.append('d')
print(x)
print(id(x))
print(id(y))


# relflection - look into the guts of things
# print(dir('hello'))
# import inspect
# print(inspect.getmembers('hello'))

# data types ============================

# None
# bool / boolean
# int / integer
# float / floating point number
# str / string
# list / list
# tuple / tuple
# dict / dictionary
# range

print(type(5)) # <class 'int'>

x = range(10)
print(x)
print(type(x))

# functions are also variables
p = print
p()
p('hello world!')
p()


# identity vs equality =========================
# == - equality
# is - identity

# a = 'hello'
# b = 'hello'
# if a == b:
#   print('equal')


# two different objects with the same value
letters1 = ['a', 'b', 'c']
letters2 = ['a', 'b', 'c']
print(id(letters1))
print(id(letters2))

if letters1 == letters2: # test for equality
  print('equal') # printed
if letters1 is letters2: # test for identity
  print('same object') # not printed


x = 5
y = x
print(x is y)



# None ==========================================



x = None
y = None
print(id(x)) # 2011602152
print(id(y)) # 2011602152
print(id(None)) # 2011602152

# there's one None object in the entire python program
# we should use 'is' instead of '=='

# if x == None:
if x is None:
  print('x is none')

# int, float ====================================

x = 5
y = 6
z = x + y
print(z)

x = 5
x += 2
print(x)

# floor division
print(5 / 2) # 2.5
print(5 // 2) # 2

# absolute value
print(abs(5)) # 5
print(abs(-5)) # 5

# min, max
print(min(5, 2)) # 2
print(max(5, 2, 1)) # 5
print(sum([1, 2, 3])) # 6

# round
print(round(3.14159263)) # 3
print(round(3.14159263, 3)) # 3.142

import math
print(math.pi) # 3.141592653589793


# for vs while =========================================
# while is better if the condition is indefinite
#     don't know how many times you'll loop
# for is better if you do know how many times you'll loop

i = 0
while i < 10:
  print(i)
  i = i + 1

# continue_looping = True
# while continue_looping:
#   user_input = input('should we keep looping? ')
#   if user_input == 'no':
#     continue_looping = False

# for loop with range ========================
# 1 argument - upper bound
# loops 10 times, llama will go 0, 1, 2, 3, ... 9
for llama in range(10):
  print(llama)

# 2 arguments - lower bound and upper bound
# loop 5 times, i will go 5, 6, 7, 8, 9
for i in range(5, 10):
  print(i)

# 3 arguments - lower bound, upper bound, increment
# loop 20 times, i will go 100, 105, 110, ... 195
for i in range(100, 200, 5):
  print(i)

# these are the same
# for i in range(10)
# for i in range(0, 10, 1)

# test how many times you loop - 12
counter = 0
for i in range(67, 103, 3):
  counter += 1
print(counter)


# for with string =======================================

mystring = 'hello'

# iterate over the characters
for char in mystring:
  print(char)

#           01234
mystring = 'hello'
print(mystring[2]) # l
# len(mystring) is 5
# for i in range(5) will go 0, 1, 2, 3, 4
for i in range(len(mystring)):
  print(i, mystring[i])

# iterating over the indices is helpful if you want to re-use the index
string1 = 'hello'
string2 = 'bye!!'
for i in range(len(string1)):
  print(i, string1[i], string2[i])

#          01234
string1 = 'hello'
for i in range(len(string1)-1):
  print(i, string1[i], string1[i+1])


# for with lists =======================================

#           0    1    2    3    4    5    6    7
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# iterate over the elements of the list
for letter in letters:
  print(letter)

# iterate over the indices of a list
# len(letters) is 8
# range(8) will go 0, 1, 2, ... 7
for i in range(len(letters)):
  print(letters[i])

# b, c, d, e, f
for i in range(1, len(letters)-2):
  print(letters[i])

# b, c, d, e, f
for letter in letters[1:6]:
  print(letter)


# remove a's
# letters = ['a', 'b', 'c', 'a', 'c', 'd', 'a']
# for letter in letters:



# functions ==========================================================

# functions allow you to re-use code, write them once, call them multiple times
# functions should be self-contained
#   not refer to any external variables
#   they should only operate on the parameters that are given
#   return instead of print
#   this helps avoid side-effects, which makes code less predictable


def min(a, b):
  if a < b:
    return a
  return b


def print_contacts(contacts):
  for contact in contacts:
    print(contact)
contacts = ['joe', 'jim', 'jane', 'jill']
print_contacts(contacts)


# get a list of ints from the user
def get_nums():
  numbers = []
  while True:
    num = input('enter a number or \'done\': ')
    if num == 'done':
      break
    numbers.append(int(num))
  return numbers

# print(get_nums())
# print(get_nums())






def add(a, b):
  print(a + b)
c = add(5, 2)
print(c)


def add(a, b):
  return a + b
print(add(5, 2))
c = add(5, 2)
c += 1
with open('myfile.txt', 'w') as file:
  file.write(str(c))






# dictionaries =======================================================
# a collection key-value pairs

# dictionaries
# keys can be any immutible type - bools, int, float, string, tuples
# values can be any type

prices = {
  'apples': 1.0,
  'bananas': 1.5,
  'pineapple': 3.0
}
# get a value from a dictionary using the key
print(prices['apples']) # 1.0
# changing the value of a dictionary using a key
prices['apples'] = 5
prices['apples'] += 1
print(prices['apples']) # 6
# if a dictionary does not have the key it'll crash
# print(prices['cherries']) # KeyError: 'cherries'
# checking if the dictionary has the key
if 'cherries' in prices: # if prices contains the key 'cherries'  
  print(prices['cherries'])

# get the value if it's in the dictionary
# or the specified default if it's not
price_cherries = prices.get('cherries', 3.5)


# using del to remove an element from a list
letters = ['a', 'b', 'c', 'd']
del letters[0]
print(letters) # ['b', 'c', 'd']

# using del to remove a key-value pair from a dictionary
prices = {'apples': 1.0, 'bananas': 1.5, 'pineapple': 3.0}
del prices['apples']
print(prices)

# using pop to remove a key-value pair to a dictionary
prices = {'apples': 1.0, 'bananas': 1.5, 'pineapple': 3.0}
print(prices.pop('apples'))
print(prices)
# specify a default to return if the key isn't found in the dictionary
print(prices.pop('apples', 1.0))
print(prices)



# iterables
# range, list, tuple, dict, list_reverseiterator, dict_keys, dict_values, dict_items

# for num in reversed([1, 2, 3]):
#   print(num) # 3, 2, 1

# x = reversed([1, 2, 3])
# print(x)
# print(type(x))

prices = {'apples': 1.0, 'bananas': 1.5, 'pineapple': 3.0}
print(list(prices.keys())) # ['apples', 'bananas', 'pineapple']
print(list(prices.values())) # [1.0, 1.5, 3.0]
print(prices.items()) # [('apples', 1.0), ('bananas', 1.5), ('pineapple', 3.0)]

# iterate over the keys of a dictionary
for key in prices:
  print(key, prices[key]) # using the key to access the value
# iterate over the values directly
for value in prices.values():
  print(value)
# iterate over the keys and values simultaneously
for key, value in prices.items():
  print(key, value)



# find the key for a given value
# value = 1.5
# for key in prices:
#   if prices[key] == value:
#     print(key)


# add all the key-value pairs from the given dictionary
# equivalent to list.extend()
prices.update({
  'cherries': 1.12
})
print(prices) # {'apples': 1.0, 'bananas': 1.5, 'pineapple': 3.0, 'cherries': 1.12}



prices = {'apples': 1.0, 'bananas': 1.5, 'pineapple': 3.0}
price = prices.setdefault('cherries', 5.0)
print(price) # 5.0
print(prices) # {'apples': 1.0, 'bananas': 1.5, 'pineapple': 3.0, 'cherries': 5}
price = prices.setdefault('bananas', 5.0)
# if 'bananas' not in prices:
#   prices['bananas'] = 5.0
# price = prices['bananas']
print(price)
print(prices)
