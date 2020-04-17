# strings ================================

# s = 'I\'m a string'
# s = "double quotes work too"

# escape sequences

# print('hello\nworld') # newline
# print('hello\tworld') # tab
# print('hello\'world') # singke-quote
# print('hello\"world') # double-quote
# print('hello\\world') # backslash


# len, [] =========================

# print(len('hello world'))

s = 'hello world'
# print(s[6])

# slicing =========================
#    0123456789
s = 'hello world'
# print(s[3:9]) # lo wor
# print(s[:9]) # hello wor
# print(s[9:]) # ld
# print(s[::2]) # hlowrd
# print(s[::-1]) # dlrow olleh

# upper, lower =========================

print('Hello'.lower())
print('Hello'.upper())


# startswith, endswith =========================

# print('hello world'.endswith('world')) # True
 
# replace =========================

# print('hello world it\'s a great day'.replace(' ', '@'))
# print('hello world it\'s a great day'.replace(' ', '@', 3))

# split, join =========================

print('hello world it\'s a great day'.split(' '))
print('hello world it\'s a great day'.split('o'))
print('\n'.join(['apples', 'bananas', 'pears']))

# cannot directly join a list of ints because .join() uses string concatenation
nums = [1, 2, 3]
nums = [str(num) for num in nums]
# for i in range(len(nums)):
#   nums[i] = str(nums[i])
print(nums)
print(' '.join(nums))


# f-strings ==================================

# x = 5
# print('my number is ' + str(x))
# print(f'my number is {x}, {x+1}')