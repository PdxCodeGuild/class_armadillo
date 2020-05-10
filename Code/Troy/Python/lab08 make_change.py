# Lab 08 Make Change
# Troy Fitzgerald


#imports modules.
import random
import math

# defines coin names and coin amounts in a dictionary.
coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

# has user enter the amount of money they have.
user_amount = input('Enter how much money you have kind person and I will break it down for you. ')
user_amount = int(float(user_amount)*100)

# defines coin amounts and amount to be divided into the input.
quarters = user_amount // 25
user_amount -= quarters * 25

dimes = user_amount // 10
user_amount -= dimes * 10

nickels = user_amount // 5
user_amount -= nickels * 5

pennies = user_amount

# prints out the broken down amount by coin type.
print(f'You have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.')


