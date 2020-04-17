# Lab 8: Make Change Version 3!

# """
# Let's convert a dollar amount into a number of coins. The input will be the total 
# amount, the output will be the number of quarters, dimes, nickles, and pennies.
# Always break the total into the highest coin value first, resulting in the fewest 
# amount of coins. 
# For this, you'll have to use floor division //, which throws 
# away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Concepts Covered
# conditionals, comparisons
# arithmetic
# Version 1
# Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.
# """
# """"
# Version 1
# Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

# Version 2
# Have the user enter a dollar amount (1.36), convert this to the total in pennies.

# Version 3 (optional)
# Instead of hard-coding the coins, store them in a list. This way you can make custom coins.

# coins = [
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]


input_amount = input("Enter the amount you want to break into change \n please enter e.g. 8.67 do not enter round numbers ? $")
amount = int(float(input_amount)*100)

print(amount)

quarters = amount // 25
amount -= quarters * 25
dimes = amount // 10
amount -= dimes * 10
nickles = amount // 5
amount -= nickles * 5
pennies = amount 



print(f"${input_amount} is {quarters} quarters, {dimes}dimes, {nickles} nickles, and {pennies} pennies")  


''' Sample from Class:
# print(round(3.1415963, 2))
input_amount = input('What is the amount you\'d like to break into change? $')
amount = int(float(input_amount)*100)
# we take the var from line 4 and we wrap that inside of float ( * 100)
# the reason we wrap it is b/c decimals are FLOAT, not INT
# bool('True')
# int()
# float()
# str()
# list()
# tuple()
# dict()
coins = [
    ('quarters', 25),
    ('dimes', 10),
    ('nickels', 5),
    ('pennies', 1)
]
# quarters = amount / 25
# dimes = amount / 10
coin_counts = []
for coin in coins:
    coin_count = amount // coin[1]  #floor division = 100 / 25 = 4
    amount = amount - ( coin_count * coin[1] )
    #amount -= coin_count * coin[1]
    coin_counts.append(coin_count)
print('$' + input_amount + ' is ...')
for i in range(len(coin_counts)):
    print('\t' + coins[i][0] + ': ' + str(coin_counts[i]))
'''