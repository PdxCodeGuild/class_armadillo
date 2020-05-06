


def fibonacci(n):
  nums = [1, 1]
  for i in range(2, n):
    nums.append(nums[i-1] + nums[i-2])
  return nums

print(fibonacci(100))



def factorial(n):
  r = 1
  for i in range(2, n+1):
    r *= i
  return r

# 4! = 4*3*2*1 = 24
# 5! = 5*4*3*2*1 = 120
# 6! = 7*6*5*4*3*2*1 = 720

def factorial_recursive(n):
  print(f'factorial({n})')
  if n == 1:
    print('hit base case, returning 1')
    return 1
  print(f'calling factorial({n-1})')
  result = n*factorial_recursive(n-1)
  print(f'returning {result}')
  return result

# print(factorial(4))
# print(factorial(5))
# print(factorial_recursive(10))


def fibonacci_recursive(n):
  print(f'fibonacci({n})')
  if n == 0 or n == 1:
    return 1
  return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(10))