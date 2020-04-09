# Let's convert a dollar amount into a number of coins.
# The input will be the total amount, the output will be
# the number of quarters, dimes, nickles, and pennies.
# Always break the total into the highest coin value first,
# resulting in the fewest amount of coins. For this,
#  you'll have to use floor division //,
#  which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# V.1
# Have the user enter the total number in pennies, e.g. for $1.36,
# the user will enter 136.

# V.2
# Have the user enter a dollar amount (1.36), convert this to the
# total in pennies.

# V.3 (optional)
# Instead of hard-coding the coins, store them in a list.
# This way you can make custom coins.

# coins = [
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]

import math
import time

print("Welcome to Your Automated Cashier ")
time.sleep(2)

amount = input("Please Enter Dollar amounts to Convert to Change.  $")
amount = int(float(amount)*100)


quarters = amount // 25
amount -= quarters * 25

dimes = amount // 10
amount -= dimes * 10

nickles = amount // 5
amount -= nickles * 5

pennies = amount // 1
amount -= pennies * 1

print("Quarters: " + str(quarters))
print("Dimes: " + str(dimes))
print("Nickles: " + str(nickles))
print("Pennies: " + str(pennies))