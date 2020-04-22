"""


"""

import random

def random_list(n): # generates and returns a list of length n, with random values between 0 and 100
  ...

def shuffle(nums): # randomly re-arranges a list
  # iterate through the indices of the list
  # for each index, generate a random index (random.randint)
  # swap the elements at the two indices
  #
  # example
  # indices    0  1  2  3  4
  # elements   5, 7, 4, 2, 8
  # iter 1     i        j
  # elements   2, 7, 4, 5, 8
  # iter 2     j  i     
  # elements   7, 2, 4, 5, 8
  # iter 3           i     j
  # elements   7, 2, 8, 5, 4
  ...

def is_sorted(nums): # checks if a list is sorted
  # iterate through the indices of the list
  # if the element at the current index is greater than the element at the next index, the list isn't sorted, and you can return False
  # if you get through the entire list and each element is less than or equal to the next element, the list is sorted, and you can return True
  #
  # e.g. 1,2,4,3
  ...

def bogosort(nums):
  while not is_sorted(nums):
    shuffle(nums)


# step 1
# nums = random_list(100)
# print(nums)

# step 2
# nums = random_list(100)
# print(nums)
# shuffle(nums)
# print(nums)

# step 3
# nums = [1, 2, 3, 4]
# print(is_sorted(nums)) # true
# nums = [1, 2, 4, 3]
# print(is_sorted(nums)) # false

# finale
# nums = random_list(100)
# print(nums)
# bogosort(nums)
# print(nums)
