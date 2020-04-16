# This originally is not my program. I copied it from another site. 
# I wa having issues understanding this version of the change maker, 
# so I used this example to understand how everything worked in it.
# I did go through and break each section and rebuilt it as a 
# learning tool and made some chages to somewhat make it mine.

# Import math is for the same reason as the previous version
# Import time for the same reason as the previous version to slow the 
# program down a little at the beggining to allow the user to read 
# the welcome message... again because I really like this sleep portion
# of this modual
import math
import time

# Welcome message
print("Welcom to Your Automated Cashier V.2")
time.sleep(1)
# This is for the user to import the dollar amount they wish to have change made for
input_amount = input("How much change would you like. $")
# This takes the amount provided by the user and the float function is to allow the user 
# to put their amount in dollar and cents form (1.36) instead of having to enter it as a whole number (136). 
# Then multiplies it by 100 
amount = int(float(input_amount) * 100)

# For this version a list is used to pull from instead of hard programing each coin into the program.
coins = [
    ("Quarters", 25),
    ("Dimes", 10),
    ("Nickels", 5),
    ("Pennies", 1)
]
# This section is simular to the previous math wise but instead of each 
# coin being hard programed this is where the program pulls from the list instead
coin_amounts = []
for coin in coins:
    coin_amount = amount //coin [1]
    amount -= coin_amount *coin [1]
    coin_amounts.append (coin_amount)
# This is the print message that shows how the dollar amount is broken down into coins. Quarters, Dimes, Nickles, Pennies.
print("$" + input_amount + " is...")
for i in range(len(coin_amounts)):
    print("\t" + coins[i] [0] + ":" + str(coin_amounts[i]))