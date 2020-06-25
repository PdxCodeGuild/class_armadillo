
#            0          1         2
fruits = ['apples', 'bananas', 'pears']
nums = [56, 57, 58]
random = ['a', 5, 5.1, True, ['hi']]


# print(fruits[0]) # apples
# print(fruits[1]) # bananas
# # print(fruits[4]) #IndexError: list index out of range
# print(fruits[-1]) # pears
# print(fruits[-2]) # bananas


# think of slicing as either
# 1) exclusive on the upper bound
# 2) referring to the spaces between elements
#            0         1          2         3           4          5           6        7
#         0        1          2         3          4         5            6         7
fruits = ['apples', 'bananas', 'pears', 'avocado', 'tomato', 'pomegranate', 'kiwi', 'raspberries']
# print(fruits[3:6]) # from index 3 to 6
# print(fruits[:5]) # from the start to index 5
# print(fruits[3:]) # from index 3 to the end
# print(fruits[::2]) # get every other element
# print(fruits[::-1]) # reverse





# copy() creates a copy of the list ============================

fruits = ['apples', 'bananas', 'pears']
otherlist = fruits.copy()
otherlist.append('avocado')
# print(otherlist)
# print(fruits)


# append() appends an element to the end ============================

# strings return copies
# s = 'hello '
# s = s + 'world'

# lists modify the original
# fruits = fruits.append('blackberries') # no 
fruits.append('blackberries')
# print(fruits)

# insert() inserts the value at the specified index ============================


fruits = ['apples', 'bananas', 'pears']
fruits.insert(1, 'avocado')
# print(fruits)


# remove() removes the first occurance of the element ============================


fruits = ['apples', 'bananas', 'pears', 'bananas']
fruits.remove('bananas')
# print(fruits)

fruits = ['apples', 'bananas', 'pears', 'bananas']
while 'bananas' in fruits:
  fruits.remove('bananas')
# print(fruits)

fruits = ['apples', 'bananas', 'pears', 'bananas']
fruits = [fruit for fruit in fruits if fruit != 'bananas']
# print(fruits)


# pop() removes the element at the given index ============================


fruits = ['apples', 'bananas', 'pears']
fruit = fruits.pop(2)
# print(fruits)
# print(fruit)


# extend() combines two lists into one ============================

fruits = ['apples', 'bananas', 'pears']
fruits2 = ['avocado', 'kumquat', 'tomato']
fruits.extend(fruits2)
# fruits.append(fruits2) # VERY different
print(fruits)





# index() returns the index of a given element ============================

fruits = ['apples', 'bananas', 'pears']
print(fruits.index('bananas'))


# reverse() reverses a list ============================

fruits = ['apples', 'bananas', 'pears']
fruits.reverse()
print(fruits)

# sort() sorts a list ============================

fruits = ['apples', 'bananas', 'pears', 'avocado', 'kumquat']
fruits.sort()
print(fruits)


# iterables: string, list, tuple, dictionary, range


# text = 'hello world!'
# print(list(reversed(text)))

# print(sorted('hello world!'))

