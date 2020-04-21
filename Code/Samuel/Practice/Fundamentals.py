# Returns True if the given value is even
# Returns False if it is not.
def is_even(a):
    return True if a%2 == 0 else False

# Returns True if the numbers are on opposite sides of 0.
# Returns False if they are not.
def opposite(a, b):
    return True if a * b < 0 else False

# Returns True if the number is within 10 units of 100.
# Returns False if not.
def near_100(a):
    return 90 <= a <= 110

# Returns the maximum value of the three numbers given.
def maximum_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c

# Prints the powers of 2 up to 2**20.
def print_powers_2():
    for i in range(20):
        print(2**i, end=" ")
    print("\n")

# Tests
if __name__ == "__main__":
    print(is_even(5))
    print(is_even(4))

    print(opposite(9,-1))
    print(opposite(-5, 6))
    print(opposite(6,6))

    print(near_100(85))
    print(near_100(96))
    print(near_100(111))

    print(maximum_of_three(2,6,7))
    print(maximum_of_three(2,6,6))

    print_powers_2()