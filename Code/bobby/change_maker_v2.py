import math
import time

print("Welcom to Your Automated Cashier V.2")
time.sleep(1)
input_amount = input("How much change would you like. $")
amount = int(float(input_amount) * 100)

coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
coin_amounts = []
for coin in coins:
    coin_amount = amount //coin [1]
    amount -= coin_amount *coin [1]
    coin_amounts.append (coin_amount)

print("$" + input_amount + " is...")
for i in range(len(coin_amounts)):
    print("\t" + coins[i] [0] + ":" + str(coin_amounts[i]))