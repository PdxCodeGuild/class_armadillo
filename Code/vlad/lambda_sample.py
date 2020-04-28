
# lambda sample: 
short and very poor example of lambda functions 
def add(x, y):
    return x + y
print(add(5, 6))

inline lambda
print((lambda x,y: x + y)(5,6))

set lambda to a variable
add = lambda x,y: x + y
print(add(5,6))