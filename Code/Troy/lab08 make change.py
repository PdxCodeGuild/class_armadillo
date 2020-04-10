

import random
import math
import time


coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

user_amount = input('Enter how much money you have kind person and I will break it down for you. ')
user_amount = int(float(user_amount)*100)

quarters = user_amount // 25
user_amount -= quarters * 25

dimes = user_amount // 10
user_amount -= dimes * 10

nickels = user_amount // 5
user_amount -= nickels * 5

pennies = user_amount

print(f'You have {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.')


