import math



#
# global fruits
# fruits = ['apple']
#
# def add(a, b):
#     global fruits
#     fruits += ['pear']
#
# add(5, 2)
#
# print(fruits)
#
# exit()



class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p):  # method, or 'member function'
        dx = self.x - p.x
        dy = self.y - p.y
        return math.sqrt(dx * dx + dy * dy)

    def scale(self, v):
        self.x *= v
        self.y *= v

    def __str__(self):
        return f'[{self.x}, {self.y}]'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


p1 = Point(5, 2)
p2 = Point(5, 2)
dist = p1.distance(p2) # or p2.distance(p1), either works


# if p1.__eq__(p2):
if p1 == p2:
    print('equal')
else:
    print('not equal')


