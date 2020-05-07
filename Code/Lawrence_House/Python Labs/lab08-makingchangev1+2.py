#Let's convert a dollar amount into a number of coins.
#The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies.
#Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
#For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

#   Version 1

#i_amount = input("Enter the total amount of pennies you have: ")

#   Version 2

i_amount = input("Enter the total amount of pennies you have: ")

amount = int(float(i_amount)*100)

print(amount,'pennies')