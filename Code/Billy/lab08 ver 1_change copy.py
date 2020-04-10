import time


print('\n' + '~'*22)
print('Let\'s make change...')
print('~'*22)

time.sleep(1)

user_cash =  int(input('Please enter your amount: (number of  pennies) '))

quarters = user_cash//25
user_cash -= quarters*25
dimes = user_cash//10
user_cash -= dimes*10
nickels = user_cash//5
user_cash -= nickels*5
pennies = user_cash

# Alternate method 2.
# quarters = user_cash//25
# dimes = (user_cash - (quarters*25))//10
# nickels = (user_cash -((quarters*25) + (dimes*10)))//5
# pennies = (user_cash - (((quarters*25) + (dimes*10) + (nickels*5))))

print(f'\nQuarters: {quarters}\nDimes: {dimes}\nNickels: {nickels}\nPennies: {pennies}\n')



'''
Lab 8: Make Change
Let's convert a dollar amount into a number of coins. The input will be the total amount, 
the output will be the number of quarters, dimes, nickles, and pennies.
Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

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