


def add(a, b):
  return a + b
c = add
print(c(5, 2))


exit()



def say_hello(first_name, last_name):
  print('Hello ' + first_name + ' ' + last_name)






# a = 'joe'
# b = 'shmoe'
# c = say_hello(a, b)
# print(c)

# nums = reversed([1, 2, 3])
# print(nums)
# print(list(nums))


def min(a, b):
  if a < b:
    return a
  else:
    return b

# print(min(5, 2)) # 2
# c = min(5, 2)
# print(c)


def subtract(a=1, b=1):
  return a - b

# print(subtract(5))
# print(subtract(5, 2))
# print(subtract(5, b=2))
# print(subtract(a=5, b=2))




# add_numbers takes any number of arguments
def add_numbers(*nums):
  print(nums)
  total = 0
  for num in nums:
    total += num
  return total


nums = [1, 2, 3, 4]

print(add_numbers(1, 2, 3, 4)) # 10
print(add_numbers(6, 7, 8, 9)) # 30
print(add_numbers(*nums)) # 10


print('hello')
print('hello', 'world')
print('hello', 'world', 'abc123llama')
print('hello', 'world', '!!', sep='_')
print('hello', 'world', '!!', sep='_', end='^_^')
print('hi')

print('xxxxx')
print('=~'*40)
for i in range(5):
  print('x', end='')
print()

# def print(*args, sep=' ', end='\n'):


full_name = input('what is your name? ').split(' ')
print(full_name)
first_name, last_name = full_name
print(first_name)
print(last_name)





