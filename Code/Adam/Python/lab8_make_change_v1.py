"""

Lab 8: Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered
-conditionals, comparisons
-arithmetic

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

"""

import time

play =  True

while play:
    participate = str(input("Want to convert cash into coin? yes or no..."))
    if participate == "yes":

        time.sleep(1)

        og_dollar_amount = input("How much cash you got? $")

        time.sleep(1)

        dollar_amount = int(float(og_dollar_amount)*100)

        n_quarters = dollar_amount // 25
        dollar_amount -= n_quarters*25
        
        n_dimes = dollar_amount // 10
        dollar_amount -= n_dimes*10

        n_nickels = dollar_amount // 5
        dollar_amount -= n_nickels*5

        n_pennies = dollar_amount

        time.sleep(1)

        print(f"${og_dollar_amount} converts to: \n    {n_quarters} quarters \n    {n_dimes} dimes \n    {n_nickels} nickels \n    {n_pennies} pennies")
        
    elif participate == "no":
        time.sleep(1)
        print("Goodbye...")
        play = False