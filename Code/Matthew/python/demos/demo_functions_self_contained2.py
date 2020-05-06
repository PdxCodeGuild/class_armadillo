


import random



nums = []
def get_random_numbers(n):
  for i in range(n):
    nums.append(random.randint(0, 10))
  return nums

# get two lists of random numbers
# one of length 5, one of length 10
print(get_random_numbers(5))
print(get_random_numbers(10))


