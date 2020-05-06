

# import random just loads random.py
# C:\Users\flux\AppData\Local\Programs\Python\Python38-32\Lib

# import module1
# print(module1.x)
# print(module1.add(5, 2))

# from module1 import x, add
# print(x)
# print(add(5, 2))


# from module1 import x as y
# print(y)

# from random import choice as random_choice
# print(random_choice([1, 2, 3]))



# BAD, implicitly import everything
# could have namespace clashes that are hard to debug
# x = 20
# from module1 import *
# print(x)


# import module0
# print(module0.string.ascii_lowercase)


# from myimports import *
# print(random.randint(5, 10))

# from random import choice, randint
# import string, math
# print(math.acosh(1.0))


# print(__name__)
import module1


print(module1.add(10, 10))



import mypackage.mymodule
print(mypackage.mymodule.x)



