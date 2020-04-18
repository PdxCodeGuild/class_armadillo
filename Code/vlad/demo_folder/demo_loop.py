# Demo loop in class by instructor! 

# 1 number - upper bound
# 0 to 99 (100 times)
for i in range(100):
    print(i)

# 2 numbers - lower bound and upper bound
# 1 to 100 (100 times)
for i in range(1, 101):
    print(i)

# 3 numbers - lower bound, upper bound, and increment
# 1 to 100, every 2 numbers (50 times)
for i in range(1, 101, 2):
    print(i)

# iterate over the elements of a list
fruits = ['apples', 'bananas', 'pears']
for fruit in fruits:
    print(fruit)

# does NOT work
# for fruit in fruits:
#     fruit += '!'
# print(fruits)

#             0          1        2
fruits = ['apples', 'bananas', 'pears']
print(fruits[0]) # apples
for i in range(3):  # 0, 1, 2
    print(fruits[i])
    fruits[i] += '!'
print(fruits)

# very different use of 'in'
# if 'apples' in fruits:
#     pass

# iterate over the characters in a string
for char in 'hello world!':
    print(char)

