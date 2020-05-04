#demo_classes using classes 


# class - grouping of data and functions that serve a common purpose
#         helps organize code
# type - interchangable with class (e.g. boolean, string, list, ...)
# object - a unit of data, has a place in memory
#          everything in python is an object
# initializer - how we instantiate objects in Python, called a constructor in other language
# instantiation - created an object from a class (blueprints)
# instance - synonymous with object
# property - data associated with an object
# self - within a class, it's your own instance
# method - a function associated with a class (e.g. string.split, list.append)
# __dict__ - a dictionary that represents an object, used "under the hood"





# functions are objects too
# def add(a, b):
#     return a + b
# print(id(add))
# print(add(5, 2))
# print(add)
# print(type(add))
# a = add
# print(a(5, 2))

# even classes are objects
# class Point:
#     pass
# print(Point)
# print(type(Point))

import math

class Point:
    def __init__(self, m=0, n=0):
        # print(x)
        # print(y)
        # print(self)
        # print(type(self))
        self.x = m
        self.y = n
        self.z = 'hello'
    
    def distance(self, p): # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx*dx + dy*dy)
    
    def scale(self, v):
        self.x *= v
        self.y *= v
    
    def __str__(self):
        return f'({self.x},{self.y})'

p1 = Point(4, 2)
# print(p1.x) # 4
p1.scale(2)
print(p1.x, p1.y) # 8 4

p2 = Point(8, 12)
d = p1.distance(p2)
# d = Point.distance(p1, p2) # more confusing way to write the above
print(d) # 8

p = Point(10, 24)
# without __str__, this would print <__main__.Point object at 0x02FF8220>
print(p) # (10,24)

p_str = str(p)
# p_str = p.__str__() # more confusing way to write the above
print(p_str) # (10,24)


# p1 = Point(5,2)
# p2 = Point(8,4)
# dist = p1.distance(p2) # or p2.distance(p1), either works
# print(dist)

#  # similar to how we can call methods of the str class
# s = 'hello world'
# print(s.split(' '))