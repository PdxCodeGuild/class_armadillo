
def add(a, b):
    return a + b

# print(add(5, 2))
# print(add(8, 1))


# problem 1 ============================

def is_even(a):
    return a%2 == 0
    # if a % 2 == 1:
    #     return False
    # else:
    #     return True




# print(is_even(5))
# print(is_even(6))


def opposite(a, b):
    if a > 0 and b > 0:
        return False
    elif a < 0 and b < 0:
        return False
    elif a == 0 or b == 0:
        return False
    else:
        return True

    #return (a > 0 and b < 0) or (a < 0 and b > 0)


# print(opposite(10, -1))
# print(opposite(2, 3))
# print(opposite(-1, -1))
# print(opposite(0, 0))

# Write a function that returns True if a number within 10 of 100.

def near_100(num):
    return abs(num - 100) <= 10
# print(near_100(50))
# print(near_100(-99))
# print(near_100(-105))


# Write a function that returns the maximum of 3 parameters.
def maximum_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    elif b > c:
        return b
    else:
        return c
# print(maximum_of_three(5,6,2))
# print(maximum_of_three(-4,3,10))

# Print out the powers of 2 from 2^0 to 2^20
# 1, 2, 4, 8, 16, 32, ...

i = 0
while i < 21:
    print(2**i)
    i += 1
