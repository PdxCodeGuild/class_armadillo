

def say_hello():
    print('hello')
say_hello()



# make function self contained
# only operater on the parameters, and return something
# no side affects - no changing external variables , no printing
# import random
# tempeture = random.randit(50, 100)
# if tempeture < 60:


# tempeture = 65
# message = ''
# if tempeture < 60:
#     message = 'cold'
# elif tempeture < 80:
#     message = 'warm'
# else:
#     message = 'hot'
# print(message)

# # scope - range of code in visable variable
# def add(a, b):
#     c = 10
#     print(c) #totally fine
#     return a + b
# #print(c)# crash - c not defined
# print(add(5, 2))

# make functions self-contained


def get_number():
    nums = []# move declaration inside the list tp avoid side-efect
    while True:
        num = input('Enter numer or \'done\': ')
        if num == 'done':
            break# leaves if done entered
        nums.append(int(num))# puts input into list
    return nums

print(get_number())


def get)_dimention():
    return 500, 200

width, height = get_dimention()
print(width)
print(height)

#lambda expressions========================================

# add = lambda a, b: a + b
# print(add(5, 2))

# increasment = lambda x: x + 1
# x = 10
# x = increasment(x)
# x = increasment(x)
# print(x)



a = [5,8,2,4]
max = 0
for i in a:
    if i <