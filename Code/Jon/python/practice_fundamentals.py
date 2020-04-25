# Problem 1
# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)
def is_even(num):
    return num % 2 == 0
# print(is_even(5)) # False
# print(is_even(6)) # True

# Problem 2
# Write a function that takes two integers, a and b, and returns True if one is positive and the other is negative, and return False otherwise.
def opposite(num1, num2):
    return num1 < 0 and num2 > 0 or num1 > 0 and num2 < 0

# print(opposite(10, -1)) # True
# print(opposite(2, 3)) # False
# print(opposite(-1, -1)) # False

# Problem 3
# Write a function that returns True if a number within 10 of 100.
def near_100(num):
    return num >= 90 and num <= 110
    
# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True

# Problem 4
# Write a function that returns the maximum of 3 parameters.
def maximum_of_three(num1, num2, num3):
    # return max(num1,num2,num3)
    num_list = []
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)

    max_number = 0

    for num in num_list:
        print(num_list)
        if num > max_number:
            max_number = num

    return max_number

# print(maximum_of_three(5,6,2)) # 6
# print(maximum_of_three(-4,3,10)) # 10

# Problem 5
# Write a loop to print the powers of 2 from 2^0 to 2^20
def print_powers_2(num):
    for i in range(6):
        print(num**i)
        
print(print_powers_2(2)) # 1, 2, 4, 8, 16, 32, ...
