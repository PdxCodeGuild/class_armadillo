#Let's convert a dollar amount into a number of coins.
#The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies.
#Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
#For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Version 1     Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

# User enters total in pennies

i_amount = input("Enter the total amount you have in pennies: ")

print(i_amount, 'pennies')