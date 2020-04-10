amount = 136
quarters = amount // 25
amount -= quarters*25
print("quarters: ' + str(quarters))
print("new amount: ' + string(amount))

#print(amount//25)
#print(amount//10)
#print(amount//5)
#print(amount//1)









Lab 8: Make Change

Let's convert a dollar amount into a number of coins. 
The input will be the total amount, the output will 
be the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value first, 
resulting in the fewest amount of coins. For this, you'll 
have to use floor division //, which throws away the 
remainder. 10/3 is 3.333333, 10//3 is 3.

Concepts Covered
conditionals, comparisons
arithmetic

$1.25 

dollar = int(input("1.25 "))

output = ("5 quarters")

$1.21

dollar = int(input("1.21"))

output = ("4 quarters", "2 dime", "1 penny")


quarter = 4
dime = 2
penny = 1

Version 1
Have the user enter the total number in pennies, e.g. 
    for $1.36, the user will enter 136.