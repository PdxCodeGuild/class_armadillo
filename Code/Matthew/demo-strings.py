

# import random
# random.randint(0, 10)




s = 'hello'
s += ' world'
print(s)


# print('~-'*40)
# print(s)
# print('~-'*40)

print(len(s)) # 11

print(s[0]) # h
print(s[1]) # e

print(s[3:10]) # lo worl
print(s[:10]) # hello worl
print(s[3:]) # lo world

print(s[::2]) # hlowrd
print(s[::-1]) # dlrow olleh

print(s.find('world')) # 6
print(s.find('goodbye')) # not found: -1

print(s.upper()) # HELLO WORLD
print(s.lower()) # hello world

print(s.startswith('hello')) # True
print(s.endswith('hello')) # False

print(s.replace('hell', 'heaven')) # heaveno world

print('    hello   '.strip())
print('__|_jello__|_____'.strip('_|'))


print(s.split(' '))
print('_'.join(['hello', 'world']))


a = 5
b = 2
print(f'the lower of {a} and {b} is {a if a < b else b}')


print('hello' in s) # True

for char in s:
    print(char)
