#Demo list in class by the instructor! 

mixed = [3, 'red', 45.012, [3, 5]]
for element in mixed:
    print(f'{element} is a {type(element)}')

print(3 in mixed)

#            0         1         2          3           4          5         6
fruits = ['apples', 'bananas', 'pears', 'avocados', 'kiwis', 'jackfruit', 'tomato']

print(len(fruits)) # 7

print(fruits[0]) # apples
print(fruits[1]) # bananas
print(fruits[-1]) # tomato
print(fruits[-2]) # jackfruit
print(fruits[len(fruits)-1]) # other languages don't use


# int *nums = new int[100] # allocate 100 integers, integers a 4 bytes each, here's 400 bytes
# std::cout << nums << std::endl # 0x672CV35
# nums[0]
# nums + 0*4

print(fruits[1:5]) # ['bananas', 'pears', 'avocados', 'kiwis']
print(fruits[:5]) # ['apples', 'bananas', 'pears', 'avocados', 'kiwis']
print(fruits[5:]) # ['jackfruit', 'tomato']

print(fruits[::2]) # ['apples', 'pears', 'kiwis', 'tomato']
print(fruits[::-1]) # ['tomato', 'jackfruit', 'kiwis', 'avocados', 'pears', 'bananas', 'apples']


# fruits = ['apples', 'bananas', 'pears', 'avocados', 'kiwis', 'jackfruit', 'tomato']
# fruits2 = fruits.copy()
# print(id(fruits))
# print(id(fruits2))
# fruits2[0] = 'cherries'
# print()
# print(fruits)
# print(fruits2)

# import random
# nums = [1, 2, 3, 4]
# nums2 = nums.copy()
# random.shuffle(nums2)
# print(nums)
# print(nums2)

# a = 'hello'
# b = a
# print(id(a))
# print(id(b))
# b = b + 'world'
# print(a)
# print(b)

# a = ['hello']
# b = a
# print(id(a))
# print(id(b))
# b.append('world')
# print(a)
# print(b)


fruits = ['apples', 'bananas', 'pears', 'avocados', 'kiwis', 'jackfruit', 'tomato']
fruits.append('grapes')
print(fruits)


fruits.insert(1, 'raspberry')
print(fruits)


fruits.remove('avocados')
print(fruits)

fruit = fruits.pop(0)
print(fruit)
print(fruits)


fruits2 = ['avocados', 'apples']
# fruits.append(fruits2) # no (probably not)
fruits.extend(fruits2)
print(fruits)

print(fruits.index('pears')) # 2
# print(fruits.index('not there')) # crash


fruits.reverse() # ['apples', 'avocados', 'grapes', 'tomato', 'jackfruit', 'kiwis', 'pears', 'bananas', 'raspberry']
print(fruits)
fruits.sort() # ['apples', 'avocados', 'bananas', 'grapes', 'jackfruit', 'kiwis', 'pears', 'raspberry', 'tomato']
print(fruits)

# fruits.sort()
# for fruit in fruits:
#     print(fruit)

# for fruit in sorted(fruits):
#     print(fruit)

# for fruit in reversed(fruits):
#     print(fruit)



person = ('Bob', 36, 'red')
print(person[0]) # Bob
print(person[1]) # 36










