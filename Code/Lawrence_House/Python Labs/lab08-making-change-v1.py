#Let's convert a dollar amount into a number of coins.
#The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies.
#Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
#For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Version 1     Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136.

# User enters total in pennies

i_amount = int(input("Enter the total amount you have in pennies: "))

# Conversion to individual coins

q_amount = i_amount//25
i_amount -= q_amount*25

d_amount = i_amount//10
i_amount -= d_amount*10

n_amount = i_amount//5
i_amount -= n_amount*5

p_amount = i_amount//1   

# Total amount in different coins

print(q_amount, 'quarters')
print(d_amount, 'dimes')
print(n_amount, 'nickels')
print(p_amount, 'pennies')
