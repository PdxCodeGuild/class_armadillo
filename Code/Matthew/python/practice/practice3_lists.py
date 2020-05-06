
import random

# Problem 1 ==============================================
# Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

def random_element(fruits):
  i = random.randint(0, len(fruits)-1)
  return fruits[i]

#            0           1        2         3
fruits = ['apples', 'bananas', 'pears', 'cherries']
# print(random_element(fruits)) # 'apples', 'bananas' or 'pears'

for i in range(100):
  print(random_element(fruits))

# for i in range(100):
#   print(random.randint(5, 10))


# Problem 3 =================================================
# Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

from practice1_fundamentals import is_even

# import practice1_fundamentals
# practice1_fundamentals.is_even(5)


def eveneven(nums):
  # evens = []
  # for num in nums:
  #   if is_even(num):
  #     evens.append(num)
  #   print(num, evens)
  # return is_even(len(evens))

  counter = 0
  for num in nums:
    if is_even(num):
      counter += 1
  return is_even(counter)

print(eveneven([5, 6, 2, 1, 2, 3, 2, 4, 2])) # False
print(eveneven([5, 5, 2])) # False