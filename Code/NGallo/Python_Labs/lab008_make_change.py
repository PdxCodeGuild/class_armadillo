
coins = [
    ('quarter', .25),
    ('dime', .10),
    ('nickel', .05),
    ('penny', .01)
]

user_amount = input("enter the cash value you have (example $159.16): $")
user_amount = int(float(user_amount)*100)
quarters = user_amount // 25
user_amount -= quarters * 25
dimes = user_amount // 10
user_amount -= dimes * 10
nickles = user_amount // 5
user_amount -= nickles * 5
pennies = user_amount

print(f"The number of quarters you would need to make change are:\n quarters: {quarters} \ndimes:{dimes} \nnickles:{nickles} \npennies:{pennies}")


'''
Lab 8: Make Change
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quar1ters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered
conditionals, comparisons
arithmetic
Version 1
Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

Version 2
Have the user enter a dollar amount (1.36), convert this to the total in pennies.

Version 3 (optional)
Instead of hard-coding the coins, store them in a list. This way you can make custom coins.

coins = [
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
'''