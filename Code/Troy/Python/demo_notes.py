import math

# x = float('nan')
# print(math.isnan(x))

# c=int(input('Please enter an amount between 0-99:'))
# print(c//25)
# print(c%25)

# s= 'hello'
# s += ' world'
# print(s)

# s = 'hello'
# print(s*10)

# '''Version 2'''
# import math

# user_distance= int(input('What is the distance? '))
# user_input = input('What unit would you like to convert? ')
# user_output = input('What unit do you want it converted to? ')
# # print('That converts to...')

# distance_conversions = {'inches': 0.0254,
#                         'feet': 0.3048,
#                         'yards': 0.9144,
#                         'meters': 1,
#                         'miles': 1609.34,
#                         'kilometers': 1000
# } 

# #user_distance = int(user_distance)

# total = user_distance * (distance_conversions[user_input]  /distance_conversions[user_output])

# print(f"The grand total is...{total}")
    



import random
import math
import time

# coins = [
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]

# user_amount = input('Enter your pennies kind person and I will break it down for you. ')
# user_amount = int(float(user_amount)*100)

# quarters = user_amount // 25
# user_amount -= quarters * 25

# dimes = user_amount // 10
# user_amount -= dimes * 10

# nickels = user_amount // 5
# user_amount -= nickels * 5

# pennies = user_amount

# print(f'You have this many {quarters} quarters, this many {dimes} dimes, this many {nickels} nickels, and this many {pennies} pennies.')

# a and b are called parameters
# def add(a, b):
#     return a + b
# print(add(5, 2))
# print(add(8, 1))


# def is_even(a):
#     ...
# print(is_even(5)) #False
# print(is_even(6)) #True



# def validate_credit_card(card):
#     # Convert the input string into a list of ints
#     card = list(card)

#     # Convert each string to an int.
#     for i in range(len(card)):
#         card[i] = int(card[i])

#     # Slice off the last digit. That is the check digit.
#     check_digit = card.pop(-1)

#     # Reverse the digits.
#     card.reverse()

#     # Iterate over every other list element in the reversed list and double it.
#     for i in range(0, len(card), 2):
#         card[i] = card[i] * 2

#     # Iterate over every number in the list and subtract nine from numbers > 9.
#     for i in range(len(card)):
#         if card[i] > 9:
#             card[i] -= 9
#     print(card)

#     # Iterate over every number in the list and sum all values.
#     card_sum = 0
#     for i in range(len(card)):
#         card_sum = card_sum + card[i]

#     # Take the second digit of that sum.
#     card_sum = card_sum % 10
#     print(card_sum)
#     # If that matches the check digit, the whole card number is valid.
#     if card_sum == check_digit:
#         return True
#     else:
#         return False


# is_valid = validate_credit_card('4556737586899855')
# print(is_valid)


# Problem 3 Write a function that returns True if a number within 10 of 100.

# def near_100(num):
#     if num >= 90 and <= 110  

#     if num in range(90, 111):
#         return True
#     else: False 
#     ...
# print(near_100(50)) # False
# print(near_100(99)) # True
# print(near_100(105)) # True


# Problem 4 Write a function that returns the maximum of 3 parameters.

# def maximum_of_three(a, b, c):
#     nums = sorted ([a, b, c])
#     returns nums[-1]

#     nums = [a, b, c]
#     nums.sort()
#     return nums[-1]
# #     ...
# print(maximum_of_three(5,6,2)) # 6
# print(maximum_of_three(-4,3,10)) # 10

# def say_hello():
#     print('hello!')


# def print_every_other_with_for(nums):

#     new_list = []
#     for i in range(0, len(nums), 2):
#         new_list.append(nums[i])
    
# print(new_list)


# print_every_other_with_for([0, 1, 2, 3, 4, 5, 6, 7, 8][::-1])

# def Reverse(lst): 
#     lst.reverse() 
#     return lst 
      
# lst = [10, 11, 12, 13, 14, 15] 
# print(Reverse(lst)) 

