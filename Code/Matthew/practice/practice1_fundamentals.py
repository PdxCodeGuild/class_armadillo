


def is_even(a):
  
  if a%2 == 0:
    return True
  else:
    return False
  
  # the else is redundant because return leaves the function immediately
  if a%2 == 0:
    return True
  return False

  # nice and short
  return a%2 == 0



# print(is_even(5)) # False
# print(is_even(6)) # True

# for i in range(10):
#   print(i, is_even(i))



def opposite(a, b):
  # if a*b < 0:
  #   return True
  # return False

  # return a*b < 0

  if a < 0 and b > 0:
    return True
  elif a > 0 and b < 0:
    return True
  return False

  return (a < 0 and b > 0) or (a > 0 and b < 0)

  
# print(opposite(10, -1)) # True
# print(opposite(-10, 100)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False


# Problem 3 =====================================
# Write a function that returns True if a number within 10 of 100.

def near_100(num):
  return 90 <= num <= 110

  # return abs(100-num) <= 10
  
  # if num >= 90 and num <= 110:
  #   return True
  # return False

# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True


# Problem 4 ================================


def maximum_of_two(a, b):
  if a > b:
    return a
  else:
    return b
  
  # return a if a > b else b


# print(maximum_of_two(5, 2)) # 5
# print(maximum_of_two(10, 16)) # 16

def maximum_of_three(a, b, c):
  if b < a > c:
    return a
  elif c < b > a:
    return b
  return c

  # nums = [a, b, c]
  # nums.sort()
  # return nums[-1]

  # if a > b:
  #   if a > c:
  #     return a
  #   else:
  #     return c
  # elif b > c:
  #   return b
  # else:
  #   return c

  # if a > b and a > c:
  #   return a
  # elif b > a and b > c:
  #   return b
  # else:
  #   return c
  
# print(maximum_of_three(5,6,2)) # 6
# print(maximum_of_three(-4,3,10)) # 10

# import random
# for i in range(100):
#   a = random.randint(1, 99)
#   b = random.randint(1, 99)
#   c = random.randint(1, 99)
#   print(a, b, c, maximum_of_three(a, b, c))



# Problem 5
# Write a loop to print the powers of 2 from 2^0 to 2^20

# print(2 ** 0)
# print(2 ** 1)
# print(2 ** 2)
# print(2 ** 3)
# print(2 ** 4)
# print(2 ** 5)
# print(2 ** 6)
# print(2 ** 7)

def print_powers_2():
  for i in range(21):
    print(2 ** i)
print_powers_2() # 1, 2, 4, 8, 16, 32, ...