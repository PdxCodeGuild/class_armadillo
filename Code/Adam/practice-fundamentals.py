"""-------------------------------------------Practice 1: Fundamentals-------------------------------------------"""

# Problem 1 - write a function that determines if a number is even. 
# Even numbers are divisible by 2 and have no 0.

def is_even(num):
    rem = num%2
    if rem > 0:
        rem = False
    elif rem == 0:
        rem = True
    return(rem)
# print(is_even(5)) # False
# print(is_even(6)) # True


# # Problem 2 - write a function that returns true if two values have opposite signs
# 2 numbers with the same sign produce a positive number; opposing signs produce a negative number

def opposite(a, b):
    if (a < 0 and b < 0) or (a > 0 and b > 0):
        product = False
    elif (a > 0 and b < 0) or (a < 0 and b > 0):
        product = True
    return(product)
# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False


# Problem 3 - write a function that returns True if a number is within 10 and 100.

def near_100(num):
    if num >= 90 and num <= 110:
        num = True
    elif num < 90 or num > 110:
        num = False
    return(num)
# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True


# Problem 4 - write a function that returns the maximum of 3 parameters

def max_of_three(a, b, c):
    if b < a > c:
        return(a)
    elif a < b > c:
        return(b)
    elif a < c > b:
        return(c)
# print(max_of_three(5,6,2)) # 6
# print(max_of_three(-4,3,10)) # 10


#Problem 5 - write a loop to print the powers of 2 from 2^0 to 2^20

def print_powers_2():
    for i in range(21):
        a = 2**i
        print(f"2^{i} = {a}")
        i += 1
    return()
print_powers_2() # 1, 2, 4, 8, 16, 32, ...