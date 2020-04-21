#Practice 1: Fundamentals April 21 2020 Keegan Group: saved under file fundametals_practice.py under Keegan GitHub

#https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/practice/practice01-fundamentals.md


# Fundamentals Practice
# April 21, 2020

# Problem 1
def is_even(num):
    '''
    Tells whether a number is even or odd
    Returns True if even, False if odd
    '''

    # longer way:
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    # one-liner:
    return num % 2 == 0

# print(is_even(5)) # False
# print(is_even(6)) # True


# Problem 2
def opposite(a, b):
    '''
    returns True if one is positive and the 
    other is negative, and return False otherwise.
    '''

    # Verbose way:
    # if (a > 0 and b < 0) or (a < 0 and b > 0):
    #     return True
    # else:
    #     return False

    # short way:
    return (a > 0 and b < 0) or (a < 0 and b > 0)

# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False


# Problem 3
def near_100(num):
    '''
    Returns True if a number within 10 of 100, otherwise returns False.
    '''
    
    # Verbose way:
    # if num >= 90 and num <= 110:
    #     return True
    # else:
    #     return False

    # combining the conditionals into one
    # if 90 <= num <= 110:
    #     return True
    # else:
    #     return False

    # method 1:
    # return num >= 90 and num <= 110

    # method 2:
    return 90 <= num <= 110

    # method 3:
    # return abs(num - 100) <= 10

# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True


# Problem 4
def max_of_three(a, b, c):
    '''
    returns the maximum of 3 parameters: a, b, c
    '''
    # if a > b and a > c:
    #     return a
    # elif b > a and b > c:
    #     return b
    # elif c > a and c > b:
    #     return c    

    # current max value
    greatest = a

    # looping through unpacked tuple (a, b, c)
    for num in a, b, c:
        # if the current number is greater than the current max value
        if num > greatest:
            # override current max value
            greatest = num

    return greatest 

    # shortest way:
    # return max([a,b,c])

# print(max_of_three(-9999, -1001, -2000))
# print(max_of_three(5,6,2)) # 6
# print(max_of_three(-4,3,10)) # 10

# Problem 5
def powers_2(n):
    '''
    Return a list of the powers of 2 from 0 to n
    '''

    powers_2 = []
    for exponent in range(n):
        powers_2.append(2 ** exponent)

    return powers_2

# print(powers_2(5))
# print(powers_2(10))
print(powers_2(20))