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


# Import math used to import the arithmatic modual 
# in order to perform the math portion of the program
# Import time modual is to break up the welcome message and the input message... and I really like the Import time modual
import math
import time
# Welcome Message
print("Welcome to Your Automated Cashier ")
time.sleep(2)
# This is for the user to import the dollar amount they wish to have change made for
amount = input("Please Enter Dollar amounts to Convert to Change.  $")
# This takes the amount provided by the user and the float function is to allow the user 
# to put their amount in dollar and cents form (1.36) instead of having to enter it as a whole number (136). 
# Then multiplies it by 100 
amount = int(float(amount)*100)

# This portion breaks the user amount down to decibles in order to place the change 
# into it's assigned position Quarters, Dimes, Nickles or pennies
quarters = amount // 25
amount -= quarters * 25

dimes = amount // 10
amount -= dimes * 10

nickles = amount // 5
amount -= nickles * 5

pennies = amount // 1
amount -= pennies * 1
# This section prints out how many Quatres, Dimes, Nickles and Penneies the 
# user will get back depending on how much they entered at the start
print("Quarters: " + str(quarters))
print("Dimes: " + str(dimes))
print("Nickles: " + str(nickles))
print("Pennies: " + str(pennies))